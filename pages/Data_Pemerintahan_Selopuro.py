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

st.title('Data Pemerintahan Desa Selopuro')

st.write('Desa Selopuro memiliki banyak lembaga masyarakat diluar perangkat desa, yang ikut menunjang sistem pemerintahan desa.')
df_lmasyarakat = pd.DataFrame(pd.read_csv("Data/Pemerintahan/Lembaga_Masyarakat.csv",sep=';'))
col1,col2 = st.columns((1,1))
with col1:
    st.dataframe(df_lmasyarakat)
with col2:
    chart = px.bar(df_lmasyarakat,x="Lembaga Kemasyarakatan",y="Jumlah")
    st.plotly_chart(chart)

st.write('Desa Selopuro terdiri dari 5 dukuh (RW), yang masing masing memiliki sejumlah RT')
st.write('')
df_dukuh = pd.DataFrame(pd.read_csv("Data/Pemerintahan/Dukuh_RT.csv",sep=';'))
st.dataframe(df_dukuh)

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