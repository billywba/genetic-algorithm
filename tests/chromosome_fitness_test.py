import unittest

from src.chromosome import Chromosome

class ChromosomeFitnessTest(unittest.TestCase):
    def test_fitness(self):
        chromosome = Chromosome([['1', 'test_student', 'CIS312'], ['2', 'test_student2', 'CIS312'], ['3', 'test_student3', 'CIS312']], 
                                ['Tutor1', 'Tutor2', 'Tutor3', 'Tutor4'], 
                                ['CIS311', 'CIS312', 'CIS313'])

        self.assertEqual(chromosome.evaluate_fitness(), 60)

    def test_fitness_invalid_tutor(self):
        chromosome = Chromosome([['1', 'test_student', 'CIS312'], ['2', 'test_student2', 'CIS312'], ['3', 'test_student3', 'CIS312']], 
                                ['Tutor1', ''], 
                                ['CIS311', 'CIS312', 'CIS313'])

        self.assertEqual(chromosome.evaluate_fitness(), 50)

    def test_fitness_missing_unit_exam(self):
        chromosome = Chromosome([['1', 'test_student', 'CIS312']], ['Tutor1'], ['CIS311'])

        # Add a new unit after the exam timetable has been scheduled
        chromosome.units.append('CIS312')

        self.assertEqual(chromosome.evaluate_fitness(), 50)

    def test_student_too_many_units(self):
        chromosome = Chromosome([['1', 'test_student', 'CIS312']], ['Tutor1'], ['CIS311'])

        # Add too many units to the student's units
        chromosome.students[0].units.extend(['test2', 'test3', 'test4', 'test5'])

        self.assertEqual(chromosome.evaluate_fitness(), 50)
