from PIL import Image
from collections import Counter
import os
import glob


#path = "response-2.jpeg"

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

# Data directory
dir_name = os.getcwd()   # current working directory
directory = os.path.join(dir_name, 'detectree_example/data/munich_response')

# /Users/benny/PycharmProjects/Detectree3/detectree-example/data/munich_response

# creates the data directory if needed --> data folder
if not os.path.exists(directory):
    os.makedirs(directory)


list_names = list()
object = os.scandir(directory)
print("Files and Directories in '% s':" % directory)
for n in object :
    if n.is_dir() or n.is_file():
        #print(n.name)
        list_names.append(n.name)
object.close()

#print(len(list_names))

percent_list = list()
for i in range(len(list_names)):
    result_temp = pixel_color(f"{directory}/{list_names[i]}")
    percent_list.append(result_temp)

mean = round(sum(percent_list)/len(percent_list), 3)
print(mean)

#print(len(percent_list))

print(percent_list)

