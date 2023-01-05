from chromosome import Chromosome

class Population():
    def __init__(self, student_units, tutors, units):
        self.student_units = student_units
        self.tutors = tutors
        self.units = units

    def generate_population(self, population_size=50):
        self.population = [Chromosome(student_units=self.student_units, tutors=self.tutors, units=self.units) for i in range(0, population_size)]
