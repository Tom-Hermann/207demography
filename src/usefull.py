##
## EPITECH PROJECT, 2021
## B-MAT-400-RUN-4-1-207demography-tom.hermann
## File description:
## usefull
##

import csv

def loadColumn(data, column):
    values = []
    try:
        for line in data:
            values.append(line[column])
    except:
        exit(84)
    return values

def load_data():
    data = []
    try:
        with open("./207demography_data.csv", 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=';')
            for row in reader:
                data.append(row)
            data.pop(0)
            if (len(data) < 1):
                exit(84)
    except:
        exit(84)
    return data
