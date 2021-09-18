# pip install pymysql
import pymysql
username=input("Enter your mysql user name: ")
pwd=input('Enter your mysql password: ')
mydb=pymysql.connect(
    host='localhost',
    user=username,
    passwd=pwd,
    database='students')

mycursor=mydb.cursor()
addResultForm="insert into result values(%s,'%s','%s',%s)"

#FUNCTION TO ADD STUDENT RESULT
def addResult():
        num=input("Enter student number : ")
        while len(num)!=4 or num.isnumeric()==False:
                num=input("Enter a valid 4 digit student roll number : ")
        numlist=[]
        mycursor.execute('select snum from result')
        for x in mycursor:
                numlist+=x
                while int(num) in numlist:
                        num=input('Student roll number already exists in database. Enter another valid number : ')
        snum=int(num)
        name=input("Enter student name : ")

        stream=input("Enter student stream : ")
        while stream not in ['SCIENCE','HUMANITIES','science','ARTS','COMMERCE','Science','humanities','commerce','arts','Humanities','Arts','Commerce']:
                stream=input("Enter a valid stream (Commerce,Humanities,Science)")
             
        marks_average=float(input("Enter avg marks : "))
        while marks_average<0 or marks_average>100:
                marks_average=float(input("Enter valid average marks : "))
                
        student=(snum,name,stream,marks_average)
        mycursor.execute(addResultForm %student)
        mydb.commit()
        print('Student details successfully added.')
        print('**********************************')

#FUNCTION TO UPDATE STUDENT RESULT       
def updateResult():
        con=pymysql.connect(host='localhost',user='root',password='',database='students')
        cur=con.cursor()
        snum = int(input("Enter 4 digit valid student number which you want to update : "))
        name = input("Enter student name : ")
        stream = input("Enter stream : ")
        marks_average = float(input("Enter marks average : "))
        
        args=(name,stream,marks_average,snum)
        qur='update result set name=%s, stream=%s, marks_average=%s where snum=%s'
        cur.execute(qur,args)
        con.commit()
        print('\n\t\tData Updated')
        con.close()

#FUNCTION TO DELETE STUDENT RESULT    
def deleteResult():
        con=pymysql.connect(host='localhost',user='root',password='',database='students')
        cur=con.cursor()
        snum = int(input('Enter 4 digit valid student number you want delete of : '))
        args=(snum)
        qur='Delete from result where snum=%s'
        cur.execute(qur,args)
        con.commit()
        print('\n\t\tData Deleted')
        con.close()

#FUNCTION TO GET STUDENT RESULT
getResultForm="select * from result where snum=%s"
def getResult():
        num=input('Enter student number you want result of : ')
        while len(num)!=4 or num.isnumeric()==False:
                num=input("Enter a valid 4 digit student number : ")
        if len(num)==4:
                numlist=[]
                mycursor.execute('select snum from result')
                for x in mycursor:
                        numlist+=x
                if len(numlist)==0:
                        print("There are no result entries in the database.")
                        print("**********************************")        
                else:
                        while int(num) not in numlist:
                                num=input('Student result does not exist in database. Enter another valid number : ')
                        snum=int(num)
                        mycursor.execute(getResultForm %snum)
                        row=mycursor.fetchone()
                        snum=row[0]
                        name = row[1]
                        stream=row[2]
                        marks_average=row[3]
                        print("Student roll:",snum)
                        print("Student name:",name)
                        print("Student's stream: ",stream)
                        print("Student's average marks: ",marks_average)
                        print('**********************************')

#FUNCTION TO ADD STUDENT CONTACT INFO:
addContactForm="insert into contactinfo values(%s,'%s','%s','%s',%s,%s,'%s')"
def addContact():
        num=input("Enter student number : ")
        while len(num)!=4 or num.isnumeric()==False:
                num=input("Enter a valid 4 digit student number : ")
        numlist=[]
        mycursor.execute('select snum from contactinfo')
        for x in mycursor:
                numlist+=x
                while int(num) in numlist:
                        while len(num)!=4 or num.isnumeric()==False:
                                num=input('Student number already exists in database. Enter another valid number')
        snum=int(num)
        name=input("Enter student's name : ")
        father_name=input("Enter Student's Father's name : ")
        mother_name=input("Enter Student's Mother's name : ")
        contact1=int(input("Enter primary contact number : "))
        contact2=int(input("Enter secondary contact number : "))
        address=input("Enter student's address : ")

                  
        student=(snum,name,father_name,mother_name,contact1,contact2,address)
        mycursor.execute(addContactForm %student)
        mydb.commit()
        print('\nStudent details successfully added.')
        print('**********************************')

#FUNCTION TO GET STUDENT CONTACT INFO
getContactForm="select * from contactinfo where snum=%s"
def getContact():
        num=input('Enter student number you want contact information of : ')
        while len(num)!=4 or num.isnumeric()==False:
                num=input("Enter a valid 4 digit student number : ")
        if len(num)==4:
                numlist=[]
                mycursor.execute('select snum from contactinfo')
                for x in mycursor:
                        numlist+=x
                if len(numlist)==0:
                        print("There are no contact information entries in the database.")
                        print("**********************************")        
                else:
                        while int(num) not in numlist:
                                num=input('Student contact information does not exist in database. Enter another valid 4 digit roll number : ')
                        snum=int(num)
                        mycursor.execute(getContactForm %snum)
                        row=mycursor.fetchone()
                        snum=row[0]
                        name=row[1]
                        father_name=row[2]
                        mother_name=row[3]
                        contact1=row[4]
                        contact2=row[5]
                        address=row[6]
                        print("Student's roll:",snum)
                        print("Student's name: ",name)
                        print("Student's father's name : ",father_name)
                        print("Student's mother's name: ",mother_name)
                        print("Primary contact number: ",contact1)
                        print("Secondary contact number: ",contact2)
                        print("Student's address: ",address)
                        print('**********************************')

#FUNCTION TO DELETE STUDENT CONTACT INFO
def deleteContact():
        con=pymysql.connect(host='localhost',user='root',password='',database='students')
        cur=con.cursor()
        snum = int(input('Enter valid 4 digit student number you want delete of : '))
        args=(snum)
        qur='Delete from contactinfo where snum=%s'
        cur.execute(qur,args)
        con.commit()
        print('\n\t\tData Deleted')
        con.close()
                       
while True:
        print("\n\nWhat do you want to do?")
        print("\n\n1. Add a student's result")
        print("2. Get a student's result")
        print("3. Add a student's contact info")
        print("4. Get a student's contact info")
        print("5. Update student's result info ")
        print("6. Delete student's result info ")
        print("7. Delete student's contact info ")
        print("8. Exit")
        
        x=input("\n\nEnter the number related to your choice: ")
        if x=='1':
                addResult()
        elif x=='2':
                getResult()
        elif x=='3':
                addContact()
        elif x=='4':
                getContact()
        elif x=='5':
                updateResult()
        elif x=='6':
                deleteResult()
        elif x=='7':
                deleteContact()
        else:
                break
       

        #         #FUNCTION TO DELETE DATA
        #         con=pymysql.connect(host='localhost',user='root',password=' ')
        #         cur=con.cursor()
        #         args=(name)
        #         qur='Delete from student where name=%s'
        #         cur.execute(qur,args)
        #         con.commit()
        #         print('Data deleted')
        #         con.close()
                

                                
            
