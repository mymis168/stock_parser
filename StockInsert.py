import pymssql
import random


"""
使用 pymssql 對資料庫進行連接
"""
server = "misdb01.database.windows.net"
database = "free-sql-db-6993718"
user = "dbeng"
password = "abc-12345"   
'''密碼洩漏問題'''

INS_SQL = """
    INSERT into dbo.stocks(sid,sname,price) 
    VALUES (
        %s,
        %s,
        %d
    )
"""
try:
    connect = pymssql.connect(server, user, password, database)
    cursor = connect.cursor()

    # 產生亂數 介於( 1850~ 1905)
    rp = random.randint(1850,1905)
    cursor.execute(INS_SQL, ("2330","TSMC",rp))
    # pymssql 預設設定 autocommit = false
    connect.commit()
    print("資料寫入完畢")
    cursor.close()
    connect.close()




except Exception as e: 
    print(f'連線失敗: 原因{e}')


