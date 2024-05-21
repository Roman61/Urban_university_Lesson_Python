# import modul_1
# from modul_1 import syi_hi

from modul_1 import summ as syi
from modul_1 import sqrt, odd

a = 10

filter_ = filter(odd, range(1, 21))
map_ = map(sqrt, filter_)
print(list(map_))

# syi()
# print(globals())
# print(dir(modul_1))
