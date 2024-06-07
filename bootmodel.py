
import mysql.connector

def opslaan(bootnaam, lengte):
    print("hij doet het")
    mydb = mysql.connector.connect(
    host="felixdemoycolfield.mysql.database.azure.com",  #port erbij indien mac
    user="felixadmin",
    password="abcd1234ABCD!@#$",
    database="bootdatabaseonline"
    )

    mycursor = mydb.cursor()

    sql = "INSERT INTO boot (naam, lengte) VALUES (%s, %s)"
    val = (bootnaam, lengte)
    mycursor.execute(sql, val)
    mydb.commit()

def allebotenopvragen():
    import mysql.connector

    mydb = mysql.connector.connect(
    host="felixdemoycolfield.mysql.database.azure.com",  #port erbij indien mac
    user="felixadmin",
    password="abcd1234ABCD!@#$",
    database="bootdatabaseonline"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM boot")

    myresult = mycursor.fetchall()

    keys = [i[0] for i in mycursor.description]

    data = [
        dict(zip(keys, row)) for row in myresult
    ]
    return data

