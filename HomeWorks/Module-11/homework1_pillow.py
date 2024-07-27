from PIL import Image

image_path = 'H:/Image/8blmpyIqFQ4.jpg'

img = Image.open(image_path)
# получаем ширину и высоту
width, height = img.size
print(width, height)
# открываем картинку в окне
img.show()

img = Image.open(image_path)
# изменяем размер
new_image = img.resize((200, 385))
new_image.show()

# указываем фиксированный размер стороны
fixed_width = 200
img = Image.open(image_path)
# получаем процентное соотношение
# старой и новой ширины
width_percent = (fixed_width / float(img.size[0]))
# на основе предыдущего значения
# вычисляем новую высоту
height_size = int((float(img.size[0]) * float(width_percent)))
# меняем размер на полученные значения
new_image = img.resize((fixed_width, height_size))
new_image.show()
new_image.save('H:/Image/8blmpyIqFQ4-2.jpg')

img = Image.open(image_path)
size = img.size
width, height = img.size
# обрезаем картинку
new_image = img.crop((0, 0, width, height - 60))
new_image.show()
new_image.save('H:/Image/8blmpyIqFQ4-3.jpg')

old_img = Image.open(image_path)
# создание нового изображения
new_image = Image.new(old_img.mode,
                      (old_img.size[0] + 50, old_img.size[1] + 50),
                      'white')
# вставляем старой изображение в новое
new_image.paste(old_img, (25, 25))
new_image.show()
new_image.save('H:/Image/8blmpyIqFQ4-4.jpg')
