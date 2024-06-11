import time

from UrTube import UrTube
from practice.UrTube.Video import Video


def watch_video(film_str):
    """
        Метод watch_video, который принимает название фильма, если не находит точного совпадения(вплоть до пробела),
         то ничего не воспроизводится, если же находит ведётся отчёт в консоль на какой секунде ведётся просмотр.
         После текущее время просмотра данного видео сбрасывается.

        Для метода watch_video так же следует учитывать следущие особенности:
        Для паузы между выводами секунд воспроизведения можно использовать функцию sleep из модуля time.
        Воспроизводить видео можно только тогда, когда пользователь вошёл в UrTube. В противном случае выводить в
        консоль надпись: "Войдите в аккаунт чтобы смотреть видео"
        Если видео найдено, следует учесть, что пользователю может быть отказано в просмотре, т.к. есть ограничения
        18+. Должно выводиться сообщение: "Вам нет 18 лет, пожалуйста покиньте страницу"
        После воспроизведения нужно выводить: "Конец видео"

        :return:
    """
    global ur
    if ur.current_user is None:
        print("Войдите в аккаунт чтобы смотреть видео")
        return
    video: Video = None
    for i in ur.videos:
        if film_str == i.title:
            video = i
            break
    if video is None:
        # print("Видео не найдено")
        return
    if video.adult_mode == True and ur.current_user.age <= 18:
        print("Вам нет 18 лет, пожалуйста покиньте страницу")
        return

    while video.time_now < video.duration:
        print(f"{video.time_now}", end=' ')
        time.sleep(1)
        video.time_now += 1
    else:
        print("Конец видео")
        video.time_now = 0

    return ''


def main():
    pass


if __name__ == '__main__':
    # main()
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    watch_video('Лучший язык программирования 2024 года!')