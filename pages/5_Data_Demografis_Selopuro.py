import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px

st.set_page_config(
    page_icon = "Image/LogoSelopuroBercerita.png",
    page_title = "Selopuro Bercerita")

df_lahan = pd.read_csv("Data\Demografis\Lahan.csv",sep=';')
st.dataframe(df_lahan)
chart = px.pie(df_lahan,names="Jenis wilayah",values="Luas wilayah (ha)")
st.plotly_chart(chart)