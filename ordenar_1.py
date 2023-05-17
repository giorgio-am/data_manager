#Para tkinter MVC un frame es una view
import funciones_interfaz

try:
    import tkinter as tk                # python 3
    from tkinter import font as tkfont  # python 3
except ImportError:
    import Tkinter as tk     # python 2
    import tkFont as tkfont  # python 2
from procesos_dao import ProcesoDAO
from tkinter import ttk

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (MenuPrincipal, Explorar, Administrar, Opciones, Kpi):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MenuPrincipal")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class MenuPrincipal(tk.Frame):

    def __init__(self, parent, controller):




        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="GESTIÓN POR PROCESOS SSBB", font=controller.title_font)
        #label.pack(side="top", fill="x", pady=10)
        label.grid(row=0, column=1)

        button1 = tk.Button(self, text="Explorar",
                            command=lambda: controller.show_frame("Explorar"))
        button2 = tk.Button(self, text="Administrar",
                            command=lambda: controller.show_frame("Administrar"))
        button3 = tk.Button(self, text="Opciones",
                            command=lambda: controller.show_frame("Opciones"))
        button1.grid(row=1, column=1)
        button2.grid(row=2, column=1)
        button3.grid(row=3, column=1)

class Explorar(tk.Frame):


    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        dptos = funciones_interfaz.listar_dptos()
        subdirecciones = funciones_interfaz.listar_subdirecciones()
        label = tk.Label(self, text="Explorar Procesos", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        combo = ttk.Combobox(self, state='readonly', values=dptos)
        combo2 = ttk.Combobox(self, state='readonly', values=subdirecciones)
        tree = ttk.Treeview(self, columns=(1, 2, 3, 4, 5, 6), height=20, show="headings")
        tree.pack(side='left')

        tree.heading(1, text="Id")
        tree.heading(2, text="Proceso")
        tree.heading(3, text="Subdirección")
        tree.heading(4, text="Departamento")
        tree.heading(5, text="Alcance")
        tree.heading(6, text="Estado")

        tree.column(1, width=100)
        tree.column(2, width=100)
        tree.column(3, width=100)
        tree.column(4, width=100)
        tree.column(5, width=100)
        tree.column(6, width=100)
        # Inserting Scrollbar
        scroll = ttk.Scrollbar(self, orient="vertical", command=tree.yview)
        scroll.pack(side='right', fill='y')

        tree.configure(yscrollcommand=scroll.set)

        registros = funciones_interfaz.ver_todos_malo()

        def poblar():
            tree.delete(*tree.get_children())
            for registro in registros:
                tree.insert('', tk.END, values=registro[0:7])
        def volver():
            tree.delete(*tree.get_children())
            controller.show_frame("MenuPrincipal")

        def filtrar_dpto(event=None):
            filtrada = []
            for registro in registros:
                if registro[3] == combo.get():
                    filtrada.append(registro)
            tree.delete(*tree.get_children())
            for filtro in filtrada:
                tree.insert("", tk.END, values=filtro[0:7])

        def filtrar_sd(event=None):
            filtrada2 = []
            for registro in registros:
                if registro[2] == combo2.get():
                    filtrada2.append(registro)
            tree.delete(*tree.get_children())
            for filtro in filtrada2:
                tree.insert("", tk.END, values=filtro[0:7])

        button = tk.Button(self, text="Volver al Menú Principal",
                           command=volver)
        button2 = tk.Button(self, text="Ver Todos",
                            command=poblar)
        button3 = tk.Button(self, text='Indicadores', command=lambda: controller.show_frame("Kpi"))
        button.pack()
        button2.pack()
        label2 = tk.Label(self, text="Filtrar por Departamento")
        label2.pack(after=button2)
        combo.pack(after=label2)
        label3 = tk.Label(self, text="Filtrar por Subdirección")
        label3.pack(after=combo)
        combo2.pack(after=label3)
        combo.bind("<<ComboboxSelected>>", filtrar_dpto)
        combo2.bind("<<ComboboxSelected>>", filtrar_sd)
        button3.pack(after=combo2)
class Administrar(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Menú Administración", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Volver al Menú Principal",
                           command=lambda: controller.show_frame("MenuPrincipal"))
        button.pack()

class Opciones(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Opciones", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Volver al Menú Principal",
                           command=lambda: controller.show_frame("MenuPrincipal"))
        button.pack()

class Kpi(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Indicadores", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Atras",
                           command=lambda: controller.show_frame("Explorar"))
        button.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()