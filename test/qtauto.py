import sys
from PyQt5 import QtWidgets, QtCore
from screen_1_welcome import Ui_screen_1_welcome
from screen_2_Help import Ui_screen_2_Help
from screen_3_authorization import Ui_screen_3_authorization

# Словарь, содержащий названия экранов и соответствующие им кнопки
screen = {
    "screen_1_welcome": ['btn_help', 'btn_authorization'],
    "screen_2_Help": ['btn_up', 'btn_back', 'btn_down'],
    "screen_3_authorization": ['btn_back', 'btn_authorization', 'btn_keyboard']
}

# Словарь, содержащий информацию о переходах между экранами
transitions = [
    {'trigger': 'btn_authorization', 'source': 'screen_1_welcome', 'dest': 'screen_3_authorization'},
    {'trigger': 'btn_help', 'source': 'screen_1_welcome', 'dest': 'screen_2_Help'},
    {'trigger': 'btn_back', 'source': 'screen_2_Help', 'dest': 'screen_1_welcome'},
    {'trigger': 'btn_back', 'source': 'screen_3_authorization', 'dest': 'screen_1_welcome'}
]


# Класс, который отвечает за отображение виджетов
class MainWindowEvent(QtCore.QObject):
    show_widget = QtCore.pyqtSignal(str)


# Главное окно приложения
class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")
        self.resize(480, 800)

        # Словарь для хранения виджетов экранов
        self.widgets = {}
        # Словарь для хранения сигналов кнопок
        self.button_signals = {}

        # Создание вертикального layout для окна
        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)

        # Создание объекта для отображения виджетов
        self.event = MainWindowEvent()
        self.event.show_widget.connect(self.show_widget)

        # Создание виджетов экранов
        self.create_widgets()

        # Отображение первого экрана
        self.show_widget('screen_1_welcome')

    # Метод, который создает виджеты для всех экранов
    def create_widgets(self):
        for screen_name, buttons in screen.items():
            # Создание виджета для текущего экрана
            widget = self.create_widget(screen_name)
            # Добавление виджета в словарь
            self.widgets[screen_name] = widget
            # Добавление виджета в layout окна
            self.layout.addWidget(widget)

        # Связывание кнопок с переходами между экранами
        for transition in transitions:
            trigger = transition['trigger']
            source = transition['source']
            dest = transition['dest']
            if source in self.widgets:
                self.bind_button_signal(source, trigger, dest)

    # Метод, который создает виджет для конкретного экрана
    def create_widget(self, screen_name):
        widget = QtWidgets.QWidget()
        # Создание объекта UI для текущего экрана
        ui_class = getattr(sys.modules[__name__], f"Ui_{screen_name}")
        ui = ui_class()
        ui.setupUi(widget)
        # Подключение кнопок на экране к обработчику нажатий
        self.find_and_connect_buttons(widget, ui)
        return widget

    # Метод, который находит все кнопки на экране и подключает их к обработчику
    def find_and_connect_buttons(self, widget, ui):
        buttons = widget.findChildren(QtWidgets.QPushButton)
        for button in buttons:
            button_name = button.objectName()
            button.clicked.connect(lambda checked, btn_name=button_name: self.button_clicked(btn_name))

    # Метод, который обрабатывает нажатие кнопок
    def button_clicked(self, button_name):
        print(f"Button '{button_name}' was clicked!")
        # Здесь можно добавить логику обработки нажатий кнопок

    # Метод, который связывает кнопки с переходами между экранами
    def bind_button_signal(self, source, trigger, dest):
        button = self.widgets[source].findChild(QtWidgets.QPushButton, trigger)
        if button:
            self.button_signals[button.objectName()] = button.clicked
            button.clicked.connect(lambda: self.event.show_widget.emit(dest))

    # Метод, который отображает нужный виджет, скрывая все остальные
    def show_widget(self, widget_name):
        for widget in self.widgets.values():
            widget.hide()
        for _, name in enumerate(self.widgets):
            if (str(name)).lower() == (str(widget_name)).lower():
                self.widgets[name].show()
                break


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
