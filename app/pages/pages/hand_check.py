import streamlit as st
import datetime as dt
import pandas as pd
st.set_page_config(page_title="ручная проверка")
floors = st.number_input("количество этажей",key="floors",step=1,min_value=1)
floors = st.number_input("количество комнат на этаже",key="flats",step=1,min_value=1)
with st.container(border=5):
    st.dataframe(pd.DataFrame())