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

def ver_todo():
    _SELECT = 'SELECT * FROM public.ley_18834 ORDER BY "Ano" ASC, "Establecimiento" ASC, "Indicador" ASC'
    with CursorDelPool() as cursor:
        log.debug('Seleccionando Proceso')
        cursor.execute(_SELECT,)
        registros = cursor.fetchall()
        resultados = []
        for resultado in registros:
            resultados.append((resultado[0], resultado[2], resultado[3], float(resultado[4]), resultado[7], resultado[8]))
    return resultados


#print((ver_todo()[1]))