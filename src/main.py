import csv

import matplotlib.pyplot as plt

from population import Population

def load_data():
    student_units = []
    with open("src/data/student_units.csv") as csv_file:    
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
           student_units.append(row)

    tutors = []
    with open("src/data/tutor.csv") as csv_file:   
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
           tutors.append(row[0])
    
    units = []
    with open("src/data/units.csv") as csv_file:   
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
           units.append(row[0])

    return student_units, tutors, units

    
if __name__ == "__main__":
    # Control Parameters
    POPULATION_SIZE         = 100 # Population size: generate population randomly within range of 50 - 250
    CROSSOVER_PROBABILITY   = 0.1 # Select crossover probability within range [0 – 1]
    MUTATION_PROBABILITY    = 0.05 # Select mutation probability within range [0 – 1] (always use lesser value as compared to the crossover probability)
    MAXIMUM_GENERTIONS      = 50 # Use maximum number of generations within range of [50 – 500]

    student_units, tutors, units = load_data()

    population = Population(student_units, tutors, units)
    population.generate_population(POPULATION_SIZE)

    averages = []
    max_fitnesses = []
    population_sizes = []

    generation = 1
    while generation <= MAXIMUM_GENERTIONS:
        print("--- Generation %d ---" % generation)
        print("Total population size: " + str(len(population.population)))

        max_fitness = max(population.evaluate_population_fitness())
        max_fitnesses.append(max_fitness)
        print("Highest fitness: " + str(max_fitness))
        
        average = sum(population.evaluate_population_fitness()) / len(population.population)
        averages.append(average)
        print("Average fitness: " + str(average))

        population.generate_next_generation(crossover_probability=CROSSOVER_PROBABILITY, 
                                            mutation_probability=MUTATION_PROBABILITY)

        generation += 1

    plt.plot(averages, label='Average')
    plt.plot(max_fitnesses, label='Max Fitness')

    plt.legend()
    plt.xlabel('Generation')
    plt.ylabel('Fitness')

    plt.show()

    