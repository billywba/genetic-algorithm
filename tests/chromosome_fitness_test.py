import unittest

from src.chromosome import Chromosome

class ChromosomeFitnessTest(unittest.TestCase):
    def test_fitness(self):
        chromosome = Chromosome([1, 2, 3], 
                                ['Tutor1', 'Tutor2', 'Tutor3', 'Tutor4'], 
                                ['CIS311', 'CIS312', 'CIS313'])

        self.assertEqual(chromosome.evaluate_fitness(), 10)
