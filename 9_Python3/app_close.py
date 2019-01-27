#!/usr/bin/python3

# Native modules
import sys
import logging
import json

# Nonnative modules
import pymysql

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
DB = 'office'
USER = 'root'
PASSWORD = 'rootpass'
CONN_TIMEOUT = 5
conn = None
APP = None
authorized_user_params = []
user_params = []

# query space
SELECT_APP_QUERY = "SELECT id, company_id, app_name, app_key, app_secret \
                    FROM application \
                    WHERE id = %s"
SELECT_AUTHORIZED_USER_QUERY = "SELECT ua.id, ua.user_id, ua.app_id, u.company_id, u.company_user_id \
                    FROM user_authenticated ua \
                    INNER JOIN user u ON ua.user_id = u.id \
                    WHERE ua.app_id = %s \
                    ORDER BY u.company_id ASC"
UPDATE_APP_QUERY = "UPDATE application \
                    SET app_secret = concat(app_secret, '_deceased_0829') \
                    WHERE id = %s AND app_key = %s AND app_name = %s"
DELETE_AUTHORIZED_USER_QUERY = 'DELETE FROM user_authenticated where id = %s AND user_id = %s AND app_id = %s'
DELETE_USER_QUERY = 'DELETE FROM user where id = %s AND company_user_id = %s AND app_id = %s'


APP_ID = input("Please enter target app id: ")
assert isinstance(int(APP_ID), int), "Only number type is allowed."
print(f'Inserted App Id is {APP_ID}')

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
                cursorclass=pymysql.cursors.DictCursor,
                autocommit=False
            )
        else:
            logging.info("Connection is exited. Skipping connection")
    except:
        logging.error("Failed to open db connection.")
        sys.exit(1)

print("Application closing process gets started...")


def isYesFromUser():
    answer = input('Keep processing?[Y/n]')
    return (answer is 'Y' or answer is 'y')

def selectRecords(query, param):
    try:
        # create cursor
        with conn.cursor() as cur:
            cur.execute(query, param)
            logging.info(f'Next Query is excuted: {query}')
            rows = cur.fetchall()
            # print(rows)
            return rows
    except Exception as e:
        logging.error(e)

# create connection
getDbConnection(HOST, PORT, DB, USER, PASSWORD)

# 
selectedAppList = selectRecords(SELECT_APP_QUERY, [APP_ID])
if(selectedAppList is None or not selectedAppList):
    print(f"{APP_ID} is not existed. Exit the process.")
    sys.exit(1)
if(len(selectedAppList) >= 2):
    print(f"DATAERROR: Target APP({APP_ID}) is existed more than 1")
    sys.exit(1)

# APP = json.loads(selectedAppList[0])
APP = selectedAppList[0]
print(f'''
==========<APP CLOSE PROCESSING>===========
APP_ID        : {APP['id']}
APP_COMPANY_ID: {APP['company_id']}
APP_NAME      : {APP['app_name']}
APP_KEY       : {APP['app_key']}
===============<CHECK ABOVE>================
        ''')

if(not isYesFromUser()):
    print('Process stops.')
    sys.exit(0)
#

print(f'Checking subscribing users for the app({APP_ID})...')
authenticated_user_list = selectRecords(SELECT_AUTHORIZED_USER_QUERY, [APP_ID])

companyId_set = set()
for user in authenticated_user_list:
    companyId_set.add(user['company_id'])

if(len(companyId_set) > 1):
    print(f'More than 1 company is subscribing the app => company Ids: {companyId_set}')
    if(not isYesFromUser()):
        print('Process stops.')
        sys.exit(0)

print('-----------------Process starts--------------------')


def updateQuery(query, param):
    try:
        with conn.cursor() as cur:
            affectedRowsNumber = cur.execute(query, param)
            if(affectedRowsNumber is 0):
                raise Exception("Failed to update target app_secret")
            if(affectedRowsNumber > 1):
                raise Exception("Affected more than 1 app record. It should be only one")
            cur.execute(SELECT_APP_QUERY, APP["id"])
            rows = cur.fetchall()
            print(f"[SUCCESS] app_secret is updated.: {rows}")
            conn.rollback()
    except Exception as e:
        logging.error(e)
        conn.rollback()

def prepareDelAuthorizedUserParams():
    for auth_user in authenticated_user_list:
        authorized_user_params.append([auth_user["id"], auth_user["user_id"], APP["id"]])

def prepareDelUserParams():
    for auth_user in authenticated_user_list:
        user_params.append([auth_user["user_id"], auth_user["company_user_id"], APP["id"]])

def deleteQueries(query, params = None):
    print(params)
    try:
        with conn.cursor() as cur:
            affectedRowsNumber = cur.executemany(query, params)
            print(affectedRowsNumber)
            cur.execute(SELECT_AUTHORIZED_USER_QUERY, [APP["id"]])
            if(cur.fetchall() is 0):
                print("[SUCCESS] subscribing users are deleted.")
            conn.rollback()
    except Exception as e:
        logging.error(e)
        conn.rollback()

# Update
updateQuery(UPDATE_APP_QUERY, [APP["id"], APP["app_key"], APP["app_name"]])
prepareDelAuthorizedUserParams()
prepareDelUserParams()
deleteQueries(DELETE_AUTHORIZED_USER_QUERY, authorized_user_params)
deleteQueries(DELETE_USER_QUERY, user_params)









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