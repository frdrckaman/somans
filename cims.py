from sqlalchemy import create_engine
import pandas as pd
import env_mixin

engine = create_engine(env_mixin.ORA_CONN_STRING_DR)

df = pd.read_sql_query("select trunc(sysdate -4) from DUAL", engine)

print(df)

