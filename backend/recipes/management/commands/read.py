import csv

with open('/Dev/foodgram-project-react/backend/data/ingredients.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)