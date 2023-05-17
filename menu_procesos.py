import listas_menu
from logger_base import log
from procesos import Proceso
from procesos_dao import ProcesoDAO
from cursor_pool import CursorDelPool
from listas_menu import listar_subdirecciones
from listas_menu import listar_dptos
from listas_menu import listar_estado
from listas_menu import nombres_dptos

opcion = None
while opcion != 5:
    print('Opciones')
    print('1: Listar Procesos')
    print('2: Agregar Proceso')
    print('3: Modificar Proceso')
    print('4: Eliminar Proceso')
    print('5: Salir')
    opcion = int(input('Escriba una opcion (1-5): '))
    if opcion == 1:
        opcion_1 = None
        while opcion_1 != 4:
            print('Menu principal --- Opciones')
            print('1: Ver todos los procesos')
            print('2: Ver por subdirección')
            print('3: Ver por departamento')
            print('4: Volver')

            opcion_1 = int(input('Escriba un opción (1-4): '))
            if opcion_1 == 1:
                procesos = ProcesoDAO.seleccionar()
                for proceso in procesos:
                    log.info(proceso)
                # opcion_1 = 5
            elif opcion_1 == 2:
                listas_menu.listar_subdirecciones()
                id_subdireccion = input('Escriba id subdirección: ')
                id_subdireccion = (id_subdireccion, )
                procesos = ProcesoDAO.seleccionar()
                nombre_subdireccion = listas_menu.nombres_subdirecciones(id_subdireccion)

                filtrada = filter(lambda proceso: proceso.subdireccion == nombre_subdireccion, procesos)
                for proceso in filtrada:
                    log.info(proceso)
            elif opcion_1 == 3:
                listas_menu.listar_subdirecciones()
                subdireccion = (input('Escriba id subdirección: '))
                listas_menu.listar_dptos(subdireccion)
                dpto_responsable_var = (input('Escribe el Departamento Responsable (id): '))
                dpto_responsable_var = (dpto_responsable_var,) # debe ser una tupla la que meto a la funcion del archivo listas_menu
                procesos = ProcesoDAO.seleccionar()
                nombre_dpto = listas_menu.nombres_dptos(dpto_responsable_var)
                filtrada = filter(lambda proceso: proceso.departamento == nombre_dpto, procesos)
                for proceso in filtrada:
                    log.info(proceso)

    elif opcion == 2:
        nombre_proceso_var = input('Escribe Nombre del Proceso: ')
        listas_menu.listar_subdirecciones()
        subdireccion = (input('Escriba id subdirección: '))
        listas_menu.listar_dptos(subdireccion)
        dpto_responsable_var = input('Escribe el Departamento Responsable (id): ')
        listas_menu.listar_estado()
        estado_var = input('Ingresar Estado (id): ')
        listas_menu.listar_madurez()
        madurez_var = input('Ingresar grado de madurez (id): ')
        listas_menu.listar_clasificacion()
        clasificacion_interna_var = input('Ingrese clasificación interna (id): ')
        listas_menu.listar_clasificacion()
        clasificacion_general_var = input('Ingrese clasificación general (id): ')
        proceso = Proceso(nombre_proceso=nombre_proceso_var, departamento=dpto_responsable_var, estado=estado_var, madurez=madurez_var, clasificacion_general=clasificacion_general_var, clasificacion_interna=clasificacion_interna_var)
        procesos_insertados = ProcesoDAO.insertar(proceso)
        log.info(f'Procesos insertados: {procesos_insertados}')

    elif opcion == 3:
        id_proceso_var = int(input('Escribe el id_proceso a modificar: '))
        nombre_proceso_var = input('Escribe el nuevo nombre del proceso: ')
        dpto_responsable_var = input('Escribe el dpto responsable (id): ')
        proceso = Proceso(id_proceso_var, nombre_proceso_var, dpto_responsable_var)
        procesos_actualizados = ProcesoDAO.actualizar(proceso)
        log.info(f'procesos actualizados: {procesos_actualizados}')

    elif opcion == 4:
        id_proceso_var = int(input('Escribe el id_proceso a eliminar: '))
        proceso = Proceso(id_proceso=id_proceso_var)
        procesos_eliminados = ProcesoDAO.eliminar(proceso)
        log.info(f'procesos eliminados: {procesos_eliminados}')
else:
    log.info('Salimos de la aplicación')