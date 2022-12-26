import pandas as pd
import streamlit as st
from PIL import Image
import plotly.express as px
import plotly.graph_objs as go


def config_page():
    st.set_page_config(page_title = 'EDA La Liga 2020/2021', page_icon = ':chart:', layout='wide')

def home():
    st.title('Los mejores jugadores de La Liga 2020/2021 a 31/12/2020')

    st.subheader('Introducción')

    img = Image.open('src/images/laliga.jpg')
    st.image(img, use_column_width='auto')

    st.markdown("""
    He realizado el trabajo sobre este año debido a que, a pesar de ser una liga atípica marcada 
    por el coronavirus, el Atlético de Madrid consiguió salir campeón realizando una primera vuelta 
    casi perfecta. 
    \n Para entender las diferentes hipótesis que se establecerán en este trabajo, es de vital 
    importancia conocer cómo iba la clasificación de este torneo a día 31 de diciembre de 2020.
    \nPara confeccionar la plantilla, se va a establecer una alineación con formación 4-4-2.
    """)
    
    with st.expander("Cuestión principal"):
        st.write('''
¿Cuáles fueron los mejores futbolistas, por posición, en la primera mitad de La Liga 2020?
''')
    with st.expander('Hipótesis'):
        st.write('''
        Hipótesis principal: 
        \n\t    Los mejores futbolistas pertenecen a cualquiera de los 4 equipos que 
        encabezaban la tabla a día 31/12/2020.
        \n Hipótesis secundarias:
        \n \t 1. El número de pases acertados por un centrocampista es directamente proporcional 
        al número de regates realizados por el mismo.
        \n \t 2. El número de pases acertados por equipo es directamente 
        proporcional a su posición en la tabla.
        \n \t 3. El número de despejes realizados por equipo es directamente proporcional a 
        los goles encajados.
        \n \t 4. Pregunta: ¿Qué defensas sobresalen a nivel estadístico en alguna de las 
        variables de estudio?  ''')
    with st.expander("Tabla clasificatoria a día 31/12/2020"):
        img2 = Image.open('src/images/Clasificacion.jpg')
        st.image(img2)
    

def carga_datos_2():
    with st.expander('Datasets Iniciales'):
        dataset_porteros = pd.read_csv('src/data/raw/datasetMatchGkInfo2020-La-Liga.csv')
        dataset_jugadores = pd.read_csv('src/data/raw/datasetMatchInfo2020-La-Liga.csv')
        if st.button('DF Porteros exclusivamente (Fuente: Kaggle)'):
            st.write(dataset_porteros)
        elif st.button('DF Jugadores (Fuente: Kaggle)'):
            st.write(dataset_jugadores)
    
    with st.expander('Datasets Finales Principales'):
        dataset_gk = pd.read_csv('src/data/processed/csv_principales/1_Portero.csv')
        dataset_cb = pd.read_csv('src/data/processed/csv_principales/2_Centrales.csv').iloc[:,1:]
        dataset_lb = pd.read_csv('src/data/processed/csv_principales/3_Lateral_Izquierdo.csv').iloc[:,1:]
        dataset_rb = pd.read_csv('src/data/processed/csv_principales/4_Lateral_Derecho.csv').iloc[:,1:]
        dataset_cm = pd.read_csv('src/data/processed/csv_principales/5_Mediocentros.csv').iloc[:,1:]
        dataset_lm = pd.read_csv('src/data/processed/csv_principales/6_Banda_Izquierda.csv').iloc[:,1:]
        dataset_rm = pd.read_csv('src/data/processed/csv_principales/7_Banda_Derecha.csv').iloc[:,1:]
        dataset_fw = pd.read_csv('src/data/processed/csv_principales/8_Delanteros.csv').iloc[:,1:]
        if st.button('DF Porteros'):
            st.write(dataset_gk)
        elif st.button('DF Defensas'):
            st.write(dataset_cb)
        elif st.button('DF Lateral Izquierdo'):
            st.write(dataset_lb)
        elif st.button('DF Lateral Derecho'):
            st.write(dataset_rb)
        elif st.button('DF Centrocampistas'):
            st.write(dataset_cm)
        elif st.button('DF Interior derecho'):
            st.write(dataset_rm)
        elif st.button('DF Interior izquierdo'):
            st.write(dataset_lm)
        elif st.button('DF Delanteros'):
            st.write(dataset_fw)

    with st.expander('Datasets Finales Secundarios'):
        dataset_desp = pd.read_csv('src/data/processed/csv_plots/3_Despejes_Golesencajados.csv').iloc[:,1:]
        dataset_pases = pd.read_csv('src/data/processed/csv_plots/2_Pases_Puntos(Puntos_pases).csv').iloc[:,1:]
        dataset_pr = pd.read_csv('src/data/processed/csv_plots/1_Pases_Regates.csv').iloc[:,1:]
        dataset_pr2= pd.read_csv('src/data/processed/csv_plots/1_Pases_Regates_Equipo.csv').iloc[:,1:]
        dataset_defensa = pd.read_csv('src/data/processed/csv_plots/4_Defensas_Sobresalientes(df_defensas_2).csv').iloc[:,1:]
        if st.button('DF Despejes/Goles encajados'):
            st.write(dataset_desp)
        elif st.button('DF Pases/Clasificación'):
            st.write(dataset_pases)
        elif st.button('DF Pases/Regates'):
            st.write(dataset_pr)
        elif st.button('DF Pases/Regates/Equipos'):
            st.write(dataset_pr2)
        elif st.button('DF Defensas sobresalientes'):
            st.write(dataset_defensa)


