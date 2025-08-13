import mysql.connector

# 1. Conexión
conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="tu_password",
    database="escuela"
)
cursor = conn.cursor()

# 2. Crear tabla
cursor.execute("""
CREATE TABLE IF NOT EXISTS estudiantes (
    id INT PRIMARY KEY,
    nombre VARCHAR(50),
    edad INT,
    curso VARCHAR(50)
)
""")

# 3. Insertar datos
cursor.executemany("""
INSERT INTO estudiantes (id, nombre, edad, curso)
VALUES (%s, %s, %s, %s)
""", [
    (1, 'Ana', 20, 'Matemáticas'),
    (2, 'Juan', 22, 'Historia'),
    (3, 'Maria', 21, 'Física')
])

# # 4. Consultar
# cursor.execute("SELECT * FROM estudiantes")
# for fila in cursor.fetchall():
#     print(fila)

# # 5. Actualizar y eliminar
# cursor.execute("UPDATE estudiantes SET curso = 'Literatura' WHERE nombre = 'Juan'")
# cursor.execute("DELETE FROM estudiantes WHERE id = 3")

# # 6. Funciones agregadas
# cursor.execute("SELECT COUNT(*) FROM estudiantes")
# print("Cantidad:", cursor.fetchone()[0])

# cursor.execute("SELECT AVG(edad) FROM estudiantes")
# print("Edad promedio:", cursor.fetchone()[0])

# 7. Confirmar cambios y cerrar
conn.commit()
conn.close()
