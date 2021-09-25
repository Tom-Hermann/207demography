##
## EPITECH PROJECT, 2021
## B-MAT-400-RUN-4-1-207demography-tom.hermann
## File description:
## error
##

from src.constante import SUCCESS, FAILURE

def printUsage():
    print("USAGE\n\t./207demography code [...]")
    print("DESCRIPTION\n\tcode\tcountry code")

def error(allCode, argv):
    if not argv:
        exit(FAILURE)
    if "-h" in argv or  "--help" in argv:
        printUsage()
        exit(SUCCESS)
    for code in argv:
        if not code in allCode:
            exit(FAILURE)