def despejes_goles():
# data preparation
    df_despejes = pd.read_csv('src/data/processed/csv_plots/3_Despejes_Golesencajados.csv')
    num_students_size  = df_despejes['Goles encajados']
    international_color = df_despejes['Despejes']

    data = [
    {
        'y': df_despejes['Despejes'],
        'x': df_despejes['Goles encajados'],
        'mode': 'markers',
        'marker': {
            'color': international_color,
            'size': num_students_size,
            'showscale': True

        },
        'text': df_despejes['Equipo']
        
        }
    ]
    layout = dict(
              xaxis= dict(title= 'Goles encajados',ticklen= 5,zeroline= False),
              yaxis= dict(title= 'Despejes',ticklen= 5,zeroline= False)
             )
    fig = dict(data = data, layout = layout)
    return fig

def pases_puntos():
    data_cm2 = pd.read_csv('src/data/processed/csv_plots/2_Pases_Puntos(Puntos_pases).csv')
    data_cm2 = data_cm2.iloc[:,1:]
    df_pases_puntos = data_cm2

    fig1 = px.bar(df_pases_puntos, 
              x="Equipo",
              y = "Pases acertados",
             template="plotly_dark",
             labels={"Equipo":'Equipos'},
             color_discrete_sequence = px.colors.qualitative.Safe,
             height=600, 
             width=700)

    fig1.update_layout(
        xaxis = dict(
            tickmode = 'linear',
            tick0 = 0,
            dtick = 1))

    fig1.update_layout(font=dict(size=9))

    return fig1

def pases_regates():
    data_pr = pd.read_csv('src/data/processed/csv_plots/1_Pases_Regates.csv')
    data_pr = data_pr.iloc[:,1:]
    trace1 =go.Scatter(
                    x = data_pr['Regates'],
                    y = data_pr['Pases Acertados'],
                    mode = "markers",
                    name = "Regates / Pases",
                    marker = dict(color = 'rgba(255, 128, 255, 0.8)'),
                    text= data_pr['Jugador']
)

    data = [trace1]

    layout = dict(title = 'Correlación Pases acertados / Regates Acertados',
              xaxis= dict(title= 'Pases Acertados',ticklen= 5,zeroline= False),
              yaxis= dict(title= 'Regates',ticklen= 5,zeroline= False)
             )

    fig = dict(data = data, layout = layout)
    #fig = go.Figure(data = data, layout=layout)

    return fig

