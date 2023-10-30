import mysql.connector
conn = mysql.connector.connect(host='localhost', password='Adi@3845', user='root')
mycursor=conn.cursor()
'''for i in range(8):
    print("enter data in row", i+1)
    courseid=int(input("Enter student id "))
    coursename=(input("enter name "))
    credits= int(input("Credits "))
    mycursor.execute('insert dj_1.course values(courseID,courseName,Credits;')'''
mycursor.execute('insert dj_1.course values(101,"maths","3");')
mycursor.execute('insert dj_1.course values(102,"History","4");')
mycursor.execute('insert dj_1.course values(103,"Computer Science","3");')
mycursor.execute('insert dj_1.course values(104,"Literature","3");')
mycursor.execute('insert dj_1.course values(105,"chemistry","4");')
mycursor.execute('insert dj_1.course values(106,"Physics","4");')
mycursor.execute('insert dj_1.course values(107,"Economics","3");')
mycursor.execute('insert dj_1.course values(108,"Biology","4");')
conn.commit()
conn.close()