import pandas as pd
import streamlit as st
from PIL import Image
import functions as ft

ft.config_page()

menu = st.sidebar.selectbox('Elige una sección:', ('Introducción', 'Dataframes','Cuadros Finales','Conclusiones', 'Gráficos hipótesis secundarias', 'Recursos utilizados'))

if menu == 'Introducción':
    ft.home()
elif menu == 'Dataframes':
    ft.carga_datos_2()

elif menu == 'Cuadros Finales':
    fig_final_1 = ft.porteros_plot()
    fig_final_2 = ft.defensas_plot()
    fig_final_3 = ft.lateral_izquierdo_plot()
    fig_final_4 = ft.lateral_derecho_plot()
    fig_final_5 = ft.centrocampista_plot()
    fig_final_6 = ft.banda_izquierda_plot()
    fig_final_7 = ft.banda_derecha_plot()
    fig_final_8 = ft.delanteros_plot()
    with st.expander('Porteros'):
        st.plotly_chart(fig_final_1, use_container_width=True)
    with st.expander('Defensas'):
        st.plotly_chart(fig_final_2, use_container_width=True)
    with st.expander('Lateral Izquierdo'):
        st.plotly_chart(fig_final_3, use_container_width=True)
    with st.expander('Lateral Derecho'):
        st.plotly_chart(fig_final_4, use_container_width=True)
    with st.expander('Centrocampistas'):
        st.plotly_chart(fig_final_5, use_container_width=True)
    with st.expander('Interior izquierdo'):
        st.plotly_chart(fig_final_6, use_container_width=True)
    with st.expander('Interior derecho'):
        st.plotly_chart(fig_final_7, use_container_width=True)
    with st.expander('Delanteros'):
        st.plotly_chart(fig_final_8, use_container_width=True)

elif menu == 'Conclusiones':
    st.header('Conclusiones')
    ft.conclusiones()


elif menu == 'Gráficos hipótesis secundarias':
    menu_plots = st.sidebar.radio("Escoge los gráficos que quieres observar",options=["Relación Pases/Regates", "Relación Pases/Clasificación","Relación Despejes/Goles Encajados",'Defensas Sobresalientes'])

    if menu_plots == 'Relación Pases/Regates':
        fig2 = ft.pases_regates()
        fig2_1 = ft.pases_regates_2()
        st.header('Relación Pases/Regates')
        st.plotly_chart(fig2, use_container_width=True)
        st.plotly_chart(fig2_1, use_container_width=True)
    
      
    elif menu_plots == 'Relación Pases/Clasificación':
        fig1 = ft.pases_puntos()
        st.header('Relación Pases/Clasificación')
        st.plotly_chart(fig1, use_container_width=True)
    
    elif menu_plots== 'Relación Despejes/Goles Encajados':
        fig0 = ft.despejes_goles()
        st.header('Relación Despejes/Goles Encajados')
        st.plotly_chart(fig0, use_container_width = True,)

   
    elif menu_plots == 'Defensas Sobresalientes':
        fig3 = ft.defensas_10()
        fig3_1 = ft.defensas_10_2()
        fig3_2 = ft.defensas_10_3()
        st.header('Defensas Sobresalientes')
        st.plotly_chart(fig3, use_container_width=True)
        st.plotly_chart(fig3_1, use_container_width=True)
        st.plotly_chart(fig3_2, use_container_width=True)

else:
    st.header('Recursos utilizados')
    st.write('Lenguaje de programación: Python') 
    st.write('Interfaz web de código: Jupyter Notebook') 
    st.write('Editor de código: Visual Studio Code')
    st.write('Desarrollo de la web: Streamlit')
    with st.expander('Librerías utilizadas'):
        st.write('Numpy')
        st.write('Pandas')
        st.write('Plotly')
        st.write('Streamlit') 
        

   
