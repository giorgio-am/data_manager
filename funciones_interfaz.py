try:
    import tkinter as tk                # python 3
    from tkinter import font as tkfont  # python 3
except ImportError:
    import tkinter as tk     # python 2
    import tkFont as tkfont  # python 2
from procesos_dao import ProcesoDAO
from tkinter import ttk
from cursor_pool import CursorDelPool
from logger_base import log
from tkinter import *

def ver_todos_malo():

    with CursorDelPool() as cursor:
        log.debug('Dentro del bloque with')
        cursor.execute('SELECT * FROM fichas_procesos ORDER BY id')
        registros = cursor.fetchall()
        procesos = []
        for registro in registros:
            dpto = (registro[3],)
            nombre_departamento = cursor.execute('SELECT nombre_dpto FROM derpartamentos WHERE id_dpto=%s', dpto)
            nombre = cursor.fetchall()
            nombre = (nombre[0][0])
            id_estado = (registro[14],)
            nombre_estado = cursor.execute('SELECT estado FROM estados WHERE id_estado=%s', id_estado)
            # estado = cursor.fetchall()
            # estado = (estado[0][0]) (AQUÍ FALTA ARREGLAR LOS DATOS)
            id_madurez = (registro[15],)
            nombre_madurez = cursor.execute('SELECT grado_madurez FROM madurez WHERE id_madurez=%s', id_madurez)
            madurez = cursor.fetchall()
            madurez = madurez[0][0]
            id_subdireccion_ = cursor.execute('SELECT * FROM derpartamentos WHERE id_dpto=%s', dpto)
            id_subdireccion = cursor.fetchall()
            id_subdireccion = (id_subdireccion[0][2],)
            subdireccion = cursor.execute('SELECT * FROM subdirecciones WHERE id_subdireccion=%s', id_subdireccion)
            subdireccion = cursor.fetchall()
            subdireccion = subdireccion[0][1]
            # clasificacion_i = (registro[16],)
            # clasificacion_interna = cursor.execute('SELECT * FROM clasificación WHERE id_clasificación=%s',
            #                                        clasificacion_i)
            # clasificacion_interna = cursor.fetchall()
            # clasificacion_interna = clasificacion_interna[0][1]
            # clasificacion_g = (registro[17],)
            # clasificacion_general = cursor.execute('SELECT * FROM clasificación WHERE id_clasificación=%s',
            #                                        clasificacion_g)
            # clasificacion_general = cursor.fetchall()
            # clasificacion_general = clasificacion_general[0][1]

            proceso =(registro[0], registro[1], subdireccion, nombre, registro[2] )  # número debe ser el de la columna en la bsae de datos
            procesos.append(proceso)
        return procesos

def listar_dptos():

    with CursorDelPool() as cursor:
        log.debug('Dentro del bloque with')
        cursor.execute('SELECT * FROM derpartamentos')
        registros = cursor.fetchall()
        dptos = []
        sds = []
        dptos_sds = []
        for registro in registros:

            id_subdireccion = (registro[2],)
            subdireccion = cursor.execute('SELECT * FROM subdirecciones WHERE id_subdireccion=%s', id_subdireccion)
            subdireccion = cursor.fetchall()
            subdireccion = subdireccion[0][1]


            dpto = registro[1]
            dptos.append(dpto)
            sd = registro[2]
            sds.append(sd)
            dpto_sd = (registro[1], subdireccion)
            dptos_sds.append(dpto_sd)

        return dptos_sds

def listar_subdirecciones():
    with CursorDelPool() as cursor:
        log.debug('Dentro del bloque with')
        cursor.execute('SELECT * FROM subdirecciones')

        registros = cursor.fetchall()
        subdirecciones = []
        for registro in registros:
            subdireccion = (registro[1])
            subdirecciones.append(subdireccion)
        return subdirecciones

