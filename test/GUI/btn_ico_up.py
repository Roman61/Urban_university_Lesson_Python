from PyQt5 import QtSvg, QtCore, QtGui
# from SvgToPng import SvgToPng


class Up:#(SvgToPng):
    '''
    example use
    from GUI.btn_ico_up import btn_ico_up
    self.lbl_info_ico.setPixmap(btn_ico_up().get_pixmap())
    '''

    def __init__(self):
        super().__init__()
        self._src = '''<?xml version="1.0" encoding="UTF-8"?>
            <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
            <svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="153px" height="153px" style="shape-rendering:geometricPrecision; text-rendering:geometricPrecision; image-rendering:optimizeQuality; fill-rule:evenodd; clip-rule:evenodd" xmlns:xlink="http://www.w3.org/1999/xlink">
            <g><path style="opacity:0.195" fill="#7bcefd" d="M 71.5,35.5 C 78.2687,34.7507 84.602,35.9174 90.5,39C 106.729,54.5602 122.229,70.7268 137,87.5C 142.481,111.352 133.314,120.519 109.5,115C 98.6547,104.821 87.8214,94.654 77,84.5C 66.5361,95.2959 55.7028,105.796 44.5,116C 34.8059,119.326 26.3059,117.493 19,110.5C 14.3333,101.833 14.3333,93.1667 19,84.5C 31.8039,70.6955 44.9706,57.1955 58.5,44C 62.2938,40.1183 66.6271,37.2849 71.5,35.5 Z"/></g>
            <g><path style="opacity:0.706" fill="#7bd0ef" d="M 81.5,43.5 C 81.8966,42.475 82.5632,42.3083 83.5,43C 99.7113,58.6995 115.045,74.5328 129.5,90.5C 113.833,75.1667 98.1667,59.8333 82.5,44.5C 82.5,43.8333 82.1667,43.5 81.5,43.5 Z"/></g>
            <g><path style="opacity:1" fill="#002c74" d="M 81.5,43.5 C 82.1667,43.5 82.5,43.8333 82.5,44.5C 97.1108,60.7856 112.777,76.7856 129.5,92.5C 133.191,104.277 128.858,109.777 116.5,109C 106.963,99.9603 97.2964,91.1269 87.5,82.5C 84.2039,78.7024 80.7039,75.0357 77,71.5C 68.9642,79.3684 61.1309,87.3684 53.5,95.5C 49.7312,99.7712 45.7312,103.938 41.5,108C 33.5179,111.596 27.6846,109.429 24,101.5C 22.8899,96.9778 23.7233,92.9778 26.5,89.5C 41.4998,76.1746 56.1665,61.8413 70.5,46.5C 70.9528,45.5416 71.6195,44.7083 72.5,44C 75.4816,43.502 78.4816,43.3354 81.5,43.5 Z"/></g>
            <g><path style="opacity:1" fill="#001863" d="M 82.5,44.5 C 98.1667,59.8333 113.833,75.1667 129.5,90.5C 129.5,91.1667 129.5,91.8333 129.5,92.5C 112.777,76.7856 97.1108,60.7856 82.5,44.5 Z"/></g>
            <g><path style="opacity:1" fill="#011864" d="M 70.5,46.5 C 56.1665,61.8413 41.4998,76.1746 26.5,89.5C 40.5514,74.4476 55.2181,60.1143 70.5,46.5 Z"/></g>
            <g><path style="opacity:0.875" fill="#86dcf7" d="M 87.5,82.5 C 83.5977,80.1074 80.0977,77.1074 77,73.5C 69.3019,81.7224 61.4685,89.0557 53.5,95.5C 61.1309,87.3684 68.9642,79.3684 77,71.5C 80.7039,75.0357 84.2039,78.7024 87.5,82.5 Z"/></g>
            </svg>
        '''
    def get_pixmap(self):
        # Загрузка SVG-кода
        renderer = QtSvg.QSvgRenderer()
        renderer.load(QtCore.QByteArray(self._src.encode()))

        # Создание пиксмапа из SVG-кода
        pixmap = QtGui.QPixmap(464, 371)
        pixmap.fill(QtCore.Qt.transparent)
        painter = QtGui.QPainter(pixmap)
        renderer.render(painter)
        painter.end()
        return pixmap
