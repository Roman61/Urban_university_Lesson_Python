
muls1 = list()
muls2 = list(range(c, d))
output = []

# print(' ', *muls2)
# str_ += "".join(str(element) for element in muls2)
# str_ = " " + string.join(first)
# output.append(str_)
for i in muls1:
    common = []
    first_space = 0
    for j in muls2:
        space = (len(str(muls1[len(muls1) - 1] * j)) - len(str(i * j)))
        common.append(space * " " + str(i * j))
    common.insert(0, str(i) + ":")
    output.append(common)

first = output[0]
lignt = len(first[0])
muls1.insert(0, -1)
# for i in zip(a, b):
#    print(i, type(i)) -> (10, 'a') <class 'tuple'>

# list(map(string.capwords, my_string)
# ... ['T', 'P', 'R', 'O', 'G', 'E', 'R']for key, el in enumerate(muls1)
# [f(num) for num in nums]
temp = list(map((lambda el, key: el), zip(first, muls1)))
# [f(num) for num in zip(first, muls1)]

for k in output:
    print(k)
