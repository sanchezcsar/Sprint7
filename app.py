import streamlit as st
import pandas as pd
import plotly.express as px

# Título de la app
st.header('Análisis de ventas de vehículos en EE.UU.')

# Cargar datos
car_data = pd.read_csv('vehicles_us.csv')

# Checkbox para histograma
if st.checkbox('Mostrar histograma del odómetro'):
    st.write('Histograma de odómetro:')
    fig_hist = px.histogram(car_data, x='odometer', color='type')
    st.plotly_chart(fig_hist, use_container_width=True)

# Checkbox para gráfico de dispersión
if st.checkbox('Mostrar gráfico de dispersión de precio vs. odómetro'):
    st.write('Gráfico de dispersión:')
    fig_scatter = px.scatter(car_data, x='odometer', y='price', color='type')
    st.plotly_chart(fig_scatter, use_container_width=True)
