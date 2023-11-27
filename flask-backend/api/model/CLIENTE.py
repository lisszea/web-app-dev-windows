import functools
import db
import pymysql

def get_CLIENTE():
    con = db.get_connection()
    cursor = con.cursor(pymysql.cursors.DictCursor)
    try:
        sql="SELECT * FROM CLIENTE"
        cursor.execute(sql)
        ret = cursor.fetchall()
        print(ret)
        return ret
    finally:
        con.close()

def get_CLIENTES(CLIENTES_id):
    con = db.get_connection() 
    cursor = con.cursor(pymysql.cursors.DictCursor)
    ret={}
    try:
        sql="SELECT * FROM CLIENTE WHERE idCLiente = {}".format(CLIENTES_id)
        cursor.execute(sql)
        ret = cursor.fetchone()
        return ret
    finally:
        con.close()

def get_cliente_by_name(cliente_name):
    con = db.get_connection() 
    cursor = con.cursor(pymysql.cursors.DictCursor)
    ret={}
    try:
        sql="SELECT * FROM CLIENTE WHERE Nombre = '{}'".format(cliente_name)
        print(sql)
        cursor.execute(sql)
        ret = cursor.fetchone()
        return ret
    finally:
        con.close()

def create_cliente(idCliente,Nombre, Apellido,Telefono, Direccion, Nombre_Mascota):
    con = db.get_connection()
    cursor = con.cursor()
    try:
        sql="INSERT INTO CLIENTE (idCliente,Nombre, Apellido,Telefono, Direccion, Nombre_Mascota) VALUES('{}','{}','{}','{}','{}', '{}' )".format(idCliente,
        Nombre, Apellido,Telefono, Direccion, Nombre_Mascota)
        print(sql)
        cursor.execute(sql)
        con.commit()
        id_org = cursor.lastrowid
        return {"message":"OK", "idCliente": id_org}
    finally:
        con.close()

def update_cliente(Nombre, Apellido,Telefono, Direccion, idCliente):
    con = db.get_connection()
    cursor = con.cursor()
    try:
        sql="UPDATE CLIENTE set Nombre='{0}', Apellido='{1}', Telefono='{2}', Direccion='{3}' WHERE idCliente = {4}".format(Nombre, Apellido,Telefono, Direccion, idCliente)
        print(sql)
        cursor.execute(sql)
        con.commit()
        return {"message":"OK"}
    finally:
        con.close()

def delete_cliente(idCliente):
    con = db.get_connection()
    cursor = con.cursor()
    try:
        sql="DELETE FROM CLIENTE WHERE idCliente = {}".format(idCliente)
        cursor.execute(sql)
        con.commit()
        return {"message":"OK"}
    finally:
        con.close()
