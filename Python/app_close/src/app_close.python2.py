#!/usr/bin/python

# Native modules
import sys
import logging
import json
import argparse

# Nonnative modules
import mysql.connector
from mysql.connector import Error

# name space
connection_config_dict = {
    'user' : 'xxxx',
    'password' : 'xxxx',
    'host' : '127.0.0.1',
    'database' : 'office',
    'port' : 3306,
    'raise_on_warnings': True,
    'connection_timeout' : 5,
    'pool_size': 5
}
conn = None
args = None
app = None
users = None

parser = argparse.ArgumentParser(description = 'Process application close')
parser.add_argument('--appId', '-id', help = 'Application ID', type = int, required=True)
args = parser.parse_args()

# query space
SELECT_APP_QUERY = 'SELECT id, app_name, company_id, app_key, app_secret \
                    FROM application \
                    WHERE id = %s'
SELECT_USER_QUERY = 'SELECT id, user_authenticated_id, company_id, company_user_id \
                    FROM user \
                    WHERE app_id = %s \
                    ORDER BY company_id ASC' 
UPDATE_APP_QUERY = 'UPDATE application \
                    SET app_secret = concat(app_secret, \'_deceased_0829\') \
                    WHERE id = %s AND app_name = %s'
DELETE_AUTHORIZED_USER_QUERY = 'DELETE FROM user_authenticated \
                                WHERE id = %s AND user_id = %s AND app_id = %s'
DELETE_USER_QUERY = 'DELETE FROM user \
                    WHERE id = %s AND company_id = %s AND user_id = %s'

# MySQL Connection
def getDbConnection(connection_config_dict):
    try:
        connection = mysql.connector.connect(**connection_config_dict)
        if connection.is_connected():
            print('MYSQL is successfully connected. MySQL server version on v' + connection.get_server_info())
            return connection
        else:
            print('MySQL is not connected.')
            sys.exit(0) 
    except Error as e:
        print('Failed to open db connection.', e)
        sys.exit(1)


def printApp(appId, appName, companyId):
    print('''
    ======< TARGET APP TO BE CLOSED >======
    APP_ID        : %s
    APP_NAME      : %s
    APP_COMPANY_ID: %s ''' % (appId, appName, companyId, ))

def printAppUsers(Users):
    print('''   ==========< USERS CONNECTED TO APP >========''')
    if users == None or len(users) == 0:
        print('No User Data connected to the app')

    for user in Users:
        print('''   COMPANY_ID: %s, USER_ID: %s, AUTHENTICATED_USER_ID: %s '''
        % (user['company_id'], user['id'], user['user_authenticated_id']))

def isYes():
    answer = raw_input('''
Check above. Keep processing?[Y/n]''')
    return (answer is 'Y' or answer is 'y')
    

conn = getDbConnection(connection_config_dict)
# create connection
cur = conn.cursor(buffered = True, dictionary = True)
cur.execute(SELECT_APP_QUERY, (args.appId,))
records = cur.fetchall()

if cur.rowcount != 1:
    print('Nothing found or More than two rows found. Something\'s wrong. Please check them out manually')
    exit(0)

app = records[0]

printApp(app['id'], app['app_name'], app['company_id'])

cur.execute(SELECT_USER_QUERY, (app['id'], ))
users = cur.fetchall()
printAppUsers(users)

if isYes() == False:
    print('exit.')
    exit(0)

print('Updating application data...')
cur.execute(UPDATE_APP_QUERY, (app['id'], app['app_name'], ))
if cur.rowcount != 1:
    print('Updated application record is not single record. Rollback')
    conn.rollback()
    exit(0)
print('OK')

print('Deleteing user authentication data...')
for user in users:
    cnt = 0
    if user['user_authenticated_id'] == None:
        cnt += 1
        continue
    cur.execute(DELETE_AUTHORIZED_USER_QUERY, (user['user_authenticated_id'], user['id'], app['id'], ))
    if cur.rowcount != (len(users) - cnt):
        print('Deleted record counts(%s) are not equal to expected numbers to be deleted(%s). Rollback' % (cur.rowcount, (len(users) - cnt), ))
        conn.rollback()
        exit(0)
print('OK')

print('Deleteing user data...')
for user in users:
    cur.execute(DELETE_USER_QUERY, (user['id'], user['company_id'], user['company_user_id'], ))
    if cur.rowcount != len(users):
        print('Deleted userrecord counts(%s) are not equal to expected numbers to be deleted(%s). Rollback' % (cur.rowcount, len(users), ))
        conn.rollback()
        exit(0)
print('OK')