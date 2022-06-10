import requests
import os

# ------------
# for Hamburg
# ------------
directory = "/Users/lucie/Documents/PycharmProjects/DataAnalytics/data/hamburg/hamburg_raw"
os.chdir(directory)

# specify boundary - left upper, left lower, right upper, right lower
boundary_hamburg = {'left_upper': '16/37083/25278', 'left_lower': '16/37083/25287', 'right_upper': '16/37093/25278', 'right_lower': '16/37093/25287'}
range_hamburg_down = {'start': 25278, 'stop': 25287}
range_hamburg_side = {'start': 37083, 'stop': 37093}
z = 16  # zoom

# get al the relevant tiles in a list
tiles_list = []
for i in range(range_hamburg_down['start'], range_hamburg_down['stop']+1):
    for t in range(range_hamburg_side['start'], range_hamburg_side['stop']+1):
        tile = f'{z}/{t}/{i}'
        tiles_list.append(tile)

for tile in tiles_list:
    url = f'https://api.mapbox.com/v4/mapbox.satellite/{tile}@2x.jpg90?access_token=pk.eyJ1IjoidGVhdHJhY2tzIiwiYSI6ImNrbnRlN3k5NDAyN3EydnFuaXg2aGp3NzEifQ.uC0Ngof314d22vpTA1dxtQ'
    response = requests.get(url)
    name_tile = tile.replace('/', '_')
    file = open(f"{name_tile}.jpg", "wb")
    file.write(response.content)
    file.close()
