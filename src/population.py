import random

from copy import copy, deepcopy

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

    def crossover(self, parent_one, parent_two):
        offspring = copy(parent_one)
        cut_index = random.randint(0, len(parent_one.schedule) - 1)
        
        # Copy the schedules
        parent_one_schedule = parent_one.schedule.copy() 
        parent_two_schedule = parent_two.schedule.copy()

        # Take schedule from first parent up until chosen index
        first_part = parent_one_schedule[:cut_index]
        second_part = parent_two_schedule[cut_index:]

        # Combine to make new schedule
        new_schedule = first_part + second_part

        # Take remaining schedule from parent two
        offspring.schedule = new_schedule

        return offspring

    def generate_next_generation(self, crossover_probability=0.3, mutation_probability=0.1):
        # Select best parents
        new_population = self.find_two_fittest_schedules(self.population)

        # Crossover
        for individual in self.population:
            if random.uniform(0, 1) < crossover_probability:
                new_offspring = self.crossover(individual, random.choice(new_population))
                new_population.append(new_offspring)

        # Mutate
        for individual in new_population:
            individual.mutate(mutation_probability)

        # Apply new generation
        self.population = new_population

    def find_two_fittest_schedules(self, population):
        ordered_population = deepcopy(population)
        ordered_population.sort(key=lambda x: x.fitness, reverse=True)

        return ordered_population[:2]