def listar_dptos_2(subdireccion):
    if subdireccion:
        with CursorDelPool() as cursor:
            log.debug('Dentro del bloque with')
            cursor.execute('SELECT * FROM derpartamentos WHERE subdirección=%s', subdireccion)

            registros = cursor.fetchall()
            dptos = []
            for registro in registros:
                dpto = (registro[1])
                dptos.append(dpto)
            return dptos
    else:
        with CursorDelPool() as cursor:
            log.debug('Dentro del bloque with')
            cursor.execute('SELECT * FROM derpartamentos')
            registros = cursor.fetchall()
            dptos = []
            for registro in registros:
                dpto = (registro[1])
                dptos.append(dpto)

            return dptos

def nuevo_proceso():
    win = Toplevel()
    win.grab_set()
    win.title("Nuevo Proceso")
    frame = ttk.Frame(win)
    frame.pack(expand=True)

    win.geometry("300x300")

    label1 = ttk.Label(frame, text='Nombre')
    label2 = ttk.Label(frame, text='Subdirección')
    label3 = ttk.Label(frame, text='Departamento')
    label4= ttk.Label(frame, text='Alcance')
    label5 = ttk.Label(frame, text='Estado')
    label6 = ttk.Label(frame, text='Nuevo Proceso')
    label6.config(font=("Default", 20))

    id_proceso_ficha = tk.IntVar()
    nombre_proceso = tk.StringVar()
    subdirección = tk.StringVar()
    departamento = tk.StringVar()
    alcance = tk.StringVar()
    estado = tk.IntVar()

    entry1 = ttk.Entry(frame, textvariable=nombre_proceso)
    entry2 = ttk.Entry(frame, textvariable=alcance)

    combo = ttk.Combobox(frame, state='readonly', values=listar_subdirecciones(), textvariable=subdirección)
    combo2 = ttk.Combobox(frame, state='readonly', values=listar_dptos(), textvariable=departamento)

    var = IntVar()
    switch = ttk.Checkbutton(frame, text='Vigencia', style='Switch.TCheckbutton', variable=estado, onvalue=1, offvalue=0)

    def filtrar_sd(event=None):
        filtrada2 = []
        combo2.set('')
        filtrados = []
        for dpto in listar_dptos():
            #print(f'dpto[1]: {dpto[1]}')
            if dpto[1] == combo.get():
                filtrados.append(dpto[0])
            combo2.config(values=filtrados)

    combo.bind("<<ComboboxSelected>>", filtrar_sd)

    button2 = ttk.Button(frame, text='Cancelar', command=win.destroy)

    label_vacia1 = ttk.Label(frame, text='None')
    label_vacia2 = ttk.Label(frame, text=None)
    label_vacia3 = ttk.Label(frame, text=None)
    label_vacia4 = ttk.Label(frame, text=None)
    label_vacia5 = ttk.Label(frame, text=None)


    label1.grid(row=1, column=0, sticky="w", pady=5)
    label2.grid(row=2, column=0, sticky="w", pady=5)
    label3.grid(row=3, column=0, sticky="w", pady=5)
    label4.grid(row=4, column=0, sticky="w", pady=5)
    label5.grid(row=5, column=0, sticky="w", pady=5)


    entry1.grid(row=1, column=1, pady=5)
    entry2.grid(row=4, column=1, pady=5)

    combo.grid(row=2, column=1, pady=5)
    combo2.grid(row=3, column=1, pady=5)

    switch.grid(row=5, column=1, pady=5)


    button2.grid(row=6, column=1, pady=5)
    label6.grid(row=0, columnspan=3)

    def insertar_proceso():
        #nombre = nombre_proceso.get



        win2 = Toplevel()
        win2.grab_set()
        win2.title("Proceso a insertar")
        frame2 = ttk.Frame(win2)
        frame2.pack(expand=True)

        def confirmar():
            win3 = Toplevel()
            win3.grab_set()
            win3.geometry('300x100')
            win3.title('Proceso insertado')
            frame3 = ttk.Frame(win3)
            frame3.pack(expand=True)



            # win2.destroy()
            # win3.destroy()

            with CursorDelPool() as cursor:

                nombre_proceso_var = (nombre_proceso.get(), )


                nombre_departamento = (departamento.get(), )
                id_dpto = cursor.execute('SELECT id_dpto FROM derpartamentos WHERE nombre_dpto=%s', nombre_departamento)
                id_dpto = cursor.fetchall()
                id_dpto = id_dpto[0]
                alcance_var = (alcance.get(), )


                nombre_estado = estado.get()

                if nombre_estado == 1:
                    nombre_estado = ('1', )
                elif nombre_estado == 0:
                    nombre_estado = ('2', )



                _INSERT = 'INSERT INTO fichas_procesos(nombre_proceso, dpto_responsable, alcance, estado) VALUES(%s, %s, %s, %s)'
                valores = (nombre_proceso_var, id_dpto, alcance_var, nombre_estado)
                cursor.execute(_INSERT, valores)
                #return cursor.rowcount

            label_confirmacion = ttk.Label(frame3, text='Proceso insertado')
            label_confirmacion.pack()
            win2.destroy()
            win.destroy()


            aceptar = ttk.Button(frame3, text='Aceptar', command=win3.destroy)
            aceptar.pack()


        win2.geometry("300x300")

        label_nombre = ttk.Label(frame2, textvariable=nombre_proceso)
        label_subdireccion = ttk.Label(frame2, textvariable=subdirección)
        label_departamento = ttk.Label(frame2, textvariable=departamento)
        label_alcance = ttk.Label(frame2, textvariable=alcance)
        label_estado = ttk.Label(frame2, textvariable=estado)

        label_nombre_l = ttk.Label(frame2, text='Nombre Proceso: ')
        label_subdireccion_l = ttk.Label(frame2, text='Nombre Subdirección: ')
        label_departamento_l = ttk.Label(frame2, text='Nombre Departamento: ')
        label_alcance_l = ttk.Label(frame2, text='Alcance: ')
        label_estado_l = ttk.Label(frame2, text='Vigencia: ')

        button_confirmar = ttk.Button(frame2, text='Confirmar', command=confirmar)
        button_cancelar = ttk.Button(frame2, text='Cancelar', command=win2.destroy)


        label_nombre_l.grid(row=1, column=0, sticky='w')
        label_subdireccion_l.grid(row=2, column=0, sticky='w')
        label_departamento_l.grid(row=3, column=0, sticky='w')
        label_alcance_l.grid(row=4, column=0, sticky='w')
        label_estado_l.grid(row=5, column=0, sticky='w')

        label_nombre.grid(row=1, column=1, sticky='e')
        label_subdireccion.grid(row=2, column=1, sticky='e')
        label_departamento.grid(row=3, column=1, sticky='e')
        label_alcance.grid(row=4, column=1, sticky='e')
        label_estado.grid(row=5, column=1, sticky='e')

        button_confirmar.grid(row=6, column=0, pady= 20, sticky='w')
        button_cancelar.grid(row=6, column=1, pady=20, sticky='e')


    button1 = ttk.Button(frame, text='Insertar', command=insertar_proceso)
    button1.grid(row=6, column=0, pady=5)

