def draw(
        arena_,
        background_char=" ",
        border_up=3,
        border_down=3,
        border_left=10,
        border_right=10
):
    for i in range(0, border_up):
        print(background_char * border_left + background_char * len(arena_[0]) + background_char * border_right)
    i, j = 0, 0
    str_ = ""
    while i < len(arena_[0]):
        while j < len(arena_[0]):
            str_ += arena_[i][j]
            j += 1
        i += 1
        j = 0
        print(background_char * border_left + str_ + background_char * border_right)
        str_ = ""
    for i in range(0, border_down):
        print(background_char * border_left + background_char * len(arena_[0]) + background_char * border_right)


def init(width=3, height=3, default_char="*"):
    temp1 = []
    if width % 2 == 1 and height % 2 == 1:
        temp2 = []
        for i in range(0, width):
            for j in range(0, height):
                temp2.append(default_char)
            temp1.append(temp2.copy())
            temp2.clear()
    return temp1


arena = []
step = 0
step_char = ""
victory = False