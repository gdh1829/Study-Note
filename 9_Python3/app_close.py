#!python

import pymysql as mysql

print("Application closing process gets started...")
APP_ID = input("Please enter target app id: ")
assert isinstance(APP_ID, int), "Number type is only allowed."
print("Inserted App Id is {APP_ID}")

SELECT_APP_SQL = "SELECT id, companyId, app_name, app_key, app_secret FROM application WHERE id = {APP_ID}"

UPDATE_APP_TABLE_SQL = "UPDATE application " \
    "SET app_secret = concat(app_secret, '_closed') " \
    "WHERE id = 1 AND app_key = 'key123' AND app_name = 'test_app';"

dbconn = getDBConnection()
runProcess(dbconn, SELECT_APP_SQL)

def getDBConnection():
    connection = mysql.connect(
        host='localhost',
        user='root',
        password='devko',
        db='PRC10000',
        charset='utf8'
    )
    return connection

def runProcess(db, query):
    cursor = db.cursor()
    try:
        db.begin()
        cursor.execute(query)
        app_info = checkQeuryResultForSelect(cursor)
        print(str(app_info))
        db.rollback()
    except Exception as e:
        print("[ERROR] %s" % str(e))
        db.rollback()

def checkQeuryResultForSelect(cursor):
    app_info = {}
    
    results = cursor.fetchall()
    if len(results) > 1 or len(results) == 0:
        raise UnexpectedTargetNumberExpection("Target application should be one.")
    
    for row in results:
        app_info["id"] = row[0]
        app_info["companyId"] = row[1]
        app_info["app_name"] = row[2]
        app_info["app_key"] = row[3]
        app_info["app_secret"] = row[4]
    
    return app_info


def checkDbExecutionForUpdateAndDelete(cursor):
    result = False
    affected_count = cursor.rowcount()
    # assert (affected_count != 1), "Failed to update."
    if affected_count != 1:
        raise AssertionError("Failed")
    return result

class UnexpectedTargetNumberExpection(Exception):
    pass

