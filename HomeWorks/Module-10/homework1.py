import datetime
from threading import Thread
from time import sleep


def write_words(word_count, file_name, encoding='WINDOWS-1251'):
    with open(file_name, mode='a+') as file:
        for i in range(0, word_count - 1):
            file.write(f"Какое-то слово № {i}\n")
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")


time_start = datetime.datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
time_stop = datetime.datetime.now()
time_result = time_stop - time_start
print(time_result)

time_start = datetime.datetime.now()
th1 = Thread(target=write_words, args=(10, 'example5.txt',))
th2 = Thread(target=write_words, args=(30, 'example6.txt',))
th3 = Thread(target=write_words, args=(200, 'example7.txt',))
th4 = Thread(target=write_words, args=(100, 'example8.txt',))
th1.start()
th2.start()
th3.start()
th4.start()
th1.join()
th2.join()
th3.join()
th4.join()
time_stop = datetime.datetime.now()
time_result = time_stop - time_start
print(time_result)
