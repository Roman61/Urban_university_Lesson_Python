from unittest import TestCase
from rt_with_exceptions import Runner, Tournament


class TournamentTest(TestCase):
    @classmethod
    def setUpClass(self):
        self.all_results = []

    @classmethod
    def setUp(self):
        self.runner_y = Runner("Усэйн", 10)
        self.runner_a = Runner("Андрей", 9)
        self.runner_n = Runner("Ник", 3)

    @classmethod
    def tearDownClass(self):
        print()
        for i in self.all_results:
            print(i)
        pass

    def test_tournament_1(self):
        tournament = Tournament(90, *(self.runner_a, self.runner_n))
        results = tournament.start()
        self.all_results.append(results)
        self.assertTrue(results[2].name, self.runner_n.name)

    def test_tournament_2(self):
        tournament = Tournament(90, *(self.runner_y, self.runner_n))
        results = tournament.start()
        self.all_results.append(results)
        self.assertTrue(results[2].name, self.runner_n.name)

    def test_tournament_3(self):
        tournament = Tournament(90, *(self.runner_y, self.runner_a, self.runner_n))
        results = tournament.start()
        self.all_results.append(results)
        self.assertTrue(results[2].name, self.runner_n.name)

    def test_tournament_multi(self):
        print()
        results = []
        for _ in range(2):
            tournament = Tournament(90, *(self.runner_y, self.runner_a, self.runner_n))
            results.append(tournament.start())
            self.setUp()
            print(results)
            if len(results) > 1:
                first = results[0]
                first_last_key = list(first.keys())
                first_last_key = first_last_key[len(first_last_key) - 1]
                second = results[len(results)-1]
                second_last_key = list(second.keys())
                second_last_key = second_last_key[len(second_last_key)-1]

                self.assertEqual(first[first_last_key].name, second[second_last_key].name)
