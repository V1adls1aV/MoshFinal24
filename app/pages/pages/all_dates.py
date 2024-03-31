import streamlit as st
from random import randint
st.set_page_config(page_title="информация по всем датам")
#date=st.date_input("выберите дату")
#st.write(date)
house,check_box = st.columns([0.8,0.3])
with house:   
    with st.container(border=20): 
        s = [[[1], [1, 0, 0]], [[0, 0], [1, 0]]]
        for floor in s:
            with st.container(border=10):
                col = st.columns(len(floor))
                for i, apart in enumerate(floor):
                    with col[i]:

                            for wind in apart:
                                    st.button(str(wind),key=str(randint(1, 10000)))