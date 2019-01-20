#!/usr/bin/python3

import sys
import pymysql
import logging
# import mysql.connector
# from mysql.connector import Error
# from mysql.connector import pooling

# try:
#     connection_pool = mysql.connector.pooling.MySQLConnectionPool(
#         pool_name = "pynative_pool", #automatically created, if nothing
#         pool_size = 5, #default is 5, if nothing
#         pool_reset_session=True,
#         host='localhost',
#         database='PRC10000',
#         user='root',
#         password='devko',
#         charset='utf8'
#     )

# name space
HOST = '127.0.0.1'
PORT = 3306
DB = 'PRC10000'
USER = 'root'
PASSWORD = 'rootpass'
CONN_TIMEOUT = 5
conn = None

# MySQL Connection
def getDbConnection(HOST, PORT, DB, USER, PASSWORD):
    global conn
    try:
        if(conn is None):
            conn = pymysql.connect(
                host=HOST, 
                port=PORT, 
                db=DB, 
                user=USER,
                password=PASSWORD,
                charset='utf8mb4',
                connect_timeout=CONN_TIMEOUT,
                cursorclass=pymysql.cursors.DictCursor
            )
        else:
            logging.info("Connection is exited. Skipping connection")
    except:
        logging.error("Failed to open db connection.")
        sys.exit(1)

print("Application closing process gets started...")

APP_ID = input("Please enter target app id: ")
assert isinstance(int(APP_ID), int), "Only number type is allowed."
print(f'Inserted App Id is {APP_ID}')

SELECT_APP_SQL = f"SELECT a.id, a.app_name, u.id as user_authenticated_id \
                    FROM application a \
                    INNER JOIN user_authenticated u ON a.id = u.app_id \
                    WHERE a.id = {APP_ID}"

def selectRecords(query):
    try:
        # create connection
        getDbConnection(HOST, PORT, DB, USER, PASSWORD)
        # create cursor
        with conn.cursor() as cur:
            cur.execute(query)
            rows = cur.fetchall()
            for row in rows:
                print(row)
    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()

selectRecords(SELECT_APP_SQL)




# UPDATE_APP_TABLE_SQL = "UPDATE application " \
#     "SET app_secret = concat(app_secret, '_closed') " \
#     "WHERE id = 1 AND app_key = 'key123' AND app_name = 'test_app';"

# dbconn = getDBConnection()
# runProcess(dbconn, SELECT_APP_SQL)

# 


# def checkQeuryResultForSelect(cursor):
#     app_info = {}
    
#     results = cursor.fetchall()
#     if len(results) > 1 or len(results) == 0:
#         raise UnexpectedTargetNumberExpection("Target application should be one.")
    
#     for row in results:
#         app_info["id"] = row[0]
#         app_info["companyId"] = row[1]
#         app_info["app_name"] = row[2]
#         app_info["app_key"] = row[3]
#         app_info["app_secret"] = row[4]
    
#     return app_info


# def checkDbExecutionForUpdateAndDelete(cursor):
#     result = False
#     affected_count = cursor.rowcount()
#     # assert (affected_count != 1), "Failed to update."
#     if affected_count != 1:
#         raise AssertionError("Failed")
#     return result

# class UnexpectedTargetNumberExpection(Exception):
#     pass

