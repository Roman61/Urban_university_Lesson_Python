"""
    Общее ТЗ:
    Реализовать классы для взаимодействия с платоформой, каждый из которых будет содержать методы добавления видео,
    авторизации и регистрации пользователя и т.д.
"""
import time

from practice.UrTube.User import User
from practice.UrTube.Video import Video


class UrTube:
    """
        Примечания:
        Не забывайте для удобства использовать dunder(магические) методы: __str__, __repr__, __contains__, __eq__ и др.
        Чтобы не запутаться рекомендуется после реализации каждого метода проверять как он работает, тестировать разные
        вариации.
    """

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user: User = None

    def add(self, *video):
        """
            Метод add, который принимает неограниченное кол-во объектов класса Video и все добавляет в videos, если с таким
             же названием видео ещё не существует. В противном случае ничего не происходит.
            :param video:
            :return:
        """
        for i in video:
            if isinstance(i, Video) and i not in self.videos:
                self.videos.append(i)

    def get_videos(self, find_str):
        """
            Метод get_videos, который принимает поисковое слово и возвращает список названий всех видео, содержащих
            поисковое слово. Следует учесть, что слово 'UrbaN' присутствует в строке 'Urban the best'
            (не учитывать регистр).
            :param find_str:
            :return:
        """
        out_video = []
        for i in self.videos:
            if find_str.lower() in i.title.lower():
                out_video.append(i)

        return out_video

    def log_out(self):
        """
            Метод log_out для сброса текущего пользователя на None.
            :return:
        """
        self.current_user = None

    def log_in(self, login, password):
        """
            Метод log_in, который принимает на вход аргументы: login, password и пытается найти пользователя в users с
            такмими же логином и паролем. Если такой пользователь суещствует, то current_user меняется на найденного.
            Помните, что password передаётся в виде строки, а сравнивается по хэшу.
            :param login:
            :param password:
            :return:
        """
        for i in self.users:
            if i.nickname == login:
                if i.password_verify(password):
                    self.current_user = i
                    return True
                else:
                    return False
        pass

    def register(self, nickname, password, age):
        """
            Метод register, который принимает три аргумента: nickname, password, age, и добавляет пользователя в список,
            если пользователя не существует (с таким же nickname). Если существует, выводит на экран: "Пользователь
            {nickname} уже существует". После регистрации, вход выполняется автоматически.
            :param nickname:
            :param password:
            :param age:
            :return:
        """
        for i in self.users:
            if i.nickname == nickname:
                print(f"Пользователь {nickname} уже существует!")
                return False
        else:
            user = User(nickname, password, age)
            self.users.append(user)
            self.current_user = user
            print("Пользователь успешно зарегестрирован!")
            return True

