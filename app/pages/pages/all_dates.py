import streamlit as st
from random import randint
st.set_page_config(page_title="информация по всем датам")
#date=st.date_input("выберите дату")
#st.write(date)
house,check_box = st.columns([0.8,0.3])
with house:   
    with st.container(border=20): 
        s = [[[1], [1, 0, 0]], [[0, 0], [1, 0]]]
        for floor in s:  #берет каждый этаж
            with st.container(border=10):
                col = st.columns(len(floor)) # на каждом этаже считает квартиры, и каждой квартире делает свой столбец 
                for i, apart in enumerate(floor): # квартиры и окна по индексу
                    with col[i]: # и в каждом окне

                            for wind in apart: 
                                    st.button(str(wind),key=str(randint(1, 10000))) #делает кнопку