# -*- coding: UTF-8 -*-

def total_salary(path):
    fail = open(path, 'r')
    lines = fail.readlines()
    fail.close()
#wow
    total_salary = 0.0
    for line in lines:
        total_salary += float(line[line.index(',') + 1:])

    return total_salary