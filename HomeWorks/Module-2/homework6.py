
list_ = ["Second"]
dict_ = {"second": 22}


def print_params(second):
    print(str(second)*2)


print_params("SECOND")
print_params(2)
print_params(*list_)
print_params(**dict_)
pass

