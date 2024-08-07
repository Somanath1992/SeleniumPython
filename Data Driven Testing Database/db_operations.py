# insert, update, delete
import mysql.connector

insert_query = "insert into student values(104,'tom');"
update_query = "update student set sname='Marry' where sid=103"
delete_query = "delete from student where sid=101"

# If any case db is down, or it has any error, we can handle it using try except block
try:
    connc = mysql.connector.connect(host="localhost", port="3306", username="root", password="9423", database="sakila")
    curs = connc.cursor()
    curs.execute(insert_query)
    curs.execute(update_query)
    curs.execute(delete_query)
    connc.commit()
    connc.close()
    print("query executed successfully")
except:
    print("Connection Unsuccessful")
