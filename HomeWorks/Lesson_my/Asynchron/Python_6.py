from inspect import getgeneratorstate


def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g

    return inner


class UserEventException(Exception):
    pass


@coroutine
def send_gen():
    x = 'Ready to accept message'
    message = yield x
    print('Subgen received: ', message)


@coroutine
def average():
    count = 0
    summ = 0
    average_ = None

    while True:
        try:
            x = yield average_
        except StopIteration:
            print('Done!')
            break
        else:
            count += 1
            summ += x
            average_ = round(summ / count, 2)

    return average_


@coroutine
def subgen():
    while True:
        try:
            message = yield
        except StopIteration:
            pass
        else:
            print('.......', message)

    # for i in 'Roman':
    #     yield i


@coroutine
def delegator(g):
    while True:
        try:
            data = yield
            g.send(data)
        except StopIteration:
            pass

    # for i in g:
    #     yield i


sg = subgen()
g = delegator(sg)
g.send('Ok')

# g = average()
# print(getgeneratorstate(g))
