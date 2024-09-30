from PyQt5 import QtSvg, QtCore, QtGui
# from SvgToPng import SvgToPng


class Back:#(SvgToPng):
    '''
    example use
    from GUI.btn_ico_back import btn_ico_back
    self.lbl_info_ico.setPixmap(btn_ico_back().get_pixmap())
    '''

    def __init__(self):
        super().__init__()
        self._src = '''<?xml version="1.0" encoding="UTF-8"?>
            <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
            <svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="153px" height="153px" style="shape-rendering:geometricPrecision; text-rendering:geometricPrecision; image-rendering:optimizeQuality; fill-rule:evenodd; clip-rule:evenodd" xmlns:xlink="http://www.w3.org/1999/xlink">
            <g><path style="opacity:0.18" fill="#ff2322" d="M 106.5,25.5 C 127.014,26.5445 134.847,37.2112 130,57.5C 124.908,64.5963 119.074,71.0963 112.5,77C 118.366,82.5313 123.866,88.3647 129,94.5C 135.49,120.339 125.657,131.172 99.5,127C 97.2746,126.439 95.2746,125.439 93.5,124C 88.9782,119.478 84.4782,114.978 80,110.5C 74.5438,114.954 69.3772,119.787 64.5,125C 54.6059,129.885 44.9392,129.551 35.5,124C 27.4155,113.737 26.5821,102.904 33,91.5C 37.8799,86.9558 42.3799,82.1225 46.5,77C 41.3464,71.1783 36.1798,65.3449 31,59.5C 24.7039,35.4678 33.8706,24.6344 58.5,27C 61.9518,27.8917 64.9518,29.5584 67.5,32C 71.6816,36.3487 76.0149,40.5154 80.5,44.5C 86.3187,39.1816 91.9854,33.6816 97.5,28C 100.628,27.1588 103.628,26.3254 106.5,25.5 Z"/></g>
            <g><path style="opacity:1" fill="#ff5454" d="M 46.5,33.5 C 50.7924,33.0349 54.7924,33.8682 58.5,36C 65.9839,42.6498 73.3172,49.4831 80.5,56.5C 88.3492,48.8168 96.3492,41.3168 104.5,34C 114.051,31.893 120.551,35.393 124,44.5C 124.652,47.594 124.318,50.594 123,53.5C 115.82,61.3451 108.654,69.1784 101.5,77C 109.026,84.8587 116.193,93.0254 123,101.5C 124.253,117.576 117.086,123.41 101.5,119C 94.6242,111.789 87.4575,104.956 80,98.5C 72.876,104.622 66.0427,111.122 59.5,118C 52.0308,121.937 45.1975,121.104 39,115.5C 36.2345,110.289 35.9011,104.956 38,99.5C 45.5314,92.303 52.6981,84.803 59.5,77C 51.2632,69.4333 43.7632,61.2666 37,52.5C 35.3994,43.701 38.5661,37.3676 46.5,33.5 Z"/></g>
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