def pases_regates_2():
    data_pr = pd.read_csv('src/data/processed/csv_plots/1_Pases_Regates_Equipo.csv')
    num_students_size  = (data_pr['Pases Acertados'] + data_pr['Regates'])*0.1
    international_color = data_pr['Regates']

    data = [
        {
        'y': data_pr['Pases Acertados'],
        'x': data_pr['Regates'],
        'mode': 'markers',
        'marker': {
            'color': international_color,
            'size': num_students_size,
            'showscale': True
        },
        'text': data_pr['Jugador']
        }
    ]
    layout = dict(title = 'Correlación Pases acertados / Regates Acertados',
              xaxis= dict(title= 'Pases Acertados',ticklen= 5,zeroline= False),
              yaxis= dict(title= 'Regates',ticklen= 5,zeroline= False)
             )
    fig = dict(data = data, layout = layout)
    return fig
    

def defensas_10():
    df_def = pd.read_csv('src/data/processed/csv_plots/4_Defensas_Sobresalientes(df_defensas_2).csv')
    df_def = df_def.iloc[:,1:].sort_values(by='Disparos bloqueados', ascending=False)
    trace0 = go.Box(y = df_def['Despejes'],
                name = 'Despejes totales',
               marker = dict(color = 'rgb(12,12,140)'),
               hovertext= df_def['Player'])

    trace1 = go.Box(y = df_def['Recuperaciones'],
                name = 'Recuperaciones totales',
               marker = dict(color = 'rgb(12,128,128)'),
               hovertext= df_def['Player'])

    trace2 = go.Box(y=df_def['Intercepciones de balón'],
                 name = 'Intercepciones de balón',
               marker_color = 'orange',
               hovertext= df_def['Player'])
    trace3 = go.Box(y=df_def['Disparos bloqueados'],
                 name = 'Disparos bloqueados',
               marker_color = 'red',
               hovertext= df_def['Player'])
    trace4 = go.Box(y=df_def['Goles encajados por partido'],
                 name = 'Goles encajados por partido',
               marker_color = 'midnightblue',
               hovertext= df_def['Player'])



    data = [trace0, trace1, trace2, trace3, trace4]
    return data
def defensas_10_2(): #Disparos bloqueados por equipo
    df_def = pd.read_csv('src/data/processed/csv_plots/4_Defensas_Sobresalientes(df_defensas_2).csv')
    df_def = df_def.iloc[:,1:].sort_values(by='Disparos bloqueados', ascending=False)
    
    
    pie1 = df_def['Disparos bloqueados']
    pie1_list =  df_def['Disparos bloqueados']  
    labels = df_def['Team']

    # figure
    fig = {
        "data": [
            {
        "values": pie1_list,
        "labels": labels,
        "domain": {"x": [0, .5]},
        "name": "Disparos bloqueados por equipo",
        "hoverinfo":"label+percent+name",
        "hole": .3,
        "type": "pie"
        },],
        "layout": {
            "title":"",
            "annotations": [
                { "font": { "size": 20},
                "showarrow": False,
                "text": "Disparos bloqueados por equipo",
                "x": 0.7,
                "y": 1.2
                },
            ]
        }
    }
    return fig

def defensas_10_3(): #Recuperaciones por equipo
    df_def = pd.read_csv('src/data/processed/csv_plots/4_Defensas_Sobresalientes(df_defensas_2).csv')
    df_def = df_def.iloc[:,1:].sort_values(by='Disparos bloqueados', ascending=False)
    
    
    pie1 = df_def['Recuperaciones']
    pie1_list =  df_def['Recuperaciones']  
    labels = df_def['Team']

    # figure
    fig = {
        "data": [
            {
        "values": pie1_list,
        "labels": labels,
        "domain": {"x": [0, .5]},
        "name": "Recuperaciones por equipo",
        "hoverinfo":"label+percent+name",
        "hole": .3,
        "type": "pie"
        },],
        "layout": {
            "title":"",
            "annotations": [
                { "font": { "size": 20},
                "showarrow": False,
                "text": "Recuperaciones por equipo",
                "x": 0.7,
                "y": 1.2
                },
            ]
        }
    }
    return fig


