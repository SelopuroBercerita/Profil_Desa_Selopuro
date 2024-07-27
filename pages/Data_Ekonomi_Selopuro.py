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

st.title('Data Ekonomi Desa Selopuro')
st.write('Kondisi perekonomian di Desa Selopuro cukup beragam. Hal ini dipengaruhi salah satunya oleh kondisi demografis dan geografisnya yang dekat dengan daerah gunung, pantai, dan perkotaan.')
st.write('Bidang pertanian di selopuro masih berjalan. Pertanian dilakukan dengan metode tadah hujan, karena kondisi air untuk irigasi yang sulit terutama di saat musing kemarau.')
col1,col2 = st.columns((1,1))
df_pertanian = pd.DataFrame(pd.read_csv("Data/Ekonomi/Pertanian.csv",sep=';'))
with col1:
        st.dataframe(df_pertanian)
with col2:
        chart = px.bar(df_pertanian,x="Jenis Tanaman",y="Luas (ha)")
        st.plotly_chart(chart)
st.write('Lahan pertanian sebagian besar dimanfaatkan untuk komoditas padi Sawah, lalu palawija. Selain itu ada juga jagung dan tembakau.')

st.write('Peternakan bukan merupakan mata pencaharian utama untuk masyarakat Desa Selopuro, melainkan merupakan pekerjaan tambahan.')
df_peternakan = pd.DataFrame(pd.read_csv("Data/Ekonomi/Peternakan.csv",sep=';'))
col3,col4 = st.columns((1,1))
with col3:
        st.dataframe(df_peternakan)
with col4:
        chart = px.bar(df_peternakan,x="Jenis Ternak",y="Jumlah")
        st.plotly_chart(chart)


st.write('Mata pencaharian masyarakat Desa Selopuro cukup beragam.')
df_pencaharian = pd.DataFrame(pd.read_csv("Data/Ekonomi/Pencaharian.csv",sep=';'))
col5,col6 = st.columns((1,1))
with col5:
        st.dataframe(df_pencaharian)
with col6:
        chart = px.bar(df_pencaharian,x="Mata Pencaharian",y="Orang")
        st.plotly_chart(chart)

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
st.markdown(styling,unsafe_allow_html=True)
st.sidebar.success("Oleh tim KKN IPB 2024 Selopuro")
st.markdown(background,unsafe_allow_html=True)