import streamlit as st
import datetime as dt
from random import randint
st.set_page_config(page_title="авто проверка")
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
                        with st.container(border=10):
                            for wind in apart:
                                    if wind==1:
                                        st.button(str(wind),key=str(randint(1, 10000)),)
                                    else:
                                        st.button(str(wind),key=str(randint(1, 10000)),)
 
with check_box:
    with st.container(border=10):
        with st.container(border=10):
            for i in range(0,10):
                st.checkbox(str(randint(1,10000000)))
        with st.container(border=10):
            st.date_input("введите дату")
            st.number_input("введите количество этажей",key="floors",step=1,min_value=1)
            st.number_input("введите количество комнат",key="aparts",step=1,min_value=1)
            st.text_input("введите количество комнат на этаже")
            st.text_input("введите номера комнат")
            st.button("сохранить")