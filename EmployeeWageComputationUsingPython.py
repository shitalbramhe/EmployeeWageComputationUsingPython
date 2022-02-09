'''
@Author: Shital Bajait
@Date: 2022-02-04 17:33:00
@Last Modified by: Shital Bajait
@Last Modified time: 2022-02-09 11:10:00
@Title : Store Day and Daily Wage using Dictionary
'''


import random

EMP_RATE_PER_HOUR = 20
NUM_OF_WORKING_DAYS = 20
MAX_HRS_IN_MONTH = 100
def FullTime():
    """
        Description:
            Function to calculate hours
        Parameter:
            None
        Return:
            None
    """
    return 8
def PartTime():
    return 4
switcher = {
        0: FullTime(),
        1: PartTime(),
    }
def total():
    totalEmpHrs = 0
    totalWorkingDays = 0
    totalEmpWage=0
    empWage = {}
    while totalEmpHrs < MAX_HRS_IN_MONTH and totalWorkingDays < NUM_OF_WORKING_DAYS:
            number = random.randint(0,1)
            option = switcher.get(number)
            if totalEmpHrs == 96 and option ==  8:
                print("you are working for more than 100 hours")
                break
            totalEmpHrs=totalEmpHrs+option
            empWage[totalWorkingDays]=option * EMP_RATE_PER_HOUR
            print("Day :", totalWorkingDays+1 ,"Daily wage : ",empWage[totalWorkingDays])
            totalWorkingDays+=1
    print("Total Employee Hours : ",totalEmpHrs)
    sum = 0
    for i in empWage.values():
           sum = sum + i
    print("Total Employee Wage : ",sum)
if __name__ == '__main__':
    total()

