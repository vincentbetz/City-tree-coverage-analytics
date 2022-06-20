'''
function to download relevant mapbox raster tiles to directory.

'''


import requests
import os

# dictionary for all cities boundaries

cities_dict = { 'Tallinn': {'range_down': {'start': 18938, 'stop': 19000},
                               'range_side': {'start': 37287, 'stop': 37357}},
                'Vienna': {'range_down': {'start': 24486, 'stop': 24496},
                            'range_side': {'start': 36370, 'stop': 36380}},
                'Helsinki': {'range_down': {'start': 18938, 'stop': 19000},
                                 'range_side': {'start': 37287, 'stop': 37357}},
                'Dnipro': {'range_down' : {'start': 22631, 'stop': 22676},
                                'range_side' : {'start': 39133, 'stop': 39164}},
                'Reykjavik' : {'range_down' : {'start': 17413, 'stop': 17427},
                                'range__side' : {'start': 28770, 'stop': 28790}},
                'Athens' : {'range_down' : {'start': 25278, 'stop': 25287},
                                'range_side' : {'start': 37083, 'stop': 37093}}
                }


def download_tiles(city_boundary):
    # get al the relevant tiles in a list

    tiles_list = []
    for i in range(city_boundary['range_down']['start'], city_boundary['range_down']['stop']+1):
        for t in range(city_boundary['range_side']['start'], city_boundary['range_side']['stop']+1):
            tile = f'{z}/{t}/{i}'
            tiles_list.append(tile)

    for tile in tiles_list:
        url = f'https://api.mapbox.com/v4/mapbox.satellite/{tile}@2x.jpg90?access_token=pk.eyJ1IjoidGVhdHJhY2tzIiwiYSI6ImNrbnRlN3k5NDAyN3EydnFuaXg2aGp3NzEifQ.uC0Ngof314d22vpTA1dxtQ'
        response = requests.get(url)
        name_tile = tile.replace('/', '_')
        file = open(f"{name_tile}.jpg", "wb")
        file.write(response.content)
        file.close()

if __name__ == "__main__":
    # specify directory
    directory = "/Users/lucie/Documents/PycharmProjects/DataAnalytics/data/"
    os.chdir(directory)

    text = str('Which station do you want to use?\n' +
                'Athens  \n  ' +
                'Dnipro \n ' +
                'Hamburg \n ' +
                'Helsinki \n ' +
                'Reykjavik \n ' +
                'Tallinn \n ' +
                'Tirana \n ' +
                'Turin \n ' +
                'Vienna \n ' +
                'Zürich \n ' +
                'Type name to download a specific city only or type ALL to download all stations: ')
    city = str(input(text))

    city_list = ['Athens', 'Dnipro', 'Hamburg', 'Helsinki', 'Reykjavik', 'Tallinn', 'Tirana',
                'Turin', 'Vienna', 'Zürich']

    if city == 'ALL':
        for c in city_list:
            city_boundary = cities_dict[c]

    else:
        city_boundary = cities_dict[city]

