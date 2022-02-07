'''
@Author: Shital Bajait
@Date: 2022-02-04 17:33:00
@Last Modified by: Shital Bajait
@Last Modified time: 2022-02-05 17:22:00
@Title : Calculate Wages till a condition of total working hours or days is reached for a month
'''

import random

EMP_RATE_PER_HOUR = 20 
NUM_OF_WORKING_DAYS = 20
empHrs = 0
empWage = 0
totalEmpWage=0
totalEmpHrs = 0
totalWorkingDays = 0
day=0
MAX_HRS_IN_MONTH = 100
while totalEmpHrs <= MAX_HRS_IN_MONTH and totalWorkingDays < NUM_OF_WORKING_DAYS:
    totalWorkingDays+=1
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
    totalEmpWage += empWage
    day+=1
#print employee wage
print("Total Employee Wage : ",totalEmpWage)