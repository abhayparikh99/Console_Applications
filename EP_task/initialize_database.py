import pymysql

username=input("Enter your mysql user name: ")
pwd=input('Enter your mysql password: ')
mydb=pymysql.connect(
    host='localhost',
    user=username,
    passwd=pwd)
mycursor=mydb.cursor()
mycursor.execute("create database Students")
mydb.commit()
mydb=pymysql.connect(
    host='localhost',
    user=username,
    passwd=pwd,
    database='students')
mycursor=mydb.cursor()
mycursor.execute("create table result (snum int(4) primary key, name varchar(25), stream varchar(12), marks_average decimal(4,2))")
mydb.commit()
mycursor.execute("create table contactinfo (snum int(4) primary key not null, name varchar(25), father_name varchar(25), mother_name varchar(25), contact1 bigint, contact2 bigint, address varchar(60))")
mydb.commit()

