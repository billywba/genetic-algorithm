import csv

def load_data():
    student_units = []
    with open("data/student_units.csv") as csv_file:    
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
           student_units.append(row)

    tutors = []
    with open("data/tutor.csv") as csv_file:   
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
           tutors.append(row[0])
    
    units = []
    with open("data/units.csv") as csv_file:   
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
           units.append(row[0])

    return student_units, tutors, units

    
if __name__ == "__main__":
    student_units, tutors, units = load_data()

    print(student_units)

    generation = 1
    while generation <= 1:
        print("--- Generation %d ---" % generation)
        generation = generation + 1
