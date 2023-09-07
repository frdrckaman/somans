from sqlalchemy.engine import URL
from sqlalchemy import create_engine
import cx_Oracle
from cx_Oracle import Error
import os
from pathlib import Path

connection_string_cims_uat = f"DRIVER=ODBC Driver 17 for SQL Server;SERVER=00172TANSQLU1P,59403;DATABASE=CIMS_PHASE2_UAT;ENCRYPT=yes;TrustServerCertificate=Yes;MultiSubnetFailover=Yes;UID=data_user;PWD=Stanbic1*"
connection_url_cims_uat = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string_cims_uat})
engine_cims_uat = create_engine(connection_url_cims_uat)

conn = cx_Oracle.connect("readonly", "readonly", "(DESCRIPTION=(SOURCE_ROUTE=YES)(ADDRESS_LIST=(ADDRESS=(PROTOCOL=TCP)(HOST=ytzocm3.tz.sbicdirectory.com)(port=1621))(ADDRESS=(PROTOCOL=TCP)(HOST=ytzoda8-scan2.tz.sbicdirectory.com)(PORT=1521)))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=ptz3cor.tz.sbicdirectory.com)))")

