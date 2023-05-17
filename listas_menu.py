from cursor_pool import CursorDelPool
from logger_base import log
from procesos import Proceso


def listar_subdirecciones():
    with CursorDelPool() as cursor:
        log.debug('Dentro del bloque with')
        cursor.execute('SELECT * FROM subdirecciones')

        registros = cursor.fetchall()
        subdirecciones = []
        for registro in registros:
            subdireccion = (registro[0], registro[1])
            subdirecciones.append(subdireccion)

        for subdireccion in subdirecciones:
            print(f'Id: {subdireccion[0]}  {subdireccion[1]}')

def listar_dptos(subdireccion):
    with CursorDelPool() as cursor:
        log.debug('Dentro del bloque with')
        cursor.execute('SELECT * FROM derpartamentos WHERE subdirección=%s', subdireccion)

        registros = cursor.fetchall()
        dptos = []
        for registro in registros:
            dpto = (registro[0], registro[1])
            dptos.append(dpto)

        for dpto in dptos:
            print(f'Id: {dpto[0]}  {dpto[1]}')

def listar_periodicidad():
    with CursorDelPool() as cursor:
        log.debug('Dentro del bloque with')
        cursor.execute('SELECT * FROM periodicidad')
        registros = cursor.fetchall()
        periodicidades = []
        for registro in registros:
            periodicidad = (registro[0], registro[1])
            periodicidades.append(periodicidad)

        for periodicidad in periodicidades:
            print(f'Id: {periodicidad[0]}  {periodicidad[1]}')

def listar_madurez():
    with CursorDelPool() as cursor:
        log.debug('Dentro del bloque with')
        cursor.execute('SELECT * FROM madurez')
        registros = cursor.fetchall()
        periodicidades = []
        for registro in registros:
            periodicidad = (registro[0], registro[1])
            periodicidades.append(periodicidad)

        for periodicidad in periodicidades:
            print(f'Id: {periodicidad[0]}  {periodicidad[1]}')

def listar_estado():
    with CursorDelPool() as cursor:
        log.debug('Dentro del bloque with')
        cursor.execute('SELECT * FROM estados')
        registros = cursor.fetchall()
        estados = []
        for registro in registros:
            estado = (registro[0], registro[1])
            estados.append(estado)

        for estado in estados:
            print(f'Id: {estado[0]}  {estado[1]}')

def nombres_dptos(id_dpto):
    with CursorDelPool() as cursor:
        log.debug('Dentro del bloque with')
        cursor.execute('SELECT * FROM derpartamentos WHERE id_dpto=%s', id_dpto) #el valor debe ser tupla
        registros = cursor.fetchall()
        nombre = registros [0][1]
        return nombre

def nombres_subdirecciones(id_subdireccion):
    with CursorDelPool() as cursor:
        log.debug('Dentro del bloque with')
        cursor.execute('SELECT * FROM subdirecciones WHERE id_subdireccion=%s', id_subdireccion) #el valor debe ser tupla
        registros = cursor.fetchall()
        nombre = registros [0][1]
        return nombre

def listar_clasificacion():
    with CursorDelPool() as cursor:
        log.debug('Dentro del bloque with')
        cursor.execute('SELECT * FROM clasificación')
        registros = cursor.fetchall()
        clasificaciones = []
        for registro in registros:
            clasificacion = (registro[0], registro[1])
            clasificaciones.append(clasificacion)

        for clasificacion in clasificaciones:
            print(f'Id: {clasificacion[0]}  {clasificacion[1]}')

def listar_procesos():
    with CursorDelPool() as cursor:
        log.debug('Dentro del bloque with')
        cursor.execute('SELECT * FROM clasificación')
        registros = cursor.fetchall()
        clasificaciones = []
        for registro in registros:
            clasificacion = (registro[0], registro[1])
            clasificaciones.append(clasificacion)