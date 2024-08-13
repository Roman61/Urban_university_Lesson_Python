import unittest
from homework1 import RunnerTest
from homework2 import TournamentTest

runnerST = unittest.TestSuite()
runnerST.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
runnerST.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

runnerTTR = unittest.TextTestRunner(verbosity=2)
runnerTTR.run(runnerST)

