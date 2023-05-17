class Proceso:
    def __init__(self, id_proceso=None, nombre_proceso=None, departamento=None, estado=None, madurez=None, subdireccion=None, alcance=None,
                 clasificacion_interna=None, clasificacion_general=None, kpi=None):
        self._id_proceso = id_proceso
        self._nombre_proceso = nombre_proceso
        self._departamento = departamento
        self._estado = estado
        self._madurez = madurez
        self._subdireccion = subdireccion
        self._alcance = alcance
        self._clasificacion_interna = clasificacion_interna
        self._clasificacion_general = clasificacion_general
        self._kpi = kpi


    def __str__(self):
        return f'Proceso: {self._id_proceso} , Nombre del proceso: {self._nombre_proceso}, Departamento Responsable: {self._departamento},' \
               f'Subdireccion: {self._subdireccion}, Alcance: {self._alcance}, Clasificación interna: {self._clasificacion_interna},' \
               f' Clasificación General: {self._clasificacion_general}, Estado: {self._estado}, Grado de Madurez: {self._madurez}, Indicadores: {self._kpi}'

    @property
    def id_proceso(self):
        return self._id_proceso
    @id_proceso.setter
    def id_proceso(self, id_proceso):
        self._id_proceso = id_proceso

    @property
    def nombre_proceso(self):
        return self._nombre_proceso
    @nombre_proceso.setter
    def nombre_proceso(self, nombre_proceso):
        self._nombre_proceso = nombre_proceso

    @property
    def departamento(self):
        return self._departamento
    @departamento.setter
    def departamento(self, departamento): #aqui podría agregar validaciones (mayus, tipos de caracteres etc.)
        self._departamento = departamento

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, estado):
        self._estado = estado

    @property
    def madurez(self):
        return self._madurez

    @madurez.setter
    def madurez(self, madurez):
        self._madurez = madurez

    @property
    def subdireccion(self):
        return self._subdireccion

    @subdireccion.setter
    def subdireccion(self, subdireccion):
        self._subdireccion = subdireccion

    @property
    def alcance(self):
        return self._alcance

    @alcance.setter
    def alcance(self, alcance):
        self._alcance = alcance

    @property
    def clasificacion_interna(self):
        return self._clasificacion_interna

    @clasificacion_interna.setter
    def clasificacion_interna(self, clasificacion_interna):
        self._clasificacion_interna = clasificacion_interna

    @property
    def clasificacion_general(self):
        return self._clasificacion_general

    @clasificacion_general.setter
    def clasificacion_general(self, clasificacion_general):
        self._clasificacion_general = clasificacion_general

    @property
    def kpi(self):
        return self._kpi

    @kpi.setter
    def kpi(self, kpi):
        self._kpi = kpi

class Subproceso(Proceso):
    pass