import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px

st.set_page_config(
    page_icon = "Image/LogoSelopuroBercerita.png",
    page_title = "Selopuro Bercerita")

df_lmasyarakat = pd.DataFrame(pd.read_csv("Data\Pemerintahan\Lembaga_Masyarakat.csv",sep=';'))
st.dataframe(df_lmasyarakat)
chart = px.bar(df_lmasyarakat,x="Lembaga Kemasyarakatan",y="Jumlah")
st.plotly_chart(chart)

df_dukuh = pd.DataFrame(pd.read_csv("Data\Pemerintahan\Dukuh_RT.csv",sep=';'))
st.dataframe(df_dukuh)