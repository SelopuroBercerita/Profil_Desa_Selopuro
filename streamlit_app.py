import streamlit as st

st.set_page_config(
    page_icon = "Image/LogoSelopuroBercerita.png",
    page_title = "Selopuro Bercerita")

st.sidebar.success("Oleh tim KKN IPB 2024 Selopuro")

with st.sidebar:
        st.page_link('streamlit_app.py', label='home', icon='🏠')
        st.page_link('pages/1_Gambaran_Umum_Desa_Selopuro.py', label='Gambaran Umum', icon='📕')
        st.page_link('pages/2_Data_Sosial_Selopuro.py', label='Data Sosial', icon='🫂')
        st.page_link('pages/3_Data_Ekonomi_Selopuro.py', label='Data Ekonomi', icon='💵')
        st.page_link('pages/4_Data_Pemerintahan_Selopuro.py', label='Data Pemerintahan', icon='🏛️')
        st.page_link('pages/5_Data_Demografis_Selopuro.py', label='Data Demografis', icon='🌏')



title = """
<div class="four">
  <h1> <span> Selopuro Bercerita </span> Profil Desa <em>Selopuro</em></h1>
</div>

<style>
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

h1 span {
  display: block;
  font-size: 0.5em;
  line-height: 1.3;
  color: #FFFFFF;
}
h1 em {
  font-style: normal;
  font-weight: 600;
  color: #FFFFFF;
}


.four h1 {
  text-align: center;
  padding-bottom: 0.7em;
  transform : translate(5%, -45%)
}
.four h1 span {
  font-weight: 300;
  word-spacing: 3px;
  line-height: 2em;
  padding-bottom: 0.35em;
  color: #FFFFFF;
}
.four h1:before {
  position: absolute;
  left: 0;
  bottom: 0;
  width: 120px;
  height: 1px;
  content: "";
  left: 50%;
  margin-left: -60px;
  background-color: #FFFFFF;
}
</style>
"""

background = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://i.imgur.com/FtT3Gwm.png");
background-size: cover;
background-position: center center;
background-repeat: no-repeat;
background-attachment: local;
}}
[data-testid="stSidebarContent"] {{
background: #27885F;
font-color: #9e9e9e
}}
</style>
"""

body = """
<div class="center">
    <div class="page">
        <h1>Selopuro Bercerita</h1>
        <img src="https://drive.google.com/thumbnail?id=1qb0Uf_CyCR5m4KPhr-T2bEm8cYCmbEyN">
    </div>
</div>

<style>
header {
visibility: hidden;
}
body {
    margin: 0;
    padding: 0;
    font-family: verdana;
    background: #CCC;
}

.center {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -10%);
}

.page {
    width: 400px;
    height: 600px;
    padding: 30px;
    background: #FFF;
    border-left: 30px solid #3CA378;
    transform: rotate(-45deg) skewX(10deg) scale(.8);
    box-shadow: -50px 50px 50px rgba(0, 0, 0, 0.5);
    filter: none;
}

.page h1 {
    margin: 0 0 20px 0;
    padding: 0;
    text-align: center;
    font-size: 25px;
    color: #9e9e9e
}

.page p {
    margin: 0;
    padding: 0;
    text-align: justify;
    color: #9e9e9e
}

.page img {
  position: absolute;
  top: 35%;
  left: 40%;
  transform: translate(-30%, 0%);
  max-width: 100%;
  height: auto;
}

.page:before {
    content: "";
    width: 30px;
    height: 100%;
    background: #27885F;
    position: absolute;
    top: 0;
    left: 0;
    transform: skewY(-45deg) translate(-57px, -43px) 
}

.page:after {
    content: "";
    width: 106%;
    height: 30px;
    background: #CCC;
    position: absolute;
    bottom: 0;
    left: 0;
    transform: skewX(-45deg) translate(-11px, 30px)
}
</style>
"""
st.markdown(title, unsafe_allow_html=True)
st.markdown(background, unsafe_allow_html=True)
st.markdown(body, unsafe_allow_html=True)

#st.title("Welcome to Selopuro")
#st.write("Looking for new kades")
#st.write(
    #"Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
#)
