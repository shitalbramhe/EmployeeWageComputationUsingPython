'''
@Author: Shital Bajait
@Date: 2022-02-04 17:33:00
@Last Modified by: Shital Bajait
@Last Modified time: 2022-02-07 17:22:00
@Title : Refactor code using function
'''
"""
Description:
    Function to calculate hours
Parameter:
      None
Return:
      None
"""

import random

EMP_RATE_PER_HOUR = 20
NUM_OF_WORKING_DAYS = 20
MAX_HRS_IN_MONTH = 100
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
def total():
    totalEmpHrs = 0
    totalWorkingDays = 0
    totalEmpWage=0
    empWage = 0
    while totalEmpHrs <= MAX_HRS_IN_MONTH and totalWorkingDays < NUM_OF_WORKING_DAYS:
            totalWorkingDays+=1
            number = random.randint(0,2)
            option = switcher.get(number)
            totalEmpHrs=totalEmpHrs+option()
            empWage=option()*EMP_RATE_PER_HOUR
            totalEmpWage += empWage
    print("Total Employee Hours : ",totalEmpHrs)
    print("Total Employee Wage : ",totalEmpWage)
#print employee wage
total()
