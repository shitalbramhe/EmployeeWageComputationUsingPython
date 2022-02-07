'''
@Author: Shital Bajait
@Date: 2022-02-04 17:33:00
@Last Modified by: Shital Bajait
@Last Modified time: 2022-02-05 17:22:00
@Title : Refactor code using function
'''

import random

def emp_hours():
    '''
    Description:
        calculates the total employee working hours untill an employee working days of the month reaches 20 or total working hours of the month reaches 100 hours.
    parameter:
        None
    Return:
        None
    '''

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
    num = random.randint(0,2)
    if num == 0:
        empHrs = 8
    elif num == 1:
        empHrs = 4
    else:
        empHrs = 0
    
    day+=1
    totalEmpHrs+= empHrs 
    print("Day#:",totalWorkingDays,"Employee Hours:",empHrs)

totalEmpWage =totalEmpHrs* EMP_RATE_PER_HOUR
print("Total Employee Wage : ",totalEmpWage)
        