# import cairosvg
from PyQt5 import QtSvg, QtCore, QtGui


class SvgToPng:

    def __init__(self):
        self.src = ""

    def get_pixmap(self):
        # Загрузка SVG-кода
        renderer = QtSvg.QSvgRenderer()
        renderer.load(QtCore.QByteArray(self.src.encode()))

        # Создание пиксмапа из SVG-кода
        pixmap = QtGui.QPixmap(464, 371)
        pixmap.fill(QtCore.Qt.transparent)
        painter = QtGui.QPainter(pixmap)
        renderer.render(painter)
        painter.end()
        return pixmap

    # def svg_to_png(self) -> QtGui.QPixmap:
    #     # Загрузка SVG-кода
    #     renderer = QtSvg.QSvgRenderer()
    #     renderer.load(QtCore.QByteArray(self.src.encode()))
    #
    #     # Создание пиксмапа из SVG-кода
    #     pixmap = QtGui.QPixmap(464, 371)
    #     pixmap.fill(QtCore.Qt.transparent)
    #     painter = QtGui.QPainter(pixmap)
    #     renderer.render(painter)
    #     painter.end()
    #     return pixmap

# if __name__ == "__main__":
#     # Пример SVG-кода
#     svg_data = """
#     <svg width="100" height="100" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
#         <circle cx="50" cy="50" r="40" fill="#0077b6" />
#     </svg>
#     """
#
#     # Конвертируем SVG в PNG
#     png_data = cairosvg.svg2png(svg_data)
#
#     # Теперь вы можете сохранить или обработать PNG-изображение
#     with open("output.png", "wb") as f:
#         f.write(png_data)