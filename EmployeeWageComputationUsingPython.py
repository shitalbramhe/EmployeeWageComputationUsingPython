'''
@Author: Shital Bajait
@Date: 2022-02-04 17:33:00
@Last Modified by: Shital Bajait
@Last Modified time: 2022-02-05 17:22:00
@Title : Wages for a month
'''

import random

EMP_RATE_PER_HOUR = 20 
NUM_OF_WORKING_DAYS = 20
empHrs = 0
empWage = 0
totalEmpWage=0
day=0
while day<NUM_OF_WORKING_DAYS:
    num = random.randint(0,2)
    if num == 0:
        empHrs = 8
    elif num == 1:
        empHrs = 4
    else:
        empHrs = 0
    
    empWage = empHrs * EMP_RATE_PER_HOUR
    totalEmpWage += empWage
    day+=1

print("Total Employee Wage : ",totalEmpWage)
        