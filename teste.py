import psycopg2

dbname = 'mybd'
user = 'pacer'
password = '123456'
host = 'localhost'

try:
    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
    cursor = conn.cursor()

    # SQL command for inserting data
    sql_insert = "INSERT INTO teste (column1) VALUES (%s)"
    data = (1,)  # Corrected data definition as a tuple
    cursor.execute(sql_insert, data)
    
    # Commit the transaction
    conn.commit()

    # SQL command for selecting data
    sql_select = "SELECT * FROM teste"
    cursor.execute(sql_select)

    # Fetch all the results
    result = cursor.fetchall()
    print("Results after insertion:", result)

    cursor.close()
    conn.close()

except Exception as e:
    print("DEU RUIM", e)
