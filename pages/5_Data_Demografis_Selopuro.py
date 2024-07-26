import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px

st.set_page_config(
    page_icon = "Image/LogoSelopuroBercerita.png",
    page_title = "Selopuro Bercerita")

df_lahan = pd.read_csv("Data\Demografis\Lahan.csv",sep=';')
st.dataframe(df_lahan)
chart = px.bar(df_lahan,x="Jenis Wilayah",y="Luas Wilayah (ha)")
st.plotly_chart(chart)