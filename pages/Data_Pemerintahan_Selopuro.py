import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px

st.set_page_config(
    page_icon = "Image/LogoSelopuroBercerita.png",
    page_title = "Selopuro Bercerita")

with st.sidebar:
        st.page_link('streamlit_app.py', label='Home', icon='🏠')
        st.page_link('pages/Gambaran_Umum_Desa_Selopuro.py', label='Gambaran Umum', icon='📕')
        st.page_link('pages/Data_Sosial_Selopuro.py', label='Data Sosial', icon='🫂')
        st.page_link('pages/Data_Ekonomi_Selopuro.py', label='Data Ekonomi', icon='💵')
        st.page_link('pages/Data_Pemerintahan_Selopuro.py', label='Data Pemerintahan', icon='🏛️')
        st.page_link('pages/Data_Demografis_Selopuro.py', label='Data Demografis', icon='🌏')

df_lmasyarakat = pd.DataFrame(pd.read_csv("Data/Pemerintahan/Lembaga_Masyarakat.csv",sep=';'))
st.dataframe(df_lmasyarakat)
chart = px.bar(df_lmasyarakat,x="Lembaga Kemasyarakatan",y="Jumlah")
st.plotly_chart(chart)

df_dukuh = pd.DataFrame(pd.read_csv("Data\Pemerintahan\Dukuh_RT.csv",sep=';'))
st.dataframe(df_dukuh)