def listar_dptos_3():
    id_subdirecciones = listar_dptos()

        # for dpto in dptos:
        #     with CursorDelPool() as cursor:
        #         log.debug('Dentro del bloque with')
        #         cursor.execute('SELECT * FROM subdirecciones WHERE id=%s',dptos)
        #         registros = cursor.fetchone()
        #         dptos_sd.append(registros)
        #     return dptos_sd
        # return dptos_sd
    return id_subdirecciones

def listar_procesos():
    with CursorDelPool() as cursor:
        log.debug('Dentro del bloque with')
        cursor.execute('SELECT * FROM fichas_procesos ORDER BY id')
        registros = cursor.fetchall()
        procesos = []
        id_proceso = []

        for registro in registros:
            print(type(registro[1]))
            proceso = f'{registro[1]}'
            procesos.append(proceso)
            id_proceso.append(registro[0])
        return procesos

def listar_procesos_id():
    with CursorDelPool() as cursor:
        log.debug('Dentro del bloque with')
        cursor.execute('SELECT * FROM fichas_procesos ORDER BY id')
        registros = cursor.fetchall()

        id_procesos = []

        for registro in registros:

            id_proceso = (registro[0],registro[1])
            id_procesos.append(id_proceso)

        return id_procesos


def editar_proceso():
    win = Toplevel()
    win.grab_set()
    win.title("Editar Proceso")
    frame = ttk.Frame(win)
    frame.pack(expand=True)

    win.geometry("300x350")

    label0 = ttk.Label(frame, text='Id')
    label1 = ttk.Label(frame, text='Nombre')
    label2 = ttk.Label(frame, text='Subdirección')
    label3 = ttk.Label(frame, text='Departamento')
    label4= ttk.Label(frame, text='Alcance')
    label5 = ttk.Label(frame, text='Estado')
    label6 = ttk.Label(frame, text='Proceso a Editar')
    label6.config(font=("Default", 20))

    id_proceso_ficha = tk.StringVar()
    nombre_proceso = tk.StringVar()
    subdirección = tk.StringVar()
    departamento = tk.StringVar()
    alcance = tk.StringVar()
    estado = tk.IntVar()

