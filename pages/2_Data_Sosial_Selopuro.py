import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px

st.set_page_config(
    page_icon = "Image/LogoSelopuroBercerita.png",
    page_title = "Selopuro Bercerita")

df_pendidikan = pd.read_csv("Data\Sosial\Pendidikan.csv",sep=';')
st.dataframe(df_pendidikan)
#st.bar_chart(df_pendidikan,x="Tingkat Pendidikan",y="Jumlah Orang")
chart = px.bar(df_pendidikan,x="Tingkat Pendidikan",y="Jumlah Orang")
st.plotly_chart(chart)

df_lpendidikan = pd.read_csv("Data\Sosial\Lembaga_Pendidikan.csv",sep=';')
st.dataframe(df_lpendidikan)
chart = px.bar(df_lpendidikan,x="Lembaga Pendidikan",y="Jumlah")
st.plotly_chart(chart)

df_agama = pd.read_csv("Data\Sosial\Agama.csv",sep=';')
st.dataframe(df_agama)
chart = px.bar(df_agama,x="Agama",y="Jumlah")
st.plotly_chart(chart)

df_lagama = pd.read_csv("Data\Sosial\Lembaga_Agama.csv",sep=';')
st.dataframe(df_lagama)
chart = px.bar(df_lagama,x="Tempat Ibadah",y="Jumlah")
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