import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

with st.sidebar:
        st.page_link('streamlit_app.py', label='Home', icon='🏠')
        st.page_link('pages/Gambaran_Umum_Desa_Selopuro.py', label='Gambaran Umum', icon='📕')
        st.page_link('pages/Data_Sosial_Selopuro.py', label='Data Sosial', icon='🫂')
        st.page_link('pages/Data_Ekonomi_Selopuro.py', label='Data Ekonomi', icon='💵')
        st.page_link('pages/Data_Pemerintahan_Selopuro.py', label='Data Pemerintahan', icon='🏛️')
        st.page_link('pages/Data_Demografis_Selopuro.py', label='Data Demografis', icon='🌏')

df_pertanian = pd.DataFrame(pd.read_csv("Data\Ekonomi\Pertanian.csv",sep=';'))
st.dataframe(df_pertanian)
chart = px.bar(df_pertanian,x="Jenis Tanaman",y="Luas (ha)")
st.plotly_chart(chart)

df_peternakan = pd.DataFrame(pd.read_csv("Data\Ekonomi\Peternakan.csv",sep=';'))
st.dataframe(df_peternakan)
chart = px.bar(df_peternakan,x="Jenis Ternak",y="Jumlah")
st.plotly_chart(chart)

df_pencaharian = pd.DataFrame(pd.read_csv("Data\Ekonomi\Pencaharian.csv",sep=';'))
st.dataframe(df_pencaharian)
chart = px.bar(df_pencaharian,x="Mata Pencaharian",y="Orang")
st.plotly_chart(chart)

background = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://i.postimg.cc/4xgNnkfX/Untitled-design.png");
background-size: cover;
background-position: center center;
background-repeat: no-repeat;
background-attachment: local;
}}[data-testid="stSidebarContent"] {{
background: #27885F;
font-color: #9e9e9e;
font-family: verdana;
}}[data-testid="stVerticalBlock"] {{
margin = 0;
padding = 0;
width:100%;
}}
</style>
"""

st.sidebar.success("Oleh tim KKN IPB 2024 Selopuro")
st.markdown("""
<style>
header {
visibility: hidden;
</style>
}""",unsafe_allow_html=True)
st.markdown(background,unsafe_allow_html=True)