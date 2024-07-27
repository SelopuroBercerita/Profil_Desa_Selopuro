import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px

st.set_page_config(
    page_icon = "Image/LogoSelopuroBercerita.png",
    page_title = "Selopuro Bercerita")

with st.sidebar:
        st.page_link('streamlit_app.py', label='home', icon='🏠')
        st.page_link('pages/Gambaran_Umum_Desa_Selopuro.py', label='Gambaran Umum', icon='📕')
        st.page_link('pages/Data_Sosial_Selopuro.py', label='Data Sosial', icon='🫂')
        st.page_link('pages/Data_Ekonomi_Selopuro.py', label='Data Ekonomi', icon='💵')
        st.page_link('pages/Data_Pemerintahan_Selopuro.py', label='Data Pemerintahan', icon='🏛️')
        st.page_link('pages/Data_Demografis_Selopuro.py', label='Data Demografis', icon='🌏')

background = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://i.imgur.com/kMBwZF2.jpg");
background-size: cover;
background-position: center center;
background-repeat: no-repeat;
background-attachment: local;
}}
[data-testid="stSidebarContent"] {{
  background: #27885F;
  color: #FFFFFF;
  font-color: #FFFFFF;
}}
[data-testid="stMarkdownContainer"] {{
  color: #FFFFFF;
  font-color: #FFFFFF;
}}
[data-testid="stSidebarCollapseButton"] {{
  color: #FFFFFF;
  font-color: #FFFFFF;
}}
[data-testid="baseButton-headerNoPadding"] {{
  color: #FFFFFF;
  font-color: #FFFFFF;
}}
[data-testid="stHeading"] {{
  color: #FFFFFF;
  font-color: #FFFFFF;
}}
</style>
"""
st.title("Data Demografis Desa Selopuro")
df_lahan = pd.read_csv("Data/Demografis/Lahan.csv",sep=';')
st.dataframe(df_lahan)
chart = px.pie(df_lahan,names="Jenis wilayah",values="Luas wilayah (ha)")
st.plotly_chart(chart)

styling = """
<style>
header {
visibility: hidden;
}
h1 {
  position: relative;
  padding: 0;
  margin-top: 0;
  font-family: "Raleway", sans-serif;
  font-weight: 300;
  font-size: 40px;
  color: #FFFFFF;
  -webkit-transition: all 0.4s ease 0s;
  -o-transition: all 0.4s ease 0s;
  transition: all 0.4s ease 0s;
}
</style>
"""

st.sidebar.success("Oleh tim KKN IPB 2024 Selopuro")
st.markdown(styling,unsafe_allow_html=True)

st.markdown(background,unsafe_allow_html=True)