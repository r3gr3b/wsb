# import MySQLdb

# db = MySQLdb.connect(host="127.0.0.1",
#                        user="root",
#                        passwd="Inaner99")

# cursor = db.cursor()
# cursor.execute("SET sql_notes = 0; ")
# cursor.execute("create database if NOT EXISTS test_db")


# cursor.execute("USE test_db")

# # not sure what this does
# cursor.execute("SET sql_notes = 0; ")

# cursor.execute("create table IF NOT EXISTS test (url mediumtext);")
# cursor.execute("SET sql_notes = 1; ")


# cursor.execute("insert into test (email,pwd) values('test@gmail.com', 'test')")

# db.commit()


# db.close()


# add_entry = ("INSERT INTO *tablename* "
#                "(first_name, last_name, hire_date, gender, birth_date) "
#                "VALUES (%s, %s, %s, %s, %s)"

print('import worked')