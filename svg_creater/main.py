import fnmatch
import os
import xml.etree.ElementTree as ET

from color_convert import color
from tqdm.auto import tqdm

import rich

listOfFiles = os.listdir('.')
pattern = "*.svg"
file_list = {}
for entry in listOfFiles:
    if fnmatch.fnmatch(entry, pattern):
        file_list[entry] = os.path.abspath(entry)

for i in file_list:
    print(i)


def rgb(r, g, b):
    return r, g, b


def gen_func(collection):
    for elem in tqdm(collection, desc='Готовность'):
        rgb_ = color.hex_to_rgb(elem.attrib['fill'])
        r, g, b = eval(rgb_)

        yield {'R': r, 'G': g, 'B': b}


# for root, dirs, files in os.walk("."):
#     for filename in files:
#         print(filename)


# path_ = input()
# color_list = input("Введите массив цветов в формате [(R1,G1,B1),(R2,G2,B2),...,(Rn,Gn,Bn)]: ")

tree = ET.parse('drawings - color - 44000.svg')  # drawings - color - 44000.svg
root = tree.getroot()

collect = (root.findall('circle'))

gf1 = gen_func(collect)
tasks = [gf1]
while tasks:
    task = tasks.pop(0)

    try:
        i = next(task)
        tasks.append(task)
    except StopIteration:
        pass
