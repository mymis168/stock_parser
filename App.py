import pymssql

"""
使用 pymssql 對資料庫進行連接
"""
server = "misdb01.database.windows.net"
database = "free-sql-db-6993718"
user = "dbeng"
password = "abc-12345"   
'''密碼洩漏問題'''

"""
資料表建立 DDL:


CREATE TABLE [dbo].[stocks] (
    [Id]    INT             IDENTITY (1, 1) NOT NULL,
    [sid]   CHAR (4)        NOT NULL,
    [sname] VARBINARY (30)  NOT NULL,
    [price] DECIMAL (16, 2) NOT NULL,
    [pdate] DATETIME        CONSTRAINT [DEFAULT_stocks_pdate] DEFAULT GETDATE() NOT NULL,
    CONSTRAINT [PK_stocks] PRIMARY KEY CLUSTERED ([Id] ASC)
);

"""


# 1. 登入 azure sql server 成功後取得一個 Connection物件
connect = pymssql.connect(server, user, password, database)
print("db登入成功")

# 2. 透過該物件(Connection) 產生一個 Cursor物件負責執行 SQL 語法
cursor = connect.cursor()
print("cursor 取得成功")
# 3. 透過 cursor 將 sql 送給 azure sql server 執行
cursor.execute("select * from stocks")

# 4. 取得查詢結果 存入 records list[]中
records = cursor.fetchall()  

rec_count = len( records) #計算筆數

print(f'總共查詢到 {rec_count} 筆資料')

cursor.close()
connect.close()








