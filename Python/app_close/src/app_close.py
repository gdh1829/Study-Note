#!/usr/bin/python

# This script is based on python v2.7.15
# Purpose: to automate manual process of closing application.

# Native modules
import sys
import logging
import json
import argparse

# Nonnative modules
import mysql.connector

# Name space
connection_config = {
    'user' : 'xxxx',
    'password' : 'xxxx',
    'host' : 'xxxx',
    'database' : 'xxxx',
    'port' : 3306,
    'raise_on_warnings': True,
    'connection_timeout' : 5,
    'pool_size': 6
}
conn = None
cur = None
args = None
app = None
users = None

# Script Parameters
parser = argparse.ArgumentParser(description = 'Process application close')
parser.add_argument('--appId', '-id', help = 'Application ID', type = int, required=True)
args = parser.parse_args()

# Query space
SELECT_APP_QUERY = '''SELECT id, app_name, company_id, app_key, app_secret 
                    FROM application 
                    WHERE id = %s'''
SELECT_USER_QUERY = '''SELECT u.id, a.id as user_authenticated_id, u.company_id, u.company_user_id 
                    FROM user u
                    LEFT OUTER JOIN user_authenticated a on u.id = a.user_id 
                    WHERE u.app_id = %s 
                    ORDER BY u.company_id ASC'''
UPDATE_APP_QUERY = '''UPDATE application 
                    SET app_secret = concat(app_secret, "_stopped") 
                    WHERE id = %s AND app_name = %s'''
DELETE_AUTHORIZED_USER_QUERY = '''DELETE FROM user_authenticated 
                                WHERE id = %s AND user_id = %s AND app_id = %s'''
DELETE_USER_QUERY = '''DELETE FROM user
                    WHERE id = %s AND company_id = %s AND company_user_id = %s'''
SELECT_DB_INFO_QUERY = '''SELECT partition_id, db_id 
                        FROM db_info 
                        WHERE partition_id = %s'''
UPDATE_AGENT_ENDDATE_QUERY = '''UPDATE agents 
                                SET end_date = now() 
                                WHERE id = %s AND name = %s'''

# Function space
def getDbConnection(connection_config):
    try:
        connection = mysql.connector.connect(**connection_config)
        if connection.is_connected():
            print('MYSQL is successfully connected. MySQL server version on v' + connection.get_server_info())
            return connection
        else:
            print('MySQL is not connected.')
            sys.exit(0) 
    except mysql.connector.Error as e:
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
        print('''   COMPANY_ID: %s, COMPANY_USER_ID: %s, OAUTH_USER_ID: %s, OAUTH_AUTHORIZED_USER_ID: %s '''
        % (user['company_id'],user['company_user_id'] , user['id'], user['user_authenticated_id']))

def execute(cursor, query, values, isSelect=False):
    try:
        cur.execute(query, values)
        if isSelect:
            if cur.rowcount == 0:
                print("Nothing found with the select query")
                exit(0)
            else:
                return cur.fetchall()
        else:
            if cur.rowcount != 1:
                print('Affected rows is more than 1. Affected Rows are %s. Rollback' % cur.rowcount)
                conn.rollback()
                exit(0)
    except mysql.connector.Error as e:
        conn.rollback()
        cur.close()
        conn.close()
        print("Failed to execute query(%s)" % query)
        print(e)
        exit(1)

def commit(conn):
    try:
        conn.commit()
    except mysql.connector.Error as e:
        print("Failed to commit. " + e)
        conn.rollback()
        cur.close()
        conn.close()
        exit(1)

def isYes():
    answer = raw_input('''
Check above. Keep processing?[Y/n]''')
    return (answer is 'Y' or answer is 'y')


# Preparing excution info to display on terminal
conn = getDbConnection(connection_config)
cur = conn.cursor(buffered = True, dictionary = True)

app = execute(cur, SELECT_APP_QUERY, (args.appId,), True)[0]
printApp(app['id'], app['app_name'], app['company_id'])

users = execute(cur, SELECT_USER_QUERY, (app['id'], ), True)
printAppUsers(users)

if isYes() == False:
    print('exit.')
    exit(0)

# Process starts
print('Updating application data...')
execute(cur, UPDATE_APP_QUERY, (app['id'], app['app_name'], ))
print('OK')

print('Deleteing user authentication data...')
for user in users:
    if user['user_authenticated_id'] == None:
        continue
    execute(cur, DELETE_AUTHORIZED_USER_QUERY, (user['user_authenticated_id'], user['id'], app['id'], ))
print('OK')

print('Deleteing user data...')
for user in users:
    execute(cur, DELETE_USER_QUERY, (user['id'], user['company_id'], user['company_user_id'], ))
print('OK')

commit(conn)
print('Office Operation is done. Committed.')

# Closing Connection to step on to the next databases
cur.close()
conn.close()

# Update agents
for user in users:
    # searching for partition info and preparing database config
    # db_info = execute(cur, SELECT_DB_INFO_QUERY, (user['company_id'], ), True)[0]
    print('Moving to PRC%s and deleting data...' % user["company_id"])
    connection_config['database'] = 'PRC%s' % user["company_id"]
    connection_config['port'] = 3307

    # Process starts
    conn = getDbConnection(connection_config)
    cur = conn.cursor(buffered = True, dictionary = True)
    execute(cur, UPDATE_AGENT_ENDDATE_QUERY , (user['company_user_id'], app['app_name'], ))
    commit(conn)
    cur.close()
    conn.close()
    print('OK. Committed.')

print('[SUCCESS] All of the operations has been finished. Thanks.')