def conclusiones():
    with st.expander('Equipo Final'):
        st.write('A partie de las variables mencionadas anteriormente, el equipo final es el siguiente:')
        st.write('Portero: Jan Oblak (Atlético de Madrid')
        st.write('Defensas: Jules Koundé (Sevilla FC), Stefan Savic (Atlético de Madrid)')
        st.write('Laterales: Kieran Trippier (Atlético de Madrid), Javi Galán (SD Huesca)')
        st.write('Centrocampistas: Luka Modric (Real Madrid), Carlos Soler (Valencia CF)')
        st.write('Interiores: Marcos Llorente (Atlético de Madrid), Mikel Oyarzábal (Real Sociedad)')
        st.write('Delanteros: Iago Aspas(Celta de Vigo), Karim Benzema (Real Madrid)')
        img = Image.open('src/images/Campo copia.jpg')
        st.image(img, use_column_width='auto')
    
    with st.expander('Conclusión Hipótesis Principal'):
        st.write('''**Hipótesis principal:** Los mejores futbolistas pertenecen a cualquiera de los 4 equipos que 
    encabezaban la tabla a día 31/12/2020.
        \n \t Los equipos que encabezan la tabla son Atlético de Madrid, Real Madrid, Sevilla y Real Sociedad
        \n \t **Rechazamos la hipótesis nula** dado que hay tres jugadores que no pertenecen a dichos equipos
        \n \t\tJavi Galán (SD Huesca)
        \n \t\tCarlos Soler (Valencia CF)
        \n \t\tIago Aspas (Celta de Vigo)''')
    
    with st.expander ('Conclusiones Hipótesis Secundarias'):
        st.write(''' **Hipótesis secundaria 1:**
        \n"El número de pases acertados por un centrocampista es directamente proporcional al número de regates realizados por el mismo." 
        \n **Conclusión:**
        \n \t -  Se procede a realizar el coeficiente de correlación entre las variables.
        \n \t - El coeficiente de correlación es de 0.4727 positivo. Al ser menor que 0.5, no podemos 
        afirmar que exista una correlación representativa entre las variables.
        ''')

        st.write(''' **Hipótesis secundaria 2:**
        \n"El número de pases acertados por un equipo es directamente proporcional a su posición en la clasificación" 
        \n **Conclusión:**
        \n \t -  Se procede a realizar el coeficiente de correlación entre las variables.
        \n \t - El coeficiente de correlación es de 0.4058 positivo. Al ser menor que 0.5, no podemos 
        afirmar que exista una correlación representativa entre las variables.
        ''')

        st.write(''' **Hipótesis secundaria 3:**
        \n"El número de despejes realizados por equipo es directamente proporcional al número de goles encajados." 
        \n **Conclusión:**
        \n \t -  Se procede a realizar el coeficiente de correlación entre las variables.
        \n \t - El coeficiente de correlación es de 0.4282 positivo. Al ser menor que 0.5, no podemos 
        afirmar que exista una correlación representativa entre las variables.
        ''')

        st.write(''' **Hipótesis secundaria 4:**
        \n"Pregunta: ¿Qué defensas sobresalen a nivel estadístico en alguna de las variables de estudio?" 
        \n **Conclusión:**
        \n \t - En recuperaciones de balón, sobresalen David García del Osasuna, el cual fue uno de 
        los centrales de la temporada y recuperó una media de 15 balones por partido, 
        y Djené Dakonam, pertenciente al Getafe FC, con una estadística similar.
	    \n \t - En disparos bloqueados, destaca principalmente Rubén Duarte, lateral izquierdo 
        del Deportivo Alavés, el cual bloqueó una media de 3 disparos por partido. 
        Otros jugadores destacados en este ámbito fueron Pau Torres, defensa del 
        Villarreal FC que posteriormente sería convocado por la Selección Española de Fútbol. 
        Por último, destaca la escasa cantidad de disparos bloquea Yeray, el defensa central 
        habitualmente titular del Athletic Club.

        ''')
               


    

