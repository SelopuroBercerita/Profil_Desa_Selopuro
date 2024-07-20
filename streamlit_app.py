import streamlit as st

st.set_page_config(
    page_icon = "Image/LogoSelopuroBercerita.png",
    page_title = "Selopuro Bercerita")

#st.write("Selopuro ngopi 🍵")

st.sidebar.success("Pilih page diatas")

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
    background: #CCC
}

.center {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-30%, 0%);
}

.page {
    width: 400px;
    height: 600px;
    padding: 30px;
    background: #FFF;
    border-left: 30px solid #3CA378;
    transform: rotate(-45deg) skewX(10deg) scale(.8);
    box-shadow: -50px 50px 50px rgba(0, 0, 0, 0.5)
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
st.markdown(background, unsafe_allow_html=True)
st.markdown(body, unsafe_allow_html=True)

#st.title("Welcome to Selopuro")
#st.write("Looking for new kades")
#st.write(
    #"Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
#)
