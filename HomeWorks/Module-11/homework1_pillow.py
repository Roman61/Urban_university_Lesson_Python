from PIL import Image

image_path = 'H:/Image/8blmpyIqFQ4.jpg'

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
