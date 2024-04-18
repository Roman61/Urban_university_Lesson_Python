immutable_var = ("Ванесса",  24, "Женский")
mutable_list = ["Полиция","Съемная квартира", False]

print('Персонаж книги "Архимаг"' + "\n")
print("Имя: "+immutable_var[0]+"\n"+"Возраст: " + str(immutable_var[1]) + "\n" + "Пол: " + str(immutable_var[2]) + "\n")

print('В начале книги: ')
print("Место работы: "+mutable_list[0]+"\n"+"Место жительства: " + mutable_list[1])
if mutable_list[2]:
    print("Является студентом: Да")
else:
    print("Является студентом: Нет")

print("\n" + 'Изменение по сюжету: ')

mutable_list[0] = "Отсутствует"
mutable_list[1] = "Коцебу"
mutable_list[2] = True
try:
    immutable_var[1] = immutable_var[1]+1
    print("В следующем году исполниться: "+str(immutable_var[1]))
except TypeError:
    print("Некрректная операция, изменение значений в кортеже невозможно!")
print("Место работы: "+mutable_list[0]+"\n"+"Место жительства: " + mutable_list[1])
if mutable_list[2]:
    print("Является студентом: Да")
else:
    print("Является студентом: Нет")