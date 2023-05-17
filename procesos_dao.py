from cursor_pool import CursorDelPool
from logger_base import log
from procesos import Proceso


class ProcesoDAO:
    '''
    DAO - Data Acces Object para la tabla de usuario
    para operaciones de tipo CRUD
    '''
    _SELECT = 'SELECT * FROM fichas_procesos ORDER BY id'
    _INSERT = 'INSERT INTO fichas_procesos(nombre_proceso, dpto_responsable, estado, madurez, clasificación_interna, clasificación_general) VALUES(%s, %s, %s, %s, %s, %s)'
    _ACTUALIZAR = 'UPDATE fichas_procesos SET nombre_proceso=%s, dpto_responsable=%s WHERE id=%s'
    _ELIMINAR = 'DELETE FROM fichas_procesos WHERE id=%s'



    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            log.debug('Seleccionando Proceso')
            cursor.execute(cls._SELECT)
            registros = cursor.fetchall()
            procesos = []
            for registro in registros:
                dpto = (registro[3], )
                nombre_departamento = cursor.execute('SELECT nombre_dpto FROM derpartamentos WHERE id_dpto=%s', dpto)
                nombre = cursor.fetchall()
                nombre = (nombre[0][0])
                id_estado = (registro[14], )
                nombre_estado = cursor.execute('SELECT estado FROM estados WHERE id_estado=%s', id_estado)
                estado = cursor.fetchall()
                estado = (estado[0][0])
                id_madurez = (registro[15], )
                nombre_madurez = cursor.execute('SELECT grado_madurez FROM madurez WHERE id_madurez=%s', id_madurez)
                madurez = cursor.fetchall()
                madurez = madurez[0][0]
                id_subdireccion_ = cursor.execute('SELECT * FROM derpartamentos WHERE id_dpto=%s', dpto)
                id_subdireccion = cursor.fetchall()
                id_subdireccion = (id_subdireccion[0][2], )
                subdireccion = cursor.execute('SELECT * FROM subdirecciones WHERE id_subdireccion=%s', id_subdireccion)
                subdireccion = cursor.fetchall()
                subdireccion = subdireccion[0][1]
                clasificacion_i = (registro[16], )
                clasificacion_interna = cursor.execute('SELECT * FROM clasificación WHERE id_clasificación=%s', clasificacion_i)
                clasificacion_interna = cursor.fetchall()
                clasificacion_interna = clasificacion_interna[0][1]
                clasificacion_g = (registro[17], )
                clasificacion_general = cursor.execute('SELECT * FROM clasificación WHERE id_clasificación=%s',
                                                       clasificacion_g)
                clasificacion_general = cursor.fetchall()
                clasificacion_general = clasificacion_general[0][1]

                proceso = Proceso(registro[0], registro[1], nombre, estado, madurez, subdireccion, registro[2], clasificacion_interna, clasificacion_general) #número debe ser el de la columna en la bsae de datos
                procesos.append(proceso)
            return procesos



    @classmethod
    def insertar(cls, proceso):
        with CursorDelPool() as cursor:
                log.debug(f'Proceso a insertar: {proceso}')
                valores = (proceso.nombre_proceso, proceso.departamento, proceso.estado, proceso.madurez, proceso.clasificacion_interna, proceso.clasificacion_general)
                cursor.execute(cls._INSERT, valores)
                return cursor.rowcount


    @classmethod
    def actualizar(cls, proceso):
        with CursorDelPool() as cursor:
            log.debug(f'Proceso a modificar: {proceso}')
            valores = (proceso.nombre_proceso, proceso.departamento, proceso.id_proceso)
            cursor.execute(cls._ACTUALIZAR, valores)
            return cursor.rowcount
    @classmethod
    def eliminar(cls, proceso):
        with CursorDelPool() as cursor:
            log.debug(f'Proceso a eliminar: {proceso}')
            valores = (proceso.id_proceso, )
            cursor.execute(cls._ELIMINAR, valores)
            return cursor.rowcount

if __name__ == '__main__':
    procesos = ProcesoDAO.seleccionar()
    for proceso in procesos:
        log.info(proceso)
    print(type(procesos))