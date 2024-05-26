import mysql.connector

db = mysql.connector.connect(
    host="localhost",         #NamaHostDatabase
    user="username",          #NamaUserDatabase 
    password="password",      #PasswordDatabase
    database="nama_database"  #NamaDatabaseYangAkanDiEksport
)

cursor = db.cursor()


query = "SELECT * FROM nama_tabel"  #TableYangAkanDieksport

cursor.execute(query)

data = cursor.fetchall()

with open("nama_file.csv", "w") as csvfile: 

    
    field_names = [field[0] for field in cursor.description]
    writer = csv.writer(csvfile)
    writer.writerow(field_names)

    for row in data:
        writer.writerow(row)

db.close()

print("Ekstraksi data ke CSV berhasil!")
