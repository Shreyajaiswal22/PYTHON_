##!/usr/bin/python3
#import pymysql
## Open database connection
#db = pymysql.connect("127.0.0.1","root","","testdb")
## prepare a cursor object using cursor() method
#cursor = db.cursor()
## execute SQL query using execute() method.
#cursor.execute("SELECT VERSION()")
## Fetch a single row using fetchone() method.
#data = cursor.fetchone()
#print ("Database version : %s " % data)
## disconnect from server
#db.close()
 


##CREATE DATABASE TABLE
## Open database connection
#import pymysql
#db = pymysql.connect("localhost","root","","testdb" )
## prepare a cursor object using cursor() method
#cursor = db.cursor()
## Drop table if it already exist using execute() method.
#cursor.execute("DROP TABLE IF EXISTS EMPLOYEE") 
## Create table as per requirement
#sql = """CREATE TABLE EMPLOYEE (
#FIRST_NAME CHAR(20) NOT NULL,
#LAST_NAME CHAR(20),
#AGE INT,
#SEX CHAR(1),
#INCOME FLOAT )"""
#cursor.execute(sql)
## disconnect from server
#db.close()



###!/usr/bin/python3
#import pymysql
## Open database connection
#db = pymysql.connect("localhost","root","","testdb")
### prepare a cursor object using cursor() method
#cursor = db.cursor()
### Prepare SQL query to INSERT a record into the database.
#sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
#LAST_NAME, AGE, SEX, INCOME)
#VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
#try:
### Execute the SQL command
#    cursor.execute(sql)
### Commit your changes in the database
#    db.commit()
#except:
### Rollback in case there is any error
#    db.rollback()
### disconnect from server
#db.close()



#
###UPDATE QUERY
###!/usr/bin/python3
#import pymysql
## Open database connection
#db = pymysql.connect("localhost","root","","testdb" )
## prepare a cursor object using cursor() method
#cursor = db.cursor()
## Prepare SQL query to UPDATE required records
#sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
#try:
## Execute the SQL command
#    cursor.execute(sql)
## Commit your changes in the database
#    db.commit()
#except:
## Rollback in case there is any error
#    db.rollback()
## disconnect from server
#db.close()


##READ QUERY
##!/usr/bin/python3
#import pymysql
## Open database connection
#db = pymysql.connect("localhost","root","","pubg" )
## prepare a cursor object using cursor() method
#cursor = db.cursor()
## Prepare SQL query to INSERT a record into the database.
#sql = "SELECT * FROM EMPLOYEE \
#WHERE AGE = '%d'"%(21)
##WHERE INCOME > '%d'" % (1000)
#try:
## Execute the SQL command
#    cursor.execute(sql)
## Fetch all the rows in a list of lists.
#    results = cursor.fetchall()
##    print(type(results))
#    for row in results:
#        fname = row[0]
#        lname = row[1]
#        age = row[2]
#        sex = row[3]
#        income = row[4]
## Now print fetched result
#    print ("fname=%s,lname=%s,age=%d,sex=%s,income=%d" % 
#           (fname, lname, age, sex, income ))
#except:
#    print ("Error: unable to fetch data")
## disconnect from server
#db.close()


##DELETE QUERY
##!/usr/bin/python3
#import pymysql
## Open database connection
#db = pymysql.connect("127.0.0.1","root","","testdb")
## prepare a cursor object using cursor() method
#cursor = db.cursor()
## Prepare SQL query to DELETE required records
#sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (21)
#try:
## Execute the SQL command
#    cursor.execute(sql)
## Commit your changes in the database
#    db.commit()
#except:
## Rollback in case there is any error
#    db.rollback()
## disconnect from server
#db.close()
















