import unittest

from src.chromosome import Chromosome

class ChromosomeTest(unittest.TestCase):
    def test_generate_schedule(self):
        chromosome = Chromosome([['1', 'test_student', 'CIS312'], ['2', 'test_student2', 'CIS312'], ['3', 'test_student3', 'CIS312']], 
                                ['Tutor1', 'Tutor2', 'Tutor3', 'Tutor4'], 
                                ['CIS311', 'CIS312', 'CIS313'])

        self.assertEqual(len(chromosome.schedule), 10)
