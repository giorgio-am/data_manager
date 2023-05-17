import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.pyplot import figure, bar, xticks, show, text


def graficar_ano(ano):

    df = pd.read_csv('Base ley 18834.csv', delimiter=';')
    #print(df)
    df['Ponderador'] = df['Ponderador'].str.replace(',','.',n=1)
    df['Cumplimiento'] = df['Cumplimiento'].str.replace(',','.',n=1)
    #print(df)
    df_limpio = df
    df_limpio['Ponderador'] = df_limpio['Ponderador'].astype(float).round(2)
    df_limpio['Cumplimiento'] = pd.to_numeric(df_limpio['Cumplimiento'], errors='coerce')
    #print(df_limpio.dtypes)
    #print(df_limpio)
    df_limpio_2 = df_limpio.dropna(subset='Cumplimiento')
    #print(df_limpio_2)
    df_limpio['Cumplimiento'] = df_limpio['Cumplimiento'].replace(np.nan, 0)
    #print(df_limpio)

    df_limpio['ResultadoPonderado'] = df_limpio['Cumplimiento']*df_limpio['Ponderador']
    #print(df_limpio)

    barplot = df_limpio.groupby(['Ano', 'Establecimiento'], as_index=False)['ResultadoPonderado'].sum()

    #print(barplot)

    metas_2021 = barplot[barplot['Ano'].isin((int(ano), ))]
    #print(metas_2021)

    establecimientos = metas_2021['Establecimiento'].to_list()
    resultados = metas_2021['ResultadoPonderado']
    resultados_por_100 = []
    for resultado in resultados:
        resultado = resultado*100
        resultados_por_100.append(resultado)

    establecimientos[0] = 'CAVRR'
    establecimientos[1] = 'DSSBB'

    fig, ax = plt.subplots(figsize=(10, 6), tight_layout=True)
    fig = bar(establecimientos, resultados_por_100)
    ax.set_title("Cumplimiento Anual Ley 18.834")
    ax.set_ylabel("Porcentaje de Cumplimiento")
    #figure(figsize=(10, 10), tight_layout=True)
    for barra in fig: # con este loop voy obteniendo la etiqueta para cada barra del gráfico
        yval = barra.get_height()
        yval1 = round(yval, 2) #asi puedo agregar una etiqueta
        etiqueta = str(yval1)
        text(barra.get_x() , yval , etiqueta + '%')
    #print(type(etiqueta))
    max_chars = 20

    #print(establecimientos[0])


    xticks(rotation=30)
    #fig.tight_layout()
    show()
#graficar_ano(2011)