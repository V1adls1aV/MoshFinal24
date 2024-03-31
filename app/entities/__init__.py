'''
Module for calculation-oriented entities.
Like Ship class with estimation of required resources 
for the specific route.
'''
import requests
def get_by_date(date:str) -> list:
    date = date.split('-')
    res = r = requests.get(f'https://olimp.miet.ru/ppo_it_final?day={date[0]}&month={date[1]}&year={date[2]}', headers= {
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
    floors.reverse
    for i in range(len(floors)):
        for j in range(res['flats_count']['data']):
            if floors[i][j] == True:
                result.append((i)*res['flats_count']['data'] + j+1) 
    return [len(result), result]