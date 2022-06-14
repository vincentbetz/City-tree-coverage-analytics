from PIL import Image
from collections import Counter
import os
import random


def pixel_color(path1):
    img = Image.open(path1)
    w, h = img.size
    data = img.load()

    colors = []
    for x in range(w):
        for y in range(h):
            color = data[x, y]
            #hex_color = '#'+''.join([hex(c)[2:].rjust(2, '0') for c in color])
            colors.append(color)

    count = Counter(colors)
    #print(count)
    white = count[255]
    black = count[0]

    sum_all = white + black
    percent = round((white/sum_all)*100, 5)

    return percent


def directory(a_str):
    dir_name = os.getcwd()   # current working directory
    directory = os.path.join(dir_name, a_str)

    # /Users/benny/PycharmProjects/Detectree3/detectree-example/data/munich_response

    # creates the data directory if needed --> data folder
    if not os.path.exists(directory):
        os.makedirs(directory)

    return directory


if __name__ == "__main__":
    
    directory = directory('detectree_example/data/munich_response')
    list_names = list()
    object = os.scandir(directory)
    print("Files and Directories in '% s':\n" % directory)
    for n in object :
        if n.is_dir() or n.is_file():
            list_names.append(n.name)
    object.close()

    percent_list = list()
    dict_low = dict()
    dict_high = dict()
    for i in range(len(list_names)):
        result_temp = pixel_color(f"{directory}/{list_names[i]}")
        percent_list.append(result_temp)
        if result_temp < 20:
            dict_low[i] = result_temp
        elif result_temp > 60:
            dict_high[i] = result_temp
    print(dict_low)
    print(dict_high)

    value_low = list()
    value_high = list()
    for i in range(1):
        if len(dict_low) >= 1:
            value_low = list_names[random.choice(list(dict_low.keys()))]
        if len(dict_high) >= 1:
            value_high = list_names[random.choice(list(dict_high.keys()))]
    print(f"For low tree coverage the following random tiles are choosen: {value_low}")
    print(f"For low high coverage the following random tiles are choosen: {value_high}\n")

    mean = round(sum(percent_list)/len(percent_list), 3)
    print(f"The mean tree coverage in all tiles is {mean}\n")

    #print(len(percent_list))
    print("List of tree coverage percentages of all tiles: ")
    print(percent_list)
