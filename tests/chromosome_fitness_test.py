import unittest

from src.chromosome import Chromosome

class ChromosomeFitnessTest(unittest.TestCase):
    # def test_fitness(self):
    #     chromosome = Chromosome([['1', 'test_student', 'CIS312'], ['2', 'test_student2', 'CIS312'], ['3', 'test_student3', 'CIS312']], 
    #                             ['Tutor1', 'Tutor2', 'Tutor3', 'Tutor4'], 
    #                             ['CIS311', 'CIS312', 'CIS313'])

    #     self.assertEqual(chromosome.evaluate_fitness(), 0)

    def test_schedule_has_exam_for_each_unit_hard_constraint_true(self):
        chromosome = Chromosome([['1', 'test_student', 'CIS312'], ['2', 'test_student2', 'CIS312'], ['3', 'test_student3', 'CIS312']], 
                                ['Tutor1', 'Tutor2', 'Tutor3', 'Tutor4'], 
                                ['CIS311', 'CIS312', 'CIS313'])

        self.assertTrue(chromosome.schedule_has_exam_for_each_unit_hard_constraint())

    def test_schedule_has_exam_for_each_unit_hard_constraint_false(self):
        chromosome = Chromosome([['1', 'test_student', 'CIS312'], ['2', 'test_student2', 'CIS312'], ['3', 'test_student3', 'CIS312']], 
                                ['Tutor1', 'Tutor2', 'Tutor3', 'Tutor4'], 
                                ['CIS311', 'CIS312', 'CIS313'])

        # Add new unit after the exam timetable schedule has been created
        chromosome.units.append('CIS316')

        self.assertFalse(chromosome.schedule_has_exam_for_each_unit_hard_constraint())

    def test_exam_has_tutor_invigilating_hard_constraint_true(self):
        chromosome = Chromosome([['1', 'test_student', 'CIS312'], ['2', 'test_student2', 'CIS312'], ['3', 'test_student3', 'CIS312']], 
                                ['Tutor1', 'Tutor2'], 
                                ['CIS311', 'CIS312', 'CIS313'])

        self.assertTrue(chromosome.exam_has_tutor_invigilating_hard_constraint())

    def test_exam_has_tutor_invigilating_hard_constraint_false(self):
        chromosome = Chromosome([['1', 'test_student', 'CIS312'], ['2', 'test_student2', 'CIS312'], ['3', 'test_student3', 'CIS312']], 
                                ['Tutor1', 'Tutor2', 'Tutor3', 'Tutor4'], 
                                ['CIS311', 'CIS312', 'CIS313'])

        # Remove tutor from exam
        chromosome.schedule[0][2] = ''

        self.assertFalse(chromosome.exam_has_tutor_invigilating_hard_constraint())

    def test_exam_has_one_tutor_invigilating_hard_constraint_true(self):
        chromosome = Chromosome([['1', 'test_student', 'CIS312'], ['2', 'test_student2', 'CIS312'], ['3', 'test_student3', 'CIS312']], 
                                ['Tutor1', 'Tutor2'], 
                                ['CIS311', 'CIS312', 'CIS313'])

        self.assertTrue(chromosome.exam_has_one_tutor_invigilating_hard_constraint())

    def test_exam_has_one_tutor_invigilating_hard_constraint_false(self):
        chromosome = Chromosome([['1', 'test_student', 'CIS312'], ['2', 'test_student2', 'CIS312'], ['3', 'test_student3', 'CIS312']], 
                                ['Tutor1', 'Tutor2'], 
                                ['CIS311', 'CIS312', 'CIS313'])

        # Add two tutors to invigilate one exam
        chromosome.schedule[0][2] = ['Tutor1', 'Tutor2']

        self.assertFalse(chromosome.exam_has_one_tutor_invigilating_hard_constraint())

    # def test_student_too_many_units(self):
    #     chromosome = Chromosome([['1', 'test_student', 'CIS312']], ['Tutor1'], ['CIS311'])

    #     # Add too many units to the student's units
    #     chromosome.students[0].units.extend(['test2', 'test3', 'test4', 'test5'])

    #     self.assertEqual(chromosome.evaluate_fitness(), 50)
