from multiprocessing import current_process
import sqlite3

#conectar y crear db alumnos
conn = sqlite3.connect('alumnos.db')
#crear cursor
cursor = conn.cursor()
##crear tabla
cursor.execute("CREATE TABLE Alumnos(Id INT, Nombre TEXT, Apellido TEXT)")

cursor.execute("INSERT INTO Alumnos VALUES(1,'Federico' , 'Acevedo')")
cursor.execute("INSERT INTO Alumnos VALUES(2,'Juan' , 'Garcia')")
cursor.execute("INSERT INTO Alumnos VALUES(3,'Myriam' , 'Zanahoria')")
cursor.execute("INSERT INTO Alumnos VALUES(4,'Pepe' , 'Lui')")
cursor.execute("INSERT INTO Alumnos VALUES(5,'Miranda' , 'Roca')")
cursor.execute("INSERT INTO Alumnos VALUES(6,'Carlos' , 'Acevedo')")
cursor.execute("INSERT INTO Alumnos VALUES(7,'Marysol' , 'Haedo')")
cursor.execute("INSERT INTO Alumnos VALUES(8,'Greg' , 'Fortinite')")

conn.commit()

cursor.execute("SELECT * FROM Alumnos WHERE Nombre='Pepe'")

rows = cursor.fetchall()

print(rows)

conn.close()

    

