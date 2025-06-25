import pandas as pd

import streamlit as st

import matplotlib.pyplot as plt

import seaborn as sns

import locale

locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')

#Es necesario importar las depencendias necesarias
from datetime import date
from datetime import datetime

#Día actual
today = date.today()

#Fecha actual
now = datetime.now()


dayName = today.strftime('%A %d de %B del Año %Y')


# Configuración de la página

st.set_page_config(layout='centered', page_title='Talento Tech')

t1, t2 = st.columns([0.3, 0.7])
t1.image('Matrix_code.webp', width=200)
t2.title('Martes 17')
t2.markdown('**tel:** 3218725370 **| email:** danielmabofilo@gmail.com')

with st.sidebar:
    st.write('Sidebar')

steps=st.tabs(['Penguins', 'Pestaña 1','Pestaña 3','Epidemiología'])

df = pd.read_csv('penguins.csv')

with steps[0]:
    st.write('Información 1')
    st.write(df.head())
    st.write('Hoy es ', dayName)
    especie = st.selectbox('Seleccione la especie',
                           ['Adelie','Gentoo', 'Chinstrap'])
    
    variable_x = st.selectbox('Seleccione la variable x', 
                           ['bill_length_mm','bill_depth_mm', 'flipper_length_mm','body_mass_g'])
    variable_y = st.selectbox('Seleccione la variable y', 
                           ['bill_length_mm','bill_depth_mm', 'flipper_length_mm','body_mass_g'])
    
    df = df[df['species']==especie]

    fig, ax = plt.subplots()
    ax = sns.scatterplot(x=df[variable_x], y=df[variable_y])
    plt.xlabel(variable_x)
    plt.ylabel(variable_y)
    plt.title('Gráfica de la especie {} de pingüinos'.format(especie))
    st.pyplot(fig)

with steps[1]:
    st.markdown('# Podemos usar $\LaTeX$ $$\dfrac{\pi}{2}$$')
    sns.set_style('darkgrid')
    df1=pd.read_csv('penguins.csv')
    markers={'Adelie':'x','Gentoo':'s','Chistrap':'0'}
    fig1, ax1=plt.subplots()
    ax1=sns.scatterplot(data=df1, x=variable_x, y=variable_y,
                        hue='species', markers=markers)
    plt.xlabel(variable_x)
    plt.ylabel(variable_y)
    st.pyplot(fig1)

with steps[2]:
    st.title('Árboles')
    df2=pd.read_csv('trees.csv')
    st.dataframe(df2)
    dfg=pd.DataFrame(df2.groupby(['dbh'])['tree_id'].count())
    dfg.columns=['tree_count']
    t1, t2, t3 = st.columns([0.3, 0.3, 0.3])

    st.line_chart(dfg)
    st.bar_chart(dfg)
    st.area_chart(dfg)

    t1.line_chart(dfg)
    t2.bar_chart(dfg)
    t3.area_chart(dfg)

    df3 = df2.dropna(subset=['longitude','latitude'])
    st.map(df3)



with steps[3]:
    st.title('Epidemiologia Colombia')
    df4 = pd.read_csv('Eventos_Epidemiol_gicos_20250619.csv',encoding='UTF-8')
    st.dataframe(df4)



