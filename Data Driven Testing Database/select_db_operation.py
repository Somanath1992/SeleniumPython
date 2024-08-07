import mysql.connector

# If any case db is down, or it has any error, we can handle it using try except block
try:
    connc = mysql.connector.connect(host="localhost", port="3306", username="root", password="9423", database="sakila")
    curs = connc.cursor()
    curs.execute("select * from actor")
    # To print records from the table
    for row in curs:
        print(row[0], row[1], row[2], row[3])
    connc.close()
    print("query executed successfully")
except:
    print("Connection Unsuccessful")
