file = open('input.txt')
input_list = list(line for line in file)
for x in range(len(input_list)):
    input_list[x] = input_list[x].split()
    for y in range(len(input_list[x])):
        input_list[x][y] = float(input_list[x][y])
file.close()
import math
import numpy as np
import statistics as stat

#input_list = np.transpose(np.array(input_list))

def get_p1(mat):
    a = [x[0] for x in mat]
    b = [x[1] for x in mat]
    print(a,b)
    return np.cov(a,b)[1][0]/(np.cov(a,b)[0][0])

def get_p2(p1,mat):
    a_average = stat.mean([x[0] for x in mat])
    b_average = stat.mean([x[1] for x in mat])
    print(a_average,b_average)
    return b_average - (a_average-1920)*p1

print(get_p1(input_list),get_p2(get_p1(input_list),input_list))

def function(value):
    return get_p1(input_list)*value + get_p2(get_p1(input_list),input_list)

def chi_squre(list_1, list_2):
    return sum((x-y)^2 for x in list_1 and for y in list_2)
print(chi_squre([x[1] for x in input_list],[function(y[0]) for y in input_list]))