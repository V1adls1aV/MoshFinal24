import streamlit as st
import requests

def get_by_date(date:str) -> list:
    date = date.split('-')
    res = requests.get(f'https://olimp.miet.ru/ppo_it_final?day={date[0]}&month={date[1]}&year={date[2]}', headers= {
    'X-Auth-Token' : 'ppo_11_18922'},).json()['message']
    result = []
    floor_num = 1
    floors =[]
    while True:
        try:
            floor = []
            temp_floor = iter(res['windows']['data'][f'floor_{floor_num}'])
            for j in res['windows_for_flat']['data']:
                appart = []
                for _ in range(j):
                    appart.append(next(temp_floor))
                result.append(appart)
                floor.append(any(appart))
            floors.append(floor)
            floor_num += 1
        except:
            break
    floors.reverse()
    flat_numbers = []
    for i in range(len(floors)):
        for j in range(res['flats_count']['data']):
            if floors[i][j] == True:
                flat_numbers.append((i)*res['flats_count']['data'] + j+1)
    return [len(flat_numbers), flat_numbers, floors, len(appart), result]

st.title('Визуализация результатов поиска')

date = st.text_input('Введите дату:')

if date:
    result = get_by_date(date)
    st.write(f"Количество квартир с необходимыми ресурсами: {result[0]}")
    st.write(f"Номера квартир с необходимыми ресурсами: {result[1]}")
    st.write("Визуализация комнат в каждой квартире:")
    floors = result[2]
    for i in range(len(result[4])):
        st.write(f' Квартира {i+1} : {[int(num) for num in result[4][i]]}')
             
else:
    st.write('Пожалуйста, введите дату для получения результатов.')
