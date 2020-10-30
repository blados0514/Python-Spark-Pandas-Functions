import os
import sys
from pyhive import hive
from thrift.transport import THttpClient
import base64

TOKEN = "<token>"
WORKSPACE_URL = "<databricks-instance>"
WORKSPACE_ID = "<workspace-id>"
CLUSTER_ID = "<cluster-id>"

conn = 'https://%s/sql/protocolv1/o/%s/%s' % (WORKSPACE_URL, WORKSPACE_ID, CLUSTER_ID)
print(conn)

transport = THttpClient.THttpClient(conn)

auth = "token:%s" % TOKEN
PY_MAJOR = sys.version_info[0]

if PY_MAJOR < 3:
  auth = base64.standard_b64encode(auth)
else:
  auth = base64.standard_b64encode(auth.encode()).decode()

transport.setCustomHeaders({"Authorization": "Basic %s" % auth})

cursor = hive.connect(thrift_transport=transport).cursor()

cursor.execute('show tables')
for table in cursor.fetchall():
    print(table)