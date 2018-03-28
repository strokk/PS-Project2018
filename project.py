# Project 2018 - Programming and Scripting
# Guilherme G. C. Paes - 2018


#code that reads iris data from iris.csv and is nicely formatted

with open("iris.csv") as f:
    for line in f:
        line = line.replace(',', ' ')
        line = line.rstrip()
        print(line[:11], line[12:16].strip())