# AAAAAAAAAAAAAAAAAAAAAAAAAAAA
    lista_departamentos = listar_dptos()
    lista_dptos = []
    for dpto in lista_departamentos:
        nombre_dpto = dpto[0]
        lista_dptos.append(nombre_dpto)

    lista_ids = listar_procesos_id()

    lista_id_2 = []
    for proceso in lista_ids:

        id_dpto = proceso[0]
        lista_id_2.append(id_dpto)

    # entry1 = ttk.Entry(frame, textvariable=nombre_proceso)
    entry2 = ttk.Entry(frame, textvariable=alcance)

    combo_id = ttk.Combobox(frame, state='readonly', values=lista_id_2, textvariable=id_proceso_ficha)
    combo_nombre = ttk.Combobox(frame, values=listar_procesos(), textvariable=nombre_proceso)
    combo = ttk.Combobox(frame, state='readonly', values=listar_subdirecciones(), textvariable=subdirección)
    combo2 = ttk.Combobox(frame, state='readonly', values=lista_dptos, textvariable=departamento)


    switch = ttk.Checkbutton(frame, text='Vigencia', style='Switch.TCheckbutton', variable=estado, onvalue=1, offvalue=0)

    def filtrar_sd(event=None):
        combo2.set('')
        filtrados = []
        for dpto in listar_dptos():
            if dpto[1] == combo.get():
                filtrados.append(dpto[0])
            combo2.config(values=filtrados)

    def filtrar_nombre(event=None):

        filtrada_nombres = []
        lista_prueba = listar_procesos_id()
        for tupla in lista_prueba:

            print(tupla)
            print(type(combo_id.get()))
            if tupla[0] == int(combo_id.get()):
                filtrada_nombres.append(tupla[1])

            combo_nombre.config(values=filtrada_nombres)
            #print(filtrada_nombres)



    combo.bind("<<ComboboxSelected>>", filtrar_sd)
    combo_id.bind("<<ComboboxSelected>>", filtrar_nombre)
    #combo_nombre.bind("<<ComboboxSelected>>")

    button2 = ttk.Button(frame, text='Cancelar', command=win.destroy)

    label_vacia1 = ttk.Label(frame, text='None')
    label_vacia2 = ttk.Label(frame, text=None)
    label_vacia3 = ttk.Label(frame, text=None)
    label_vacia4 = ttk.Label(frame, text=None)
    label_vacia5 = ttk.Label(frame, text=None)

    label0.grid(row=1, column=0, sticky="w", pady=5)
    label1.grid(row=2, column=0, sticky="w", pady=5)
    label2.grid(row=3, column=0, sticky="w", pady=5)
    label3.grid(row=4, column=0, sticky="w", pady=5)
    label4.grid(row=5, column=0, sticky="w", pady=5)
    label5.grid(row=6, column=0, sticky="w", pady=5)

    combo_id.grid(row=1, column=1, pady=5)
    combo_nombre.grid(row=2, column=1, pady=5)
    #entry1.grid(row=1, column=1, pady=5)
    entry2.grid(row=5, column=1, pady=5)

    combo.grid(row=3, column=1, pady=5)
    combo2.grid(row=4, column=1, pady=5)

    switch.grid(row=6, column=1, pady=5)


    button2.grid(row=7, column=1, pady=5)
    label6.grid(row=0, columnspan=3)

    def resumen_editar():
        #nombre = nombre_proceso.get



        win4 = Toplevel()
        win4.grab_set()
        win4.title("Proceso a editar")
        frame4 = ttk.Frame(win4)
        frame4.pack(expand=True)

        def confirmar_edicion():
            win3 = Toplevel()
            win3.geometry('300x100')
            win3.title('Proceso editado')
            frame3 = ttk.Frame(win3)
            frame3.pack(expand=True)



            # win2.destroy()
            # win3.destroy()

            with CursorDelPool() as cursor:
                _ACTUALIZAR = 'UPDATE fichas_procesos SET nombre_proceso=%s, dpto_responsable=%s, alcance=%s, estado=%s WHERE id=%s'
                nombre_proceso_var = (nombre_proceso.get(), )


                nombre_departamento = (departamento.get(), )
                id_dpto = cursor.execute('SELECT id_dpto FROM derpartamentos WHERE nombre_dpto=%s', nombre_departamento)
                id_dpto = cursor.fetchall()
                id_dpto = id_dpto[0]
                alcance_var = (alcance.get(), )

                id_proceso = combo_id.get()

                nombre_estado = estado.get()

                if nombre_estado == 1:
                    nombre_estado = ('1', )
                elif nombre_estado == 0:
                    nombre_estado = ('2', )




                valores = (nombre_proceso_var, id_dpto, alcance_var, nombre_estado,id_proceso)
                cursor.execute(_ACTUALIZAR, valores)
                #return cursor.rowcount

            label_confirmacion = ttk.Label(frame3, text='Proceso insertado')
            label_confirmacion.pack()
            win4.destroy()
            win.destroy()


            aceptar = ttk.Button(frame3, text='Aceptar', command=win3.destroy)
            aceptar.pack()


        win4.geometry("300x300")

        label_nombre = ttk.Label(frame4, textvariable=nombre_proceso)
        label_subdireccion = ttk.Label(frame4, textvariable=subdirección)
        label_departamento = ttk.Label(frame4, textvariable=departamento)
        label_alcance = ttk.Label(frame4, textvariable=alcance)
        label_estado = ttk.Label(frame4, textvariable=estado)

        label_nombre_l = ttk.Label(frame4, text='Nombre Proceso: ')
        label_subdireccion_l = ttk.Label(frame4, text='Nombre Subdirección: ')
        label_departamento_l = ttk.Label(frame4, text='Nombre Departamento: ')
        label_alcance_l = ttk.Label(frame4, text='Alcance: ')
        label_estado_l = ttk.Label(frame4, text='Vigencia: ')

        button_confirmar = ttk.Button(frame4, text='Confirmar', command=confirmar_edicion)
        button_cancelar = ttk.Button(frame4, text='Cancelar', command=win4.destroy)


        label_nombre_l.grid(row=1, column=0, sticky='w')
        label_subdireccion_l.grid(row=2, column=0, sticky='w')
        label_departamento_l.grid(row=3, column=0, sticky='w')
        label_alcance_l.grid(row=4, column=0, sticky='w')
        label_estado_l.grid(row=5, column=0, sticky='w')

        label_nombre.grid(row=1, column=1, sticky='e')
        label_subdireccion.grid(row=2, column=1, sticky='e')
        label_departamento.grid(row=3, column=1, sticky='e')
        label_alcance.grid(row=4, column=1, sticky='e')
        label_estado.grid(row=5, column=1, sticky='e')

        button_confirmar.grid(row=6, column=0, pady= 20, sticky='w')
        button_cancelar.grid(row=6, column=1, pady=20, sticky='e')


    button1 = ttk.Button(frame, text='Editar', command=resumen_editar)
    button1.grid(row=7, column=0, pady=5)