def porteros_plot():
    df_gk = pd.read_csv('src/data/processed/csv_principales/1_Portero.csv').head(5)
    
    # import graph objects as "go"
    import plotly.graph_objs as go

    # create trace1 
    trace1 = go.Bar(x = df_gk['Player'],
                y = df_gk['Goles encajados x(-1)'],
                name = 'Goles encajados',
                marker = dict(color = 'rgba(255, 174, 255, 0.5)',
                line = dict(color='rgb(0,0,0)', width = 1.5)),
                hovertext = 'Goles encajados')
                

    trace2 = go.Bar(x = df_gk['Player'],
               y = df_gk['Paradas'],
               name = 'Paradas',
               marker = dict(color = 'rgba(255, 255, 128, 0.5)',
                line = dict(color='rgb(0,0,0)', width = 1.5)),
                hovertext = 'Paradas')
               
    
    trace3 = go.Bar(x = df_gk['Player'],
               y = df_gk['Porcentaje paradas/tiros'],
               name = 'Porcentaje paradas/tiros',
               marker = dict(color = 'rgba(255, 193, 95, 0.5)',
                line = dict(color='rgb(0,0,0)', width = 1.5)),
                hovertext = 'Porcentaje de paradas/tiros')
               


    data = [trace1, trace2, trace3]

    layout = go.Layout(barmode = "group",
        title = 'Porteros')

    fig = go.Figure(data = data, layout = layout)

    return fig
    
def defensas_plot():
    df_cb = pd.read_csv('src/data/processed/csv_principales/2_Centrales.csv').head(5)
    
    # import graph objects as "go"
    import plotly.graph_objs as go

    # create trace1 
    trace1 = go.Bar(x = df_cb['Player'],
                y = df_cb['Disparos bloqueados'],
                name = 'Disparos bloqueados',
                marker = dict(color = 'rgba(255, 174, 255, 0.5)',
                line = dict(color='rgb(0,0,0)', width = 1.5)),
                hovertext= 'Disparos bloqueados (valor ponderado sobre el total)')
                

    trace2 = go.Bar(x = df_cb['Player'],
               y = df_cb['Intercepciones de balón'],
               name = 'Intercepciones de balón',
               marker = dict(color = 'rgba(255, 255, 128, 0.5)',
                line = dict(color='rgb(0,0,0)', width = 1.5)),
                hovertext='Intercepciones de balón (valor ponderado sobre el total)')
               
    
    trace3 = go.Bar(x = df_cb['Player'],
               y = df_cb['Recuperaciones'],
               name = 'Recuperaciones',
               marker = dict(color = 'rgba(255, 193, 95, 0.5)',
                line = dict(color='rgb(0,0,0)', width = 1.5)),
                hovertext='Recuperaciones (valor ponderado sobre el total)')
               
    
    trace4 = go.Bar(x = df_cb['Player'],
               y = df_cb['Despejes'],
               name = 'Despejes',
               marker = dict(color = 'rgba(255, 133, 95, 0.5)',
                line = dict(color='rgb(0,0,0)', width = 1.5)),
                hovertext = 'Despejes (valor ponderado sobre el total)')
               
    
    trace5 = go.Bar(x = df_cb['Player'],
               y = df_cb['Goles encajados por partido'],
               name = 'Goles encajados por partido',
               marker = dict(color = 'rgba(179, 255, 117, 0.5)',
                line = dict(color='rgb(0,0,0)', width = 1.5)),
                hovertext = 'Goles encajados por partido')
               
    data = [trace1, trace2, trace3, trace4, trace5]

    layout = go.Layout(barmode = "group",
        title= 'Defensas')

    fig = go.Figure(data = data, layout = layout)

    return fig 

