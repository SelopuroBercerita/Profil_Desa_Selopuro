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

st.title('Data Sosial Desa Selopuro')
st.write('Desa Selopuro merupakan sebuah desa yang sangat hangat, dengan penduduk yang ramah. Kami pun ikut merasakan kehangatan tersebut ketika melaksanakan KKN.')

st.write('Aspek pertama adalah pendidikan, Pendidikan memiliki peran yang sangat penting dalam pembangunan dan kemajuan suatu desa, termasuk Desa Selopuro. Pendidikan merupakan fondasi utama yang membentuk karakter dan keterampilan individu, sehingga mampu berkontribusi secara positif terhadap masyarakat. Di desa, pendidikan tidak hanya berfungsi sebagai sarana untuk meningkatkan pengetahuan dan keterampilan, tetapi juga sebagai alat untuk mengurangi kesenjangan sosial dan ekonomi.')
col1,col2 = st.columns((1,1))
df_pendidikan = pd.read_csv("Data/Sosial/Pendidikan.csv",sep=';')
with col1:
    st.dataframe(df_pendidikan)
with col2:
    chart = px.bar(df_pendidikan,x="Tingkat Pendidikan",y="Jumlah Orang",template="simple_white")
    st.plotly_chart(chart)
st.write('Sebagian besar masyarakat Selopuro memiliki tingkat pendidikan SD/Sederajat, sebagian lagi sampai SMP. Sebagian lulus SMA yang menepati wajib belajar 12 tahun, dan sebagian kecil memiliki kesempatan untuk melanjutkannya ke perguruan tinggi. Masih ada bagian masyarakat yang putus sekolah dan buta huruf. Data ini menunjukan bahwa pendidikan di Desa Selopuro perlu lagi untuk ditingkatkan.')

st.write('Masih didalam aspek pendidikan, data dibawah menunjukan tentang lembaga pendidikan yang ada di Desa Selopuro.')
col3,col4 = st.columns((1,1))
df_lpendidikan = pd.read_csv("Data/Sosial/Lembaga_Pendidikan.csv",sep=';')
with col3:
    st.dataframe(df_lpendidikan)
with col4:
    chart = px.bar(df_lpendidikan,x="Lembaga Pendidikan",y="Jumlah")
    st.plotly_chart(chart)
st.write('Dari data dapat dilihat TK dan SD terdapat cukup banyak di Desa Selopuro, akan tetapi, tidak ada SMP dan SMA. Hal ini mungkin menjadi salah satu pengaruh, tingkatan pendidikan di masyarakat sekitar karena keberadaan sarana pendidikan SMP dan SMA yang cukup jauh.')

st.write('Aspek selanjutnya adalah Agama, masyarakat selopuro cenderung bertoleransi terhadap Agama.')
col5,col6 = st.columns((1,1))
df_agama = pd.read_csv("Data/Sosial/Agama.csv",sep=';')
with col5:
    st.dataframe(df_agama)
with col6:
    chart = px.bar(df_agama,x="Agama",y="Jumlah")
    st.plotly_chart(chart)
st.write('Masyarakat Desa Selopuro sebagian besar memeluk Agama Islam dan sebagian lainnya memeluk agama Kristen dan Hindu.')

st.write('Keberadaan lembaga dan sarana untuk beribadah dipengaruhi dengan jumlah pemeluk di daerah sekitar.')
col7,col8 = st.columns((1,1))
df_lagama = pd.read_csv("Data/Sosial/Lembaga_Agama.csv",sep=';')
with col7:
    st.dataframe(df_lagama)
with col8:
    chart = px.bar(df_lagama,x="Tempat Ibadah",y="Jumlah")
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

st.sidebar.success("Oleh tim KKN IPB 2024 Selopuro")
st.markdown(background,unsafe_allow_html=True)
st.markdown(styling,unsafe_allow_html=True)