def eliminar_proceso():
    win = Toplevel()
    win.grab_set()
    win.title("Eliminar Proceso")
    frame = ttk.Frame(win)
    frame.pack(expand=True)

    win.geometry("300x350")

    label0 = ttk.Label(frame, text='Id')
    label1 = ttk.Label(frame, text='Nombre')
    label2 = ttk.Label(frame, text='Subdirección')
    label3 = ttk.Label(frame, text='Departamento')
    #label4 = ttk.Label(frame, text='Alcance')
    #label5 = ttk.Label(frame, text='Estado')
    label6 = ttk.Label(frame, text='Proceso a Eliminar')
    label6.config(font=("Default", 20))

    id_proceso_ficha = tk.StringVar()
    nombre_proceso = tk.StringVar()
    subdirección = tk.StringVar()
    departamento = tk.StringVar()
    alcance = tk.StringVar()
    estado = tk.IntVar()

    # AAAAAAAAAAAAAAAAAAAAAAAAAAAA
    lista_departamentos = listar_dptos()
    lista_dptos = []
    for dpto in lista_departamentos:
        nombre_dpto = dpto[0]
        lista_dptos.append(nombre_dpto)

    lista_ids = listar_procesos_id()

    lista_id_2 = []
    for proceso in lista_ids:
        id_dpto = proceso[0]
        lista_id_2.append(id_dpto)

    # entry1 = ttk.Entry(frame, textvariable=nombre_proceso)
    #entry2 = ttk.Entry(frame, textvariable=alcance)

    combo_id = ttk.Combobox(frame, state='readonly', values=lista_id_2, textvariable=id_proceso_ficha)
    combo_nombre = ttk.Combobox(frame, state='readonly', values=listar_procesos(), textvariable=nombre_proceso)
    combo = ttk.Combobox(frame, state='readonly', textvariable=subdirección)
    combo2 = ttk.Combobox(frame, state='readonly', values=lista_dptos, textvariable=departamento)

    switch = ttk.Checkbutton(frame, text='Vigencia', style='Switch.TCheckbutton', variable=estado, onvalue=1,
                             offvalue=0)

    def filtrar_sd(event=None):
        combo2.set('')
        filtrados = []
        for dpto in listar_dptos():
            if dpto[1] == combo.get():
                filtrados.append(dpto[0])
            combo2.config(values=filtrados)

    def filtrar_nombre(event=None):
        #ficha_entera = ver_todos_con_id(com)
        filtrada_nombres = []
        lista_prueba = listar_procesos_id()
        id_prueba = lista_prueba[0][0]
        ficha_entera = ver_todos_con_id(id_prueba)
        for tupla in lista_prueba:

            print(tupla)
            print(type(combo_id.get()))
            if tupla[0] == int(combo_id.get()):
                filtrada_nombres.append(tupla[1])
                combo_nombre.set(tupla[1])
                combo.set(ficha_entera[0][2])
                combo2.set(ficha_entera[0][3])
            #combo_nombre.config(values=filtrada_nombres)
            # print(filtrada_nombres)
            #combo_nombre.set(filtrada_nombres)

    def filtrar_ids(event=None):


        #print(f' fecha entera es:    {ficha_entera}')
        filtrada_id = []
        lista_prueba_2 = listar_procesos_id()

        for tupla in lista_prueba_2:

            print(tupla)
            print(type(combo_id.get()))
            if tupla[1] == combo_nombre.get():
                ficha_entera = ver_todos_con_id(tupla[0])
                filtrada_id.append(tupla[0])
                combo_id.set(tupla[0])
                combo.set(ficha_entera[0][2])
                combo2.set(ficha_entera[0][3])

    # def filtrar_d():
    #     registros = funciones_interfaz.ver_todos_malo()
    #     combo.set('')
    #     combo2.set('')
    #     tree.delete(*tree.get_children())
    #     for registro in registros:
    #         tree.insert('', tk.END, values=registro[0:7])

    #combo.bind("<<ComboboxSelected>>", filtrar_sd)
    combo_id.bind("<<ComboboxSelected>>", filtrar_nombre)
    combo_nombre.bind("<<ComboboxSelected>>", filtrar_ids)

    button2 = ttk.Button(frame, text='Cancelar', command=win.destroy)

    label_vacia1 = ttk.Label(frame, text='None')
    label_vacia2 = ttk.Label(frame, text=None)
    label_vacia3 = ttk.Label(frame, text=None)
    label_vacia4 = ttk.Label(frame, text=None)
    label_vacia5 = ttk.Label(frame, text=None)

    label0.grid(row=1, column=0, sticky="w", pady=5)
    label1.grid(row=2, column=0, sticky="w", pady=5)
    label2.grid(row=3, column=0, sticky="w", pady=5)
    label3.grid(row=4, column=0, sticky="w", pady=5)
    #label4.grid(row=5, column=0, sticky="w", pady=5)
    #label5.grid(row=6, column=0, sticky="w", pady=5)

    combo_id.grid(row=1, column=1, pady=5)
    combo_nombre.grid(row=2, column=1, pady=5)
    # entry1.grid(row=1, column=1, pady=5)
    #entry2.grid(row=5, column=1, pady=5)

    combo.grid(row=3, column=1, pady=5)
    combo2.grid(row=4, column=1, pady=5)

    #switch.grid(row=6, column=1, pady=5)

    button2.grid(row=6, column=1, pady=5)
    label6.grid(row=0, columnspan=3)

    def resumen_eliminar():
        # nombre = nombre_proceso.get

        win4 = Toplevel()
        win4.grab_set()
        win4.title("Proceso a eliminar")
        frame4 = ttk.Frame(win4)
        frame4.pack(expand=True)

        def confirmar_eliminacion():
            win5 = Toplevel()
            win5.grab_set()
            win5.geometry('300x100')
            win5.title('Proceso Eliminado')
            frame5 = ttk.Frame(win5)
            frame5.pack(expand=True)
            label_eliminacion = ttk.Label(frame5, text='Proceso Eliminado')
            # win2.destroy()
            # win3.destroy()
            ELIMINAR = 'DELETE FROM fichas_procesos WHERE id=%s'

            with CursorDelPool() as cursor:

                valores = (combo_id.get(),)
                cursor.execute(ELIMINAR, valores)
                #return cursor.rowcount

            label_eliminacion.pack()


            win4.destroy()
            win.destroy()

            aceptar = ttk.Button(frame5, text='Aceptar', command=win5.destroy)
            aceptar.pack()

        win4.geometry("300x300")

        label_nombre = ttk.Label(frame4, textvariable=nombre_proceso)
        label_subdireccion = ttk.Label(frame4, textvariable=subdirección)
        label_departamento = ttk.Label(frame4, textvariable=departamento)
        label_alcance = ttk.Label(frame4, textvariable=alcance)
        label_estado = ttk.Label(frame4, textvariable=estado)

        label_nombre_l = ttk.Label(frame4, text='Nombre Proceso: ')
        label_subdireccion_l = ttk.Label(frame4, text='Nombre Subdirección: ')
        label_departamento_l = ttk.Label(frame4, text='Nombre Departamento: ')
        label_alcance_l = ttk.Label(frame4, text='Alcance: ')
        label_estado_l = ttk.Label(frame4, text='Vigencia: ')

        button_confirmar = ttk.Button(frame4, text='Confirmar', command=confirmar_eliminacion)
        button_cancelar = ttk.Button(frame4, text='Cancelar', command=win4.destroy)

        label_nombre_l.grid(row=1, column=0, sticky='w')
        label_subdireccion_l.grid(row=2, column=0, sticky='w')
        label_departamento_l.grid(row=3, column=0, sticky='w')
        label_alcance_l.grid(row=4, column=0, sticky='w')
        label_estado_l.grid(row=5, column=0, sticky='w')

        label_nombre.grid(row=1, column=1, sticky='e')
        label_subdireccion.grid(row=2, column=1, sticky='e')
        label_departamento.grid(row=3, column=1, sticky='e')
        label_alcance.grid(row=4, column=1, sticky='e')
        label_estado.grid(row=5, column=1, sticky='e')

        button_confirmar.grid(row=5, column=0, pady=20, sticky='w')
        button_cancelar.grid(row=5, column=1, pady=20, sticky='e')

    button1 = ttk.Button(frame, text='Eliminar', command=resumen_eliminar)
    button1.grid(row=6, column=0, pady=5)