def lateral_izquierdo_plot():
    df_lb = pd.read_csv('src/data/processed/csv_principales/3_Lateral_Izquierdo.csv').head(5)
    
    # import graph objects as "go"
    import plotly.graph_objs as go

    # create trace1 
    trace1 = go.Bar(x = df_lb['Jugador'],
                y = df_lb['Recuperaciones'],
                name = 'Recuperaciones',
                marker = dict(color = 'rgba(255, 174, 255, 0.5)',
                line = dict(color='rgb(0,0,0)', width = 1.5)),
                hovertext= 'Recuperaciones (valor ponderado sobre el total)' )
                

    trace2 = go.Bar(x = df_lb['Jugador'],
               y = df_lb['Porcentaje de pases acertados'],
               name = 'Porcentaje de pases acertados',
               marker = dict(color = 'rgba(255, 255, 128, 0.5)',
                line = dict(color='rgb(0,0,0)', width = 1.5)),
                hovertext='Porcentaje de pases acertados (ponderado sobre el total) ')
               
    
    trace3 = go.Bar(x = df_lb['Jugador'],
               y = df_lb['Porcentaje de regates acertados'],
               name = 'Porcentaje de regates acertados',
               marker = dict(color = 'rgba(255, 193, 95, 0.5)',
                line = dict(color='rgb(0,0,0)', width = 1.5)),
                hovertext='Porcentaje de regates acertados (ponderado sobre el total) ')
               
    
    trace4 = go.Bar(x = df_lb['Jugador'],
               y = df_lb['Asistencias'],
               name = 'Asistencias',
               marker = dict(color = 'rgba(255, 133, 95, 0.5)',
                line = dict(color='rgb(0,0,0)', width = 1.5)),
                hovertext = 'Asistencias')
               
    
    trace5 = go.Bar(x = df_lb['Jugador'],
               y = df_lb['Goles encajados'],
               name = 'Goles encajados por partido',
               marker = dict(color = 'rgba(179, 255, 117, 0.5)',
                line = dict(color='rgb(0,0,0)', width = 1.5)),
                hovertext = 'Goles encajados por partido (ponderados sobre el total)')
               
    data = [trace1, trace2, trace3, trace4, trace5]

    layout = go.Layout(barmode = "group",
        title= 'Lateral izquierdo')

    fig = go.Figure(data = data, layout = layout)

    return fig     

def lateral_derecho_plot():
    df_rb = pd.read_csv('src/data/processed/csv_principales/4_Lateral_Derecho.csv').head(5)
    
    # import graph objects as "go"
    import plotly.graph_objs as go

    # create trace1 
    trace1 = go.Bar(x = df_rb['Jugador'],
                y = df_rb['Recuperaciones'],
                name = 'Recuperaciones',
                marker = dict(color = 'rgba(255, 174, 255, 0.5)',
                line = dict(color='rgb(0,0,0)', width = 1.5)),
                hovertext= 'Recuperaciones (valor ponderado sobre el total)')
                

    trace2 = go.Bar(x = df_rb['Jugador'],
               y = df_rb['Porcentaje de pases acertados'],
               name = 'Porcentaje de pases acertados',
               marker = dict(color = 'rgba(255, 255, 128, 0.5)',
                line = dict(color='rgb(0,0,0)', width = 1.5)),
                hovertext='Porcentaje de pases acertados (valor ponderado sobre el total) ')
               
    
    trace3 = go.Bar(x = df_rb['Jugador'],
               y = df_rb['Porcentaje de regates acertados'],
               name = 'Porcentaje de regates acertados',
               marker = dict(color = 'rgba(255, 193, 95, 0.5)',
                line = dict(color='rgb(0,0,0)', width = 1.5)),
                hovertext='Porcentaje de regates acertados (valor ponderado sobre el total) ')
               
    
    trace4 = go.Bar(x = df_rb['Jugador'],
               y = df_rb['Asistencias'],
               name = 'Asistencias',
               marker = dict(color = 'rgba(255, 133, 95, 0.5)',
                line = dict(color='rgb(0,0,0)', width = 1.5)),
                hovertext = 'Asistencias')
               
    
    trace5 = go.Bar(x = df_rb['Jugador'],
               y = df_rb['Goles encajados'],
               name = 'Goles encajados por partido',
               marker = dict(color = 'rgba(179, 255, 117, 0.5)',
                line = dict(color='rgb(0,0,0)', width = 1.5)),
                hovertext = 'Goles encajados por partido (valor ponderado sobre el total)')
               
    data = [trace1, trace2, trace3, trace4, trace5]

    layout = go.Layout(barmode = "group",
        title= 'Lateral derecho')

    fig = go.Figure(data = data, layout = layout)

    return fig   

