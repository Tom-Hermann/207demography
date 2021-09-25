#!/usr/bin/python3
##
## EPITECH PROJECT, 2021
## B-MAT-400-RUN-4-1-207demography-tom.hermann
## File description:
## main
##

import csv
from sys import argv
from src.error import error
from src.usefull import *
from src.calcul import *
from math import sqrt


def printCountry(arg, code, country):
    all_country = "Country:"
    for i in arg:
        all_country += " " + country[code.index(i)] + ","
    print(all_country[:-1])

def getDataFit1(total, years):
    sums = [0] * 4

    for i in range(0, len(total)):
        sums[0] += total[i]
        sums[1] += years[i]
        sums[2] += years[i] ** 2
        sums[3] += total[i]*years[i]
    return sums

def fit1(total, years):
    print("Fit1")
    res = 0
    data = getDataFit1(total, years)
    a = getA(data, years)
    b = getB(data, years)

    if a >= 0:
        print("\tY = {:.2f} X + {:.2f}".format(b / 10 ** 6, a / 10 ** 6))
    else:
        print("\tY = {:.2f} X - {:.2f}".format(b / 10 ** 6, abs(a) / 10 ** 6))
    for i in range(len(total)):
        population  = years[i] * b + a
        res += (population - total[i]) ** 2
    res /= len(total)
    print("\tRoot-mean-square deviation: {:.2f}".format(sqrt(res) / 10 ** 6))
    print("\tPopulation in 2050: {:.2f}".format((2050 * b + a) / 10 ** 6, ".2f"))
    return  (b / 10 ** 6), (a / 10 ** 6)

def getDataFit2(total, years):
    sums = [0] * 4

    for i in range(0, len(total)):
        sums[0] += years[i]
        sums[1] += total[i]
        sums[2] += pow(total[i], 2)
        sums[3] += total[i] * years[i]
    return sums


def fit2(total, years):
    print("Fit2")
    res = 0
    data = getDataFit2(total, years)
    a = getA(data, years)
    b = getB(data, years)

    if a >= 0:
        print("\tX = {:.2f} Y + {:.2f}".format(b * 10 ** 6, a))
    else:
        print("\tX = {:.2f} Y - {:.2f}".format(b * 10 ** 6, abs(a)))
    for i in range(len(total)):
        population  = (years[i] - a) / b
        res += (population - total[i]) ** 2
    res /= len(total)
    print("\tRoot-mean-square deviation: {:.2f}".format(sqrt(res) / 10 ** 6))
    print("\tPopulation in 2050: {:.2f}".format((2050 - a) / (b * 10 ** 6), ".2f"))

def correlation(total, years):
    print("Correlation:\t", end='')
    totalMean = sum(total) / len(total)
    yearsMean = sum(years) / len(years)
    first = 0
    second = 0
    yearDistanceMean = 0
    totalDistanceMean = 0
    for i in range(len(total)):
        first += (total[i] - totalMean) * (years[i] - yearsMean)
        yearDistanceMean += (total[i] - totalMean) ** 2
        totalDistanceMean += (years[i] - yearsMean) ** 2
    second = sqrt(yearDistanceMean * totalDistanceMean)
    print("{:.4f}".format(first / second))
    return total

def main():
    arg = argv[1:]
    years = [x for x in range(1960, 2018)]
    data = load_data()
    country = loadColumn(data, 0)
    code = loadColumn(data, 1)
    error(code, arg)
    printCountry(arg, code, country)
    total = calculeTotale(arg, code, data)
    fit1(total, years)
    fit2(total, years)
    correlation(total, years)
    exit(0)

if __name__ == "__main__":
    main()
