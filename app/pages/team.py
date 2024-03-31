import streamlit as st

st.set_page_config(
    page_title="Team",
)

#STYLES
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://images.unsplash.com/photo-1709572563747-5de4d256fa6c?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
background-size: cover;
background-position: center center;
background-repeat: no-repeat;
background-attachment: local;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
</style>
"""
card = f"""
background-color: beige;
border: 4px
"""
#STYLES
st.sidebar.success("predprof final")
st.markdown(page_bg_img, unsafe_allow_html=True)

#st.image("https://avatars.mds.yandex.net/get-altay/1881734/2a00000186f0b0e5501073631801aab84b7f/XL")
#st.image("https://i.pinimg.com/564x/c0/49/85/c04985baa5b18e54636217e5d51f0de8.jpg")
st.markdown('<div style="text-align: left;">lorem ipsum</div>', unsafe_allow_html=True)

st.subheader("Etiam imperdiet mi in vehicula aliquam. Ut posuere rhoncus lobortis. Sed diam lorem, bibendum eget lacus et, cursus pellentesque quam. Donec a scelerisque justo, sed hendrerit ante. Aenean at erat.")
memb1, memb2, memb3, memb4, memb5 = st.columns(5)
with memb1:
    with st.container(border= 5):
        "## memb1"
        st.image("https://upload.wikimedia.org/wikipedia/commons/9/99/Sample_User_Icon.png")
        "первый"
with memb2:
    with st.container(border= 5):
        "## memb2"
        st.image("https://upload.wikimedia.org/wikipedia/commons/9/99/Sample_User_Icon.png")
        "второй"
with memb3:
    with st.container(border= 5):
        "## memb3"
        st.image("https://upload.wikimedia.org/wikipedia/commons/9/99/Sample_User_Icon.png")
        "третий"
with memb4:
    with st.container(border= 5):
        "## memb4"
        st.image("https://upload.wikimedia.org/wikipedia/commons/9/99/Sample_User_Icon.png")
        "четвертый"
with memb5:
    with st.container(border= 5):
        "## memb5"
        st.image("https://upload.wikimedia.org/wikipedia/commons/9/99/Sample_User_Icon.png")
        "пятый"