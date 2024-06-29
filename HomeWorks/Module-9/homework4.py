def all_variants(param):
    target = ''
    fixer = 0
    char_in_str = 1
    string_count = 0
    while True:
        if string_count - fixer > len(param) - char_in_str:
            fixer += len(param) - char_in_str + 1
            char_in_str += 1
        for index_char in range(string_count - fixer, string_count + char_in_str - fixer):
            if len(param) > index_char:
                target += param[index_char]
            else:
                return
        yield target
        target = ''
        string_count += 1


a = all_variants("abc")
for i in a:
    print(i)
