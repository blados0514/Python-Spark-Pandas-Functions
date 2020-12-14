import pandas as pd


delimiter = ';'
#Archivo a leer
name_file_read = 'contribuyente.csv'
#archivo a exportar el resultado
name_file_export = 'contribuyentes.txt'
#nombre de la columna de busqueda
name_column = 'ID_USUARIO'

df_temp = pd.DataFrame(data=None, columns = [name_column,'INCONSISTENCIAS'])

#Ruta donde esta los archivos
path = 'C:\\Users\\BlaimirOspinaCardona\\Desktop\\Impuestos\\'

#ruta para leer el archivo
path_input = path + name_file_read
#ruta para exporta el archivo
path_out_put = path + name_file_export

datos = pd.read_csv(path + name_file_read, delimiter = delimiter, header = 'infer')
datos[name_column] = datos[name_column].astype('str')

"""
ft_unificar_inconsistencia
Esta funcion unica los errores por el campo columna parametrizado
"""

def ft_unificar_inconsistencia(ar_id_usuario):
  error = ''
  for inconsistencia in datos[datos[name_column] == ar_id_usuario]['INCONSISTENCIA']:
    error = error + inconsistencia + '; '
  return error

for identificacion in datos[name_column].unique():
  new_row = {name_column:identificacion, 'INCONSISTENCIAS':ft_unificar_inconsistencia(identificacion)}
  df_temp = df_temp.append(new_row,ignore_index=True)
df_temp[name_column] = df_temp[name_column].astype('str')


df_contribuyentes = pd.merge(df_temp, datos, on = name_column, how='inner')
df_contribuyentes = df_contribuyentes.drop(["INCONSISTENCIA"], axis=1)
df_reporte = pd.DataFrame(data=None, columns = df_contribuyentes.columns)


for index in df_contribuyentes[name_column].unique():
  df_reporte = df_reporte.append(df_contribuyentes[df_contribuyentes[name_column] == index].head(1))

df_reporte.to_csv(path + name_file_export, sep = '|', index = False)