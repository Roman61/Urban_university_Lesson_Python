import random

_holder = []
MAX_BUNCHES = 5


def put_stones():
    global _holder
    _holder = []
    for i in range(MAX_BUNCHES):
        _holder.append(random.randint(1, 20))


def take_frome_bunch(position, quantity):
    if _holder[position-1] < quantity:
        return
    if 1 <= position < len(_holder)+1:
        _holder[position-1] -= quantity


def get_bunches():
    return _holder


def is_gameover():
    return sum(_holder) <= 0