def centrocampista_plot():
    df_cm = pd.read_csv('src/data/processed/csv_principales/5_Mediocentros.csv').head(5)
    
    # import graph objects as "go"
    import plotly.graph_objs as go

    # create trace1 
    trace1 = go.Bar(x = df_cm['Jugador'],
                y = df_cm['Recuperaciones'],
                name = 'Recuperaciones',
                marker = dict(color = 'rgba(255, 174, 255, 0.5)',
                line = dict(color='rgb(0,0,0)', width = 1.5)),
                hovertext= 'Recuperaciones (valor ponderado sobre el total)')
                

    trace2 = go.Bar(x = df_cm['Jugador'],
               y = df_cm['Porcentaje de pases acertados'],
               name = 'Porcentaje de pases acertados',
               marker = dict(color = 'rgba(255, 255, 128, 0.5)',
                line = dict(color='rgb(0,0,0)', width = 1.5)),
                hovertext='Porcentaje de pases acertados (valor ponderado sobre el total) ')
               
    
    trace3 = go.Bar(x = df_cm['Jugador'],
               y = df_cm['Regates Acertados'],
               name = 'Regates acertados',
               marker = dict(color = 'rgba(255, 193, 95, 0.5)',
                line = dict(color='rgb(0,0,0)', width = 1.5)),
                hovertext='Regates acertados (valor ponderado sobre el total) ')
               
    
    trace4 = go.Bar(x = df_cm['Jugador'],
               y = df_cm['Asistencias'],
               name = 'Asistencias',
               marker = dict(color = 'rgba(255, 133, 95, 0.5)',
                line = dict(color='rgb(0,0,0)', width = 1.5)),
                hovertext = 'Asistencias')
               
    
    trace5 = go.Bar(x = df_cm['Jugador'],
               y = df_cm['Goles'],
               name = 'Goles',
               marker = dict(color = 'rgba(179, 255, 117, 0.5)',
                line = dict(color='rgb(0,0,0)', width = 1.5)),
                hovertext = 'Goles')
               
    data = [trace1, trace2, trace3, trace4, trace5]

    layout = go.Layout(barmode = "group",
        title= 'Centrocampistas')

    fig = go.Figure(data = data, layout = layout)

    return fig    

def banda_izquierda_plot():
    df_lm = pd.read_csv('src/data/processed/csv_principales/6_Banda_Izquierda.csv').head(5)
    
    # import graph objects as "go"
    import plotly.graph_objs as go

    # create trace1 
                

    trace2 = go.Bar(x = df_lm['Jugador'],
               y = df_lm['Porcentaje de pases acertados'],
               name = 'Porcentaje de pases acertados',
               marker = dict(color = 'rgba(255, 255, 128, 0.5)',
                line = dict(color='rgb(0,0,0)', width = 1.5)),
                hovertext='Porcentaje de pases acertados (valor ponderado sobre el total) ')
               
    
    trace3 = go.Bar(x = df_lm['Jugador'],
               y = df_lm['Porcentaje de regates acertados'],
               name = 'Porcentaje de regates acertados',
               marker = dict(color = 'rgba(255, 193, 95, 0.5)',
                line = dict(color='rgb(0,0,0)', width = 1.5)),
                hovertext='Porcentaje de regates acertados (valor ponderado sobre el total)')
               
    
    trace4 = go.Bar(x = df_lm['Jugador'],
               y = df_lm['Asistencias'],
               name = 'Asistencias',
               marker = dict(color = 'rgba(255, 133, 95, 0.5)',
                line = dict(color='rgb(0,0,0)', width = 1.5)),
                hovertext = 'Asistencias')
               
    
    trace5 = go.Bar(x = df_lm['Jugador'],
               y = df_lm['Goles'],
               name = 'Goles',
               marker = dict(color = 'rgba(179, 255, 117, 0.5)',
                line = dict(color='rgb(0,0,0)', width = 1.5)),
                hovertext = 'Goles')
               
    data = [ trace2, trace3, trace4, trace5]

    layout = go.Layout(barmode = "group",
        title= 'Interior izquierdo')

    fig = go.Figure(data = data, layout = layout)

    return fig    

