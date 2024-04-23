
list_ = ["First", "Second"]
dict_ = {"first": 11, "second": 22}


def print_params(first, second):
    print(str(second)*2)


print_params("FIRST", "SECOND")
print_params(1, 2)
print_params(*list_)
print_params(**dict_)
pass

