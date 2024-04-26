import pymysql

class DML:
    result = []
    __host="localhost"
    __user="root"
    __password="Iiebc04299?"
    __db="practicas_profesionales"
    __port=3305

    def __init__(self,host, user, password, db, port):
        self.__host= host
        self.__user = user
        self.__password = password
        self.__db = db
        self.__port = port

    def conectar(self):
        self.db = pymysql.connect(
            host=self.__host,
            user=self.__user,
            password=self.__password,
            db=self.__db,
            port=self.__port)
        cur = self.db.cursor()
        self.cursor = cur

    def consultar(self, query, parameters=None, fetchall=False):
        if parameters:
            self.cursor.execute(query, parameters)
        else:
            self.cursor.execute(query)

        if fetchall:
            return self.cursor.fetchall()
        else:
            return self.cursor.fetchone()

    def insertar(self, query2, values):
        self.cursor.execute(query2, values)
        self.db.commit()

    def actualizar(self, query, updated_data):
        self.cursor.execute(query, updated_data)
        self.db.commit()

    def eliminar(self, query, delete_data):
        self.cursor.execute(query, delete_data)
        self.db.commit()

    def imprimir(self):
        for filas in self.result:
            print(filas)

    def cerrar_conex(self):
        self.db.close()