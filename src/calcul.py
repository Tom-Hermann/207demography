##
## EPITECH PROJECT, 2021
## B-MAT-400-RUN-4-1-207demography-tom.hermann
## File description:
## calcul
##

def sumColumn(data, index):
    res = 0
    for i in data:
        try:
            res += int(i[index])
        except:
            res += 0
    return res

def calculeTotale(arg, code, data):
    allLine = []
    res = []
    for i in arg:
        allLine.append((data[code.index(i)])[2:])
    for i in range(0, 58):
        res.append(sumColumn(allLine, i))
    return res


def getA(data, years):
    return (data[0] * data[2] - data[1] * data[3]) / (len(years) * data[2] - data[1] ** 2)

def getB(data, years):
    return (len(years) * data[3] - data[0] * data[1]) / (len(years) * data[2] - data[1] ** 2)
