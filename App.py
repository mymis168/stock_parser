import pymssql

"""
使用 pymssql 對資料庫進行連接
"""
server = "misdb01.database.windows.net"
database = "free-sql-db-6993718"
user = "dbeng"
password = "abc-12345"   
'''密碼洩漏問題'''




connect = pymssql.connect(server, user, password, database)
print("db登入成功")


