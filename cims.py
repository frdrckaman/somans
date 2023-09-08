from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("oracle+cx_oracle://readonly:readonly@(DESCRIPTION=(SOURCE_ROUTE=YES)(ADDRESS_LIST=(ADDRESS=(PROTOCOL=TCP)(HOST=ytzocm3.tz.sbicdirectory.com)(port=1621))(ADDRESS=(PROTOCOL=TCP)(HOST=ytzoda8-scan2.tz.sbicdirectory.com)(PORT=1521)))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=ptz3cor.tz.sbicdirectory.com)))")

df = pd.read_sql_query("select trunc(sysdate -4) from DUAL", engine)

print(df)

