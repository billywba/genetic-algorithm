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
    student_units, tutors, units = load_data()

    population = Population(student_units, tutors, units)
    population.generate_population(200)
    population.population[0].print_schedule()

    generation = 1
    while generation <= 3:
        print("--- Generation %d ---" % generation)
        generation = generation + 1
