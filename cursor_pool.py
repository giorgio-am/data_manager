from conexion import Conexion
from logger_base import log


class CursorDelPool:
    def __init__(self):
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        log.debug('Inicio del metodo with __enter__')
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor
    def __exit__(self, tipo_excepcion, valor_excepcion, traceback_exception):
        log.debug('Se ejecuta metodo __exit__')
        if valor_excepcion:
            self._conexion.rollback()
            log.error(f'Ocurrio una excepcion: {valor_excepcion} Se hace rollback')
        else:
            self._conexion.commit()
            log.debug('Commit de la transaccion')
        self._cursor.close()
        Conexion.liberarConexion(self._conexion)

if __name__ == '__main__': #de aqui solo puedo recuperar registros, para obtener OBJETOS de tipo PERSONA, lo hago en persona DAO
    with CursorDelPool() as cursor:
        log.debug('Dentro del bloque with')
        cursor.execute('SELECT * FROM subdirecciones')
        log.info(cursor.fetchall())