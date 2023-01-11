import unittest

from src.chromosome import Chromosome

class ChromosomeFitnessTest(unittest.TestCase):
    def test_fitness(self):
        chromosome = Chromosome([['1', 'test_student', 'CIS312'], ['2', 'test_student2', 'CIS312'], ['3', 'test_student3', 'CIS312']], 
                                ['Tutor1', 'Tutor2', 'Tutor3', 'Tutor4'], 
                                ['CIS311', 'CIS312', 'CIS313'])

        # self.assertGreater(chromosome.evaluate_fitness(), 35)

    def test_schedule_has_exam_for_each_unit_hard_constraint_true(self):
        chromosome = Chromosome([['1', 'test_student', 'CIS312'], ['2', 'test_student2', 'CIS312'], ['3', 'test_student3', 'CIS312']], 
                                ['Tutor1', 'Tutor2', 'Tutor3', 'Tutor4'], 
                                ['CIS311', 'CIS312', 'CIS313'])

        chromosome.schedule = [
                                ['P417', 'CIS311', 'Tutor5', 'Monday_PM'],
                                ['P418', 'CIS312', 'Tutor3', 'Monday_AM'],
                                ['P418', 'CIS313', 'Tutor3', 'Friday_PM']
                            ]

        # self.assertTrue(chromosome.schedule_has_exam_for_each_unit_hard_constraint())
        self.assertEqual(0, chromosome.schedule_has_exam_for_each_unit_hard_constraint())

    def test_schedule_has_exam_for_each_unit_hard_constraint_false(self):
        chromosome = Chromosome([['1', 'test_student', 'CIS312'], ['2', 'test_student2', 'CIS312'], ['3', 'test_student3', 'CIS312']], 
                                ['Tutor1', 'Tutor2', 'Tutor3', 'Tutor4'], 
                                ['CIS311', 'CIS312', 'CIS313'])

        chromosome.schedule = [
                                ['P417', 'CIS311', 'Tutor5', 'Monday_PM'],
                                ['P418', 'CIS312', 'Tutor3', 'Monday_AM'],
                                ['P418', 'CIS313', 'Tutor3', 'Friday_PM']
                            ]

        # Add new units after the exam timetable schedule has been created
        chromosome.units.extend(['CIS316', 'CIS319'])

        self.assertEqual(2, chromosome.schedule_has_exam_for_each_unit_hard_constraint())

    def test_exam_has_tutor_invigilating_hard_constraint_true(self):
        chromosome = Chromosome([['1', 'test_student', 'CIS312'], ['2', 'test_student2', 'CIS312'], ['3', 'test_student3', 'CIS312']], 
                                ['Tutor1', 'Tutor2'], 
                                ['CIS311', 'CIS312', 'CIS313'])

        self.assertEqual(0, chromosome.exam_has_tutor_invigilating_hard_constraint())

    def test_exam_has_tutor_invigilating_hard_constraint_false(self):
        chromosome = Chromosome([['1', 'test_student', 'CIS312'], ['2', 'test_student2', 'CIS312'], ['3', 'test_student3', 'CIS312']], 
                                ['Tutor1', 'Tutor2', 'Tutor3', 'Tutor4'], 
                                ['CIS311', 'CIS312', 'CIS313'])

        # Remove tutor from exam
        chromosome.schedule[0][2] = ''

        self.assertEqual(1, chromosome.exam_has_tutor_invigilating_hard_constraint())

    def test_tutor_invigilates_one_exam_at_a_time_hard_constraint_true(self):
        chromosome = Chromosome([['1', 'test_student', 'CIS312'], ['2', 'test_student2', 'CIS312'], ['3', 'test_student3', 'CIS312']], 
                                ['Tutor1', 'Tutor2'], 
                                ['CIS311', 'CIS312', 'CIS313'])

        chromosome.schedule = [
                                ['P417', 'CIS311', 'Tutor5', 'Monday_PM'],
                                ['P418', 'CIS312', 'Tutor3', 'Monday_PM'],
                                ['P418', 'CIS313', 'Tutor7', 'Monday_PM']
                            ]

        self.assertEqual(0, chromosome.tutor_invigilates_one_exam_at_a_time_hard_constraint())

    def test_tutor_invigilates_one_exam_at_a_time_hard_constraint_false(self):
        chromosome = Chromosome([['1', 'test_student', 'CIS312'], ['2', 'test_student2', 'CIS312'], ['3', 'test_student3', 'CIS312']], 
                                ['Tutor1', 'Tutor2'], 
                                ['CIS311', 'CIS312', 'CIS313'])

        chromosome.schedule = [
                                ['P417', 'CIS311', 'Tutor5', 'Monday_PM'],
                                ['P418', 'CIS312', 'Tutor5', 'Monday_PM'],
                                ['P418', 'CIS313', 'Tutor7', 'Monday_PM']
                            ]

        self.assertEqual(2, chromosome.tutor_invigilates_one_exam_at_a_time_hard_constraint())

    def test_student_does_not_sit_more_than_one_exam_per_day_soft_constraint_true(self):
        chromosome = Chromosome([['1', 'test_student', 'CIS312'], ['2', 'test_student2', 'CIS312'], ['3', 'test_student3', 'CIS312']], 
                                ['Tutor1', 'Tutor2'], 
                                ['CIS311', 'CIS312', 'CIS313'])

        chromosome.schedule = [
                                ['P415', 'CIS311', 'Tutor1'],
                                ['P416', 'CIS312', 'Tutor2']
                            ]

        # self.assertEqual(chromosome.student_does_not_sit_more_than_one_exam_per_day_soft_constraint())

    def test_student_does_not_sit_more_than_one_exam_per_day_soft_constraint_false(self):
        chromosome = Chromosome([['1', 'test_student', 'CIS312'], ['2', 'test_student2', 'CIS312'], ['3', 'test_student3', 'CIS312']], 
                                ['Tutor1', 'Tutor2'], 
                                ['CIS311', 'CIS312', 'CIS313'])

        chromosome.schedule = [
                                ['P417', 'CIS311', 'Tutor5'],
                                ['P418', 'CIS311', 'Tutor3']
                            ]

        # self.assertFalse(chromosome.student_does_not_sit_more_than_one_exam_per_day_soft_constraint())

    # def test_student_too_many_units(self):
    #     chromosome = Chromosome([['1', 'test_student', 'CIS312']], ['Tutor1'], ['CIS311'])

    #     # Add too many units to the student's units
    #     chromosome.students[0].units.extend(['test2', 'test3', 'test4', 'test5'])

    #     self.assertEqual(chromosome.evaluate_fitness(), 50)
