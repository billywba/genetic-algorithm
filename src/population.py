import random

from chromosome import Chromosome

class Population():
    def __init__(self, student_units, tutors, units):
        self.student_units = student_units
        self.tutors = tutors
        self.units = units

    def generate_population(self, population_size=50):
        self.population = [Chromosome(student_units=self.student_units, tutors=self.tutors, units=self.units) for i in range(0, population_size)]

    def evaluate_population_fitness(self):
        return [population.evaluate_fitness() for population in self.population]

    def generate_next_generation(self, crossover_probability=0.3, mutation_probability=0.1):
        # Select best parents
        new_population = self.population[:10]

        # Crossover 

        # Mutate
        for individual in self.population:
            individual.mutate(mutation_probability)

        # Apply new generation
        self.population = new_population
