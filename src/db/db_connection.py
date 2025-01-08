import mysql.connector
from mysql.connector import Error

def connect_to_mysql():
    try:
        connection = mysql.connector.connect(
            host="http://church15.cy8rbq816tpn.us-west-2.rds.amazonaws.com",
            port=3306,
            user="gildo",
            password="aPQWTwhxV65MiYoz9jktG53NRQbhdvBe979p2VceBXDzWNwCT4d2G",
            database=11584
        )
        if connection.is_connected():
            print("Conexão bem-sucedida!")
            return connection
    except Error as e:
        print(f"Erro ao conectar: {e}")
        return None

def close_connection(connection):
    if connection.is_connected():
        connection.close()
        print("Conexão encerrada.")
