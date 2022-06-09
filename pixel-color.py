from PIL import Image
from collections import Counter
import prettytable

path = "response-2.jpeg"

img = Image.open(path)
size = w, h = img.size
data = img.load()

colors = []
for x in range(w):
    for y in range(h):
        color = data[x, y]
        #hex_color = '#'+''.join([hex(c)[2:].rjust(2, '0') for c in color])
        colors.append(color)

count = Counter(colors)
print(count)
white = count[255]
black = count[0]

percent = round(white/black, 3)
print("Percentage of tree coverage:", "{0:.1%}".format(percent))

# Analyze color value and corresponding frequency

# pt = prettytable.PrettyTable(["Color", "Count"])
#
# for color, count in Counter(colors).items():
#     pt.add_row([color, count])
#
# for row in pt:
#       row.border = False
#       row.header = False
#       print (row.get_string(fields=["Count"]).strip())
#
#
# print(pt)

