import requests
import os

# ------------
# for vienna
# ------------
directory = "/Users/lucie/Documents/PycharmProjects/DataAnalytics/data/vienna/vienna_raw"
os.chdir(directory)

# specify boundary - left upper, left lower, right upper, right lower
boundary_turin = {'left_upper': '16/34155/23545', 'left_lower': '16/34155/23568', 'right_upper': '16/34163/23545', 'right_lower': '16/34163/23568'}
range_turin_down = {'start': 23545, 'stop': 23568}
range_turin_side = {'start': 34155, 'stop': 34163}
z = 16  # zoom

# get al the relevant tiles in a list
tiles_list = []
for i in range(range_turin_down['start'], range_turin_down['stop']+1):
    for t in range(range_turin_side['start'], range_turin_side['stop']+1):
        tile = f'{z}/{t}/{i}'
        tiles_list.append(tile)

for tile in tiles_list:
    url = f'https://api.mapbox.com/v4/mapbox.satellite/{tile}@2x.jpg90?access_token=pk.eyJ1IjoidGVhdHJhY2tzIiwiYSI6ImNrbnRlN3k5NDAyN3EydnFuaXg2aGp3NzEifQ.uC0Ngof314d22vpTA1dxtQ'
    response = requests.get(url)
    name_tile = tile.replace('/', '_')
    file = open(f"{name_tile}.jpg", "wb")
    file.write(response.content)
    file.close()
