# reutilizo los archivos de conexion, cursor y logger. Eso lo podria utilizar cada vez que necesite un proyecto
# conectandome a una base de datos postgreSQL

import logging
from logger_base import log
#import psycopg2 as bd ya no lo uso, debo importar otro
from psycopg2 import pool
import sys

class Conexion:
    _DATABASE = 'Procesos'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    # _conexion = None esto será administrado por el POOL DE CONEXIONES
    # _cursor = None
    _MIN_CON = 1
    _MAX_CON = 5 # MINIMO Y MAXIMO DE CONEXIONES
    _pool = None

    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON, cls._MAX_CON, host=cls._HOST, user=cls._USERNAME,
                                                      password=cls._PASSWORD, port=cls._DB_PORT, database=cls._DATABASE)
                log.debug(f'Creación del pool exitosa: {cls._pool}')
                return cls._pool
            except Exception as e:
                log.error(f'Ocurrió un error al obtener el pool: {e}')
                sys.exit()
        else:
            return cls._pool


    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn() #getconn devuelve un objeto de conexion desde el pool (que tiene maximo 5)
        log.debug(f'Conexion obtenida del pool: {conexion}')
        return conexion
        pass

    @classmethod
    def liberarConexion(cls, conexion):
        cls.obtenerPool().putconn(conexion)
        log.debug(f'Regresamos la conexion al pool: {conexion}')

    @classmethod
    def cerrarConexiones(cls):
        cls.obtenerPool().closeall()
    # tambien el pool de conexion
        # if cls._conexion is None:
        #     try:
        #         cls._conexion = bd.connect(host=cls._HOST,
        #                                    user=cls._USERNAME,
        #                                    password=cls._PASSWORD,
        #                                    port=cls._DB_PORT,
        #                                    database=cls._DATABASE)
        #         log.debug(f'Conexión exitosa: {cls._conexion}')
        #         return cls._conexion
        #     except Exception as e:
        #         log.debug(f'Ocurrió una excepción: {e}')
        #         sys.exit()
        # else:
        #     return cls._conexion
    # @classmethod
    # def obtenerCursor(cls):
    #     if cls._cursor is None or cls._cursor.closed: # si dejo solo el none, puede q se cierre el cursor, asi va a ser distinto de none poer estará cerrado
    #         try:
    #             cls._cursor = cls.obtenerConexion().cursor()
    #             log.debug(f'Se abrió correctamente el cursor: {cls._cursor}')
    #             return cls._cursor
    #         except Exception as e:
    #             log.error(f'Ocurrió una excepción: {e}') #error pq es un problema ya en la aplicación
    #     else:
    #         return cls._cursor
# todo el cursor se verá en el POOL


if __name__ == '__main__':
    conexion1 = Conexion.obtenerConexion()
    Conexion.liberarConexion((conexion1))
    conexion2 = Conexion.obtenerConexion()

    pass
    # Conexion.obtenerConexion()
    # Conexion.obtenerCursor()