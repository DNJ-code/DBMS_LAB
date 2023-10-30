import mysql.connector
conn = mysql.connector.connect(host='localhost', password='Adi@3845', user='root')
mycursor=conn.cursor()
mycursor.execute('insert dj_1.exam values(201,"2023-11-10","09:00","Exam Hall A");')
mycursor.execute('insert dj_1.exam values(202,"2023-11-12","02:00","Exam Hall B");')
mycursor.execute('insert dj_1.exam values(203,"2023-11-15","10:30","Exam Hall C");')
mycursor.execute('insert dj_1.exam values(204,"2023-11-18","03:15","Exam Hall D");')
mycursor.execute('insert dj_1.exam values(205,"2023-11-20","01:00","Exam Hall E");')
conn.commit()
conn.close()



