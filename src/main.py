import csv

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
    CROSSOVER_PROBABILITY   = 0.4 # Select crossover probability within range [0 – 1]
    MUTATION_PROBABILITY    = 0.2 # Select mutation probability within range [0 – 1] (always use lesser value as compared to the crossover probability)
    MAXIMUM_GENERTIONS      = 250 # Use maximum number of generations within range of [50 – 500]
    THRESHOLD_FITNESS       = (10 * 7) + (5 * 2) # Constant values from chromosome.py - 7 hard constraints and 2 soft constraints

    student_units, tutors, units = load_data()

    population = Population(student_units, tutors, units)
    population.generate_population(POPULATION_SIZE)
    population.population[0].print_schedule()

    generation = 1
    while generation <= MAXIMUM_GENERTIONS:
        print("--- Generation %d ---" % generation)
        generation = generation + 1
