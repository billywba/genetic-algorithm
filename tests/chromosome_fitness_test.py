import unittest

from src.chromosome import Chromosome

class ChromosomeFitnessTest(unittest.TestCase):
    def test_fitness(self):
        chromosome = Chromosome([1, 2, 3], 
                                ['Tutor1', 'Tutor2', 'Tutor3', 'Tutor4'], 
                                ['CIS311', 'CIS312', 'CIS313'])

        self.assertEqual(chromosome.evaluate_fitness(), 50)

    def test_fitness_invalid_tutor(self):
        chromosome = Chromosome([1, 2, 3], 
                                ['Tutor1', ''], 
                                ['CIS311', 'CIS312', 'CIS313'])

        self.assertEqual(chromosome.evaluate_fitness(), 40)

    def test_fitness_missing_unit_exam(self):
        chromosome = Chromosome([1], ['Tutor1'], ['CIS311'])

        # Add a new unit after the exam timetable has been scheduled
        chromosome.units = ['CIS311', 'CIS312']

        self.assertEqual(chromosome.evaluate_fitness(), 40)