def banda_derecha_plot():
    df_rm = pd.read_csv('src/data/processed/csv_principales/7_Banda_Derecha.csv').head(5)
    
    # import graph objects as "go"
    import plotly.graph_objs as go

    # create trace1 
                

    trace2 = go.Bar(x = df_rm['Jugador'],
               y = df_rm['Porcentaje de pases acertados'],
               name = 'Porcentaje de pases acertados',
               marker = dict(color = 'rgba(255, 255, 128, 0.5)',
                line = dict(color='rgb(0,0,0)', width = 1.5)),
                hovertext='Porcentaje de pases acertados (valor ponderado sobre el total) ')
               
    
    trace3 = go.Bar(x = df_rm['Jugador'],
               y = df_rm['Porcentaje de regates acertados'],
               name = 'Porcentaje de regates acertados',
               marker = dict(color = 'rgba(255, 193, 95, 0.5)',
                line = dict(color='rgb(0,0,0)', width = 1.5)),
                hovertext='Porcentaje de regates acertados (valor ponderado sobre el total)')
               
    
    trace4 = go.Bar(x = df_rm['Jugador'],
               y = df_rm['Asistencias'],
               name = 'Asistencias',
               marker = dict(color = 'rgba(255, 133, 95, 0.5)',
                line = dict(color='rgb(0,0,0)', width = 1.5)),
                hovertext = 'Asistencias')
               
    
    trace5 = go.Bar(x = df_rm['Jugador'],
               y = df_rm['Goles'],
               name = 'Goles',
               marker = dict(color = 'rgba(179, 255, 117, 0.5)',
                line = dict(color='rgb(0,0,0)', width = 1.5)),
                hovertext = 'Goles')
               
    data = [ trace2, trace3, trace4, trace5]

    layout = go.Layout(barmode = "group",
        title= 'Interior derecho')

    fig = go.Figure(data = data, layout = layout)

    return fig    

def delanteros_plot():
    df_fw = pd.read_csv('src/data/processed/csv_principales/8_Delanteros.csv').head(5)
    
    # import graph objects as "go"
    import plotly.graph_objs as go

    # create trace1 
                

    trace2 = go.Bar(x = df_fw['Jugador'],
               y = df_fw['Porcentaje de pases acertados'],
               name = 'Porcentaje de pases acertados',
               marker = dict(color = 'rgba(255, 255, 128, 0.5)',
                line = dict(color='rgb(0,0,0)', width = 1.5)),
                hovertext='Porcentaje de pases acertados (valor ponderado sobre el total) ')
               
    
    trace3 = go.Bar(x = df_fw['Jugador'],
               y = df_fw['Porcentaje de regates acertados'],
               name = 'Porcentaje de regates acertados',
               marker = dict(color = 'rgba(255, 193, 95, 0.5)',
                line = dict(color='rgb(0,0,0)', width = 1.5)),
                hovertext='Porcentaje de regates acertados (valor ponderado sobre el total)')
               
    
    trace4 = go.Bar(x = df_fw['Jugador'],
               y = df_fw['Asistencias'],
               name = 'Asistencias',
               marker = dict(color = 'rgba(255, 133, 95, 0.5)',
                line = dict(color='rgb(0,0,0)', width = 1.5)),
                hovertext = 'Asistencias')
               
    
    trace5 = go.Bar(x = df_fw['Jugador'],
               y = df_fw['Goles'],
               name = 'Goles',
               marker = dict(color = 'rgba(179, 255, 117, 0.5)',
                line = dict(color='rgb(0,0,0)', width = 1.5)),
                hovertext = 'Goles')
               
    data = [ trace2, trace3, trace4, trace5]

    layout = go.Layout(barmode = "group",
        title= 'Delanteros')

    fig = go.Figure(data = data, layout = layout)

    return fig     