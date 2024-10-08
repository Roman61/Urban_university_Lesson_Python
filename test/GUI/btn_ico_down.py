from PyQt5 import QtSvg, QtCore, QtGui
# from SvgToPng import SvgToPng


class Down:#(SvgToPng):
    '''
    example use
    from GUI.btn_ico_down import btn_ico_down
    self.lbl_info_ico.setPixmap(btn_ico_down().get_pixmap())
    '''

    def __init__(self):
        super().__init__()
        self._src = '''<?xml version="1.0" encoding="UTF-8"?>
            <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
            <svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="153px" height="153px" style="shape-rendering:geometricPrecision; text-rendering:geometricPrecision; image-rendering:optimizeQuality; fill-rule:evenodd; clip-rule:evenodd" xmlns:xlink="http://www.w3.org/1999/xlink">
            <g><path style="opacity:0.195" fill="#7ccefd" d="M 113.5,35.5 C 134.443,35.0101 142.276,45.0101 137,65.5C 122.896,81.6062 108.062,97.1062 92.5,112C 85.702,117.189 78.0354,118.856 69.5,117C 67.2746,116.439 65.2746,115.439 63.5,114C 47.2712,98.4398 31.7712,82.2732 17,65.5C 11.8635,41.9698 21.0301,32.8032 44.5,38C 55.6374,48.1366 66.4707,58.6366 77,69.5C 87.1969,59.6372 97.0302,49.4706 106.5,39C 108.713,37.3838 111.047,36.2172 113.5,35.5 Z"/></g>
            <g><path style="opacity:0.71" fill="#7dd0f2" d="M 78.5,80.5 C 77.8826,80.6107 77.3826,80.944 77,81.5C 64.1956,69.6963 51.6956,57.5296 39.5,45C 35.3562,42.8624 31.3562,43.029 27.5,45.5C 26.2617,45.19 26.2617,44.69 27.5,44C 31.7955,40.8164 36.1288,40.8164 40.5,44C 52.7587,56.7621 65.4254,68.9287 78.5,80.5 Z"/></g>
            <g><path style="opacity:1" fill="#012c74" d="M 78.5,80.5 C 80.1667,79.5 81.5,78.1667 82.5,76.5C 88.5,70.1667 94.5,63.8333 100.5,57.5C 105.298,53.2033 109.965,48.7033 114.5,44C 121.704,42.3522 126.871,44.8522 130,51.5C 130.837,55.2946 130.504,58.9613 129,62.5C 114.5,78.3333 99.3333,93.5 83.5,108C 79.9743,109.337 76.3076,109.837 72.5,109.5C 71.5,109.167 70.8333,108.5 70.5,107.5C 56.2547,91.7521 41.4214,76.4188 26,61.5C 25.5939,58.2578 24.7605,55.2578 23.5,52.5C 23.9613,49.6967 25.2947,47.3634 27.5,45.5C 31.3562,43.029 35.3562,42.8624 39.5,45C 51.6956,57.5296 64.1956,69.6963 77,81.5C 77.3826,80.944 77.8826,80.6107 78.5,80.5 Z"/></g>
            <g><path style="opacity:0.749" fill="#7bd0f0" d="M 23.5,57.5 C 23.8923,59.1789 24.3923,60.8455 25,62.5C 40.0348,77.7018 55.2015,92.7018 70.5,107.5C 70.8333,108.5 71.5,109.167 72.5,109.5C 72.1034,110.525 71.4368,110.692 70.5,110C 55,94.5 39.5,79 24,63.5C 21.5919,59.8583 20.9252,55.8583 22,51.5C 22.1909,53.7078 22.6909,55.7078 23.5,57.5 Z"/></g>
            <g><path style="opacity:0.929" fill="#87e0fd" d="M 100.5,57.5 C 94.5,63.8333 88.5,70.1667 82.5,76.5C 81.475,76.1034 81.3083,75.4368 82,74.5C 88.0309,67.938 94.1976,62.2714 100.5,57.5 Z"/></g>
            <g><path style="opacity:1" fill="#001864" d="M 23.5,52.5 C 24.7605,55.2578 25.5939,58.2578 26,61.5C 41.4214,76.4188 56.2547,91.7521 70.5,107.5C 55.2015,92.7018 40.0348,77.7018 25,62.5C 24.3923,60.8455 23.8923,59.1789 23.5,57.5C 23.5,55.8333 23.5,54.1667 23.5,52.5 Z"/></g>
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