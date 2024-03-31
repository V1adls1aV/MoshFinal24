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
                wind=0
                for apart in range(len(floor)):
                    
                    wind +=len(apart)
                col = st.columns(wind)
                for i, apart in enumerate(floor):
                    with col[i]:
                            for windo in apart:
                                st.button(str(windo),key=str(randint(1, 10000)))