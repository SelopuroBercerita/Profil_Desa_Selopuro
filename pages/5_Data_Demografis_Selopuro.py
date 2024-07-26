import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px

st.set_page_config(
    page_icon = "Image/LogoSelopuroBercerita.png",
    page_title = "Selopuro Bercerita")

with st.sidebar:
        st.page_link('streamlit_app.py', label='home', icon='🏠')
        st.page_link('pages/1_Gambaran_Umum_Desa.py', label='Gambaran Umum', icon='📕')
        st.page_link('pages/2_Data_Sosial_Selopuro.py', label='Data Sosial', icon='🫂')
        st.page_link('pages/3_Data_Ekonomi_Selopuro.py', label='Data Ekonomi', icon='💵')
        st.page_link('pages/4_Data_Pemerintahan_Selopuro.py', label='Data Pemerintahan', icon='🏛️')
        st.page_link('pages/5_Data_Demografis_Selopuro.py', label='Data Demografis', icon='🌏')

df_lahan = pd.read_csv("Data\Demografis\Lahan.csv",sep=';')
st.dataframe(df_lahan)
chart = px.pie(df_lahan,names="Jenis wilayah",values="Luas wilayah (ha)")
st.plotly_chart(chart)