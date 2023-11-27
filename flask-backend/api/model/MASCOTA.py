import functools
import db
import pymysql

def get_MASCOTA():
    con = db.get_connection()
    cursor = con.cursor(pymysql.cursors.DictCursor)
    try:
        sql="SELECT * FROM MASCOTA"
        cursor.execute(sql)
        ret = cursor.fetchall()
        print(ret)
        return ret
    finally:
        con.close()

def get_mascotas(idMascota):
    con = db.get_connection() 
    cursor = con.cursor(pymysql.cursors.DictCursor)
    ret={}
    try:
        sql="SELECT * FROM MASCOTA WHERE idMASCOTA = {}".format(idMascota)
        cursor.execute(sql)
        ret = cursor.fetchone()
        return ret
    finally:
        con.close()

def create_mascota(Nombre_Mascota,Especie,Raza, Genero, Tipo_de_Sangre, Edad, Estado):
    con = db.get_connection()
    cursor = con.cursor()
    try:
        sql="INSERT INTO MASCOTA (Nombre_Mascota,Especie, Raza, Genero, Tipo_de_Sangre, Edad, Estado) VALUES('{}','{}', '{}','{}','{}','{}','{}')".format(Nombre_Mascota,Especie, Raza, Genero, Tipo_de_Sangre, Edad, Estado)
        print(sql)
        cursor.execute(sql)
        con.commit()
        id_org = cursor.lastrowid
        return {"message":"OK", "id": id_org}
    finally:
        con.close()

def update_mascota(Nombre_Mascota, Edad, Estado,idMascota):
    con = db.get_connection()
    cursor = con.cursor()
    try:
        sql="UPDATE MASCOTA set Nombre_Mascota='{0}', Edad='{1}',Estado='{2}'  WHERE idMASCOTA = {3}".format(Nombre_Mascota, Edad, Estado,idMascota)
        print(sql)
        cursor.execute(sql)
        con.commit()
        return {"message":"OK"}
    finally:
        con.close()

def delete_mascota(idMascota):
    con = db.get_connection()
    cursor = con.cursor()
    try:
        sql="DELETE FROM MASCOTA WHERE idMASCOTA = {}".format(idMascota)
        cursor.execute(sql)
        con.commit()
        return {"message":"OK"}
    finally:
        con.close()
