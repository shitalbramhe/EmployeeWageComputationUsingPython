'''
@Author: Shital Bajait
@Date: 2022-02-04 17:33:00
@Last Modified by: Shital Bajait
@Last Modified time: 2022-02-05 17:22:00
@Title : Employee Wage using switch case
'''

import random

EMP_RATE_PER_HOUR = 20
number = random.randint(0,2)
def FullTime():
    return 8
def PartTime():
    return 4
def Absent():
    return 0    

switcher = {
    0: Absent,
    1: FullTime,
    2: PartTime,
}
# Get the option from switcher dictionary
option = switcher.get(number)

empWage=option()*EMP_RATE_PER_HOUR

#print employee wage
print("Employee Wage:",empWage)