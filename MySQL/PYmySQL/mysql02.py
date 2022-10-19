from sqlalchemy import create_engine
import pandas as pd
db_connerction_str = 'mysql+pymysql://scott:tiger@172.16.12.101/hr?charset=utf8mb4'
db_connerction = create_engine(db_connerction_str)
conn = db_connerction.connect()

sql = "select * from emp"

result = pd.read_sql_query(sql, conn)
print(pd.DataFrame(result))

conn.close()