import unittest
import random

from src.chromosome import Chromosome

class ChromosomeTest(unittest.TestCase):
    def test_generate_schedule(self):
        chromosome = Chromosome([['1', 'test_student', 'CIS312'], ['2', 'test_student2', 'CIS312'], ['3', 'test_student3', 'CIS312']], 
                                ['Tutor1', 'Tutor2', 'Tutor3', 'Tutor4'], 
                                ['CIS311', 'CIS312', 'CIS313'])

        self.assertEqual(len(chromosome.schedule), 10)

    def test_mutate(self):
        # Set seed to reproduce same results
        random.seed(42)
        
        chromosome = Chromosome([['1', 'test_student', 'CIS312'], ['2', 'test_student2', 'CIS312'], ['3', 'test_student3', 'CIS312']], 
                                ['Tutor1', 'Tutor2', 'Tutor3', 'Tutor4'], 
                                ['CIS311', 'CIS312', 'CIS313'])

        chromosome.schedule = [
                                ['P417', 'CIS311', 'Tutor5'],
                                ['P418', 'CIS312', 'Tutor3']
                            ]

        # Mutate with 100% probability
        chromosome.mutate(1)

        # Assert new schedule has changed evening unit (from CIS312 to CIS311)
        self.assertEqual(chromosome.schedule, [['P417', 'CIS311', 'Tutor5'], ['P412', 'CIS312', 'Tutor3']])