def ver_todos_con_id(id):

    with CursorDelPool() as cursor:
        log.debug('Dentro del bloque with')
        _id = (id,)
        cursor.execute('SELECT * FROM fichas_procesos WHERE id=%s',_id)
        registros = cursor.fetchall()
        procesos = []
        for registro in registros:
            dpto = (registro[3],)
            nombre_departamento = cursor.execute('SELECT nombre_dpto FROM derpartamentos WHERE id_dpto=%s', dpto)
            nombre = cursor.fetchall()
            nombre = (nombre[0][0])
            id_estado = (registro[14],)
            nombre_estado = cursor.execute('SELECT estado FROM estados WHERE id_estado=%s', id_estado)
            estado = cursor.fetchall()
            estado = (estado[0][0])
            id_madurez = (registro[15],)
            nombre_madurez = cursor.execute('SELECT grado_madurez FROM madurez WHERE id_madurez=%s', id_madurez)
            madurez = cursor.fetchall()
            madurez = madurez[0][0]
            id_subdireccion_ = cursor.execute('SELECT * FROM derpartamentos WHERE id_dpto=%s', dpto)
            id_subdireccion = cursor.fetchall()
            id_subdireccion = (id_subdireccion[0][2],)
            subdireccion = cursor.execute('SELECT * FROM subdirecciones WHERE id_subdireccion=%s', id_subdireccion)
            subdireccion = cursor.fetchall()
            subdireccion = subdireccion[0][1]
            clasificacion_i = (registro[16],)
            clasificacion_interna = cursor.execute('SELECT * FROM clasificación WHERE id_clasificación=%s',
                                                   clasificacion_i)
            clasificacion_interna = cursor.fetchall()
            clasificacion_interna = clasificacion_interna[0][1]
            clasificacion_g = (registro[17],)
            clasificacion_general = cursor.execute('SELECT * FROM clasificación WHERE id_clasificación=%s',
                                                   clasificacion_g)
            clasificacion_general = cursor.fetchall()
            clasificacion_general = clasificacion_general[0][1]

            proceso =(registro[0], registro[1], subdireccion, nombre, registro[2] , estado)  # número debe ser el de la columna en la bsae de datos
            procesos.append(proceso)
        return procesos





if __name__ == '__main__':
    print(ver_todos_con_id(1)[0][2])
    print(ver_todos_malo())
    print(listar_dptos())



