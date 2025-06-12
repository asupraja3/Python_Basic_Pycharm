import mysql.connector as mysql
mydb = mysql.connect(host='localhost', user='root', password = '2508'
                     , database = 'sup')
mycursor = mydb.cursor()

mycursor.execute("select * from student")
result = mycursor.fetchall()
for i in result:
    print(i)