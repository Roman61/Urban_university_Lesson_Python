from unittest import TestCase, main

from homework1 import Runner_2
import logging


def run():
    try:
        runner = Runner_2(speed="Усэйн", name=10)
        for i in range(10):
            runner.run()
        logging.info(f"Successful test runner, name - Усэйн")
    except ValueError as ve:
        logging.error(msg=f"fail test runner, name - Усэйн", exc_info=True)
    except TypeError as te:
        logging.error(msg=f"fail test runner, name - Усэйн", exc_info=True)


def walk():
    try:
        runner = Runner_2(name="Ник", speed=-3)
        for i in range(10):
            runner.walk()
        logging.info(f"Successful test runner, name - Ник")
    except ValueError as ve:
        logging.error(msg=f"fail test runner, name - Ник", exc_info=True)
    except TypeError as te:
        logging.error(msg=f"fail test runner, name - Ник", exc_info=True)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, encoding="UTF-8", filemode="w", filename="runner_tests.log",
                        format="%(asctime)s | %(levelname)s | %(message)s")
    run()
    walk()
