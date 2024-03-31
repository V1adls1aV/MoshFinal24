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
                floor.append(any(appart))
            floors.append(floor)
            floor_num += 1
        except:
            break
    floors.reverse()
    for i in range(len(floors)):
        for j in range(res['flats_count']['data']):
            if floors[i][j] == True:
                result.append((i)*res['flats_count']['data'] + j+1) 
    return [len(result), result]

# Заголовок веб-приложения
st.title('Визуализация результатов функции')

# Получение даты от пользователя
date = st.text_input('Введите дату в формате ГГГГ-ММ-ДД (например, 2024-03-31):')

# Проверка, была ли введена дата
if date:
    # Получение результатов функции
    result = get_by_date(date)
    
    # Вывод результатов
    st.write(f"Количество квартир с необходимыми ресурсами: {result[0]}")
    st.write(f"Номера квартир с необходимыми ресурсами: {result[1]}")
    
    # Визуализация комнат в каждой квартире
    st.write("Визуализация комнат в каждой квартире:")
    floors = result[2]  # Получение floors из результата
    for i, flat_number in enumerate(result[1], start=1):
        st.write(f"Квартира №{flat_number}")
        for j, room in enumerate(floors[flat_number - 1], start=1):
            st.write(f"Комната {j}: {room}")
else:
    st.write('Пожалуйста, введите дату для получения результатов.')
