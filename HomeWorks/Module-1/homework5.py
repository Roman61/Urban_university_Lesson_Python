# - Создайте переменную my_list иHприсвойте ей список из нескольких элементов, например, фруктов.
my_list = ["Малина","Клубника","Клюква","Ежевика","Крыжовник","Брусника"]
# - Выведите на экран список my_list.
print("Элементы списка: " + str(my_list))
# - Выведите на экран первый и последний элементы списка my_list.
print("Первый элемент списка: " + str(my_list[0:1])+"\n"+"Последний элемент списка: " +str(my_list[:len(my_list)-2:-1]))
# - Выведите на экран подсписок my_list с третьего до пятого элементов.
print("Элементы списка с третьего до пятого: " + str(my_list[2:5]))
# - Измените значение третьего элемента списка my_list.
my_list[2] = "Арбуз"
# - Выведите на экран измененный список my_list.
print("Обновлён третий элемент списка: " + str(my_list))
print()
# - Создайте переменную my_dict и присвойте ей словарь с парами ключ-значение, например, переводами некоторых слов.
my_dict = {"вход": ["entry", "entrance", "login", "inlet", "admission", "door", "gate", "ingress", "gateway"], "входить": ["enter", "login", "go in", "come in", "walk in", "get in", "enter into", "go into"], "входной": ["input", "entrance", "inlet", "entry"], "вхождение": ["occurrence", "entry", "entrance", "ingoing"], "вхожий": ["enter"], "бдение": ["vigil", "wakefulness"], "бдительность": ["vigilance", "alertness", "look-out"], "бдительный": ["vigilant", "alert", "watchful", "awake", "waking", "wakeful", "unsleeping", "unwinking"]}
# - Выведите на экран словарь my_dict.
print("Словарь: " +str(my_dict))
# - Выведите на экран значение для заданного ключа в my_dict.
print("Перевод слова - вход: " +str(my_dict["вход"]))
# - Измените значение для заданного ключа или добавьте новый в my_dict.
my_dict["кабина"] = ["cabin", "booth", "cage", "cope", "cab", "cockpit", "cubicle", "nacelle"]
# - Выведите на экран измененный словарь my_dict.
print("Словарь обновлён: " +str(my_dict))
print("Добавлено слово кабина и его перевод: " +str(my_dict["кабина"]))