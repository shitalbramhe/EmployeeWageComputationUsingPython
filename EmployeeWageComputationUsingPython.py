'''
@Author: Shital Bajait
@Date: 2022-02-04 17:33:00
@Last Modified by: Shital Bajait
@Last Modified time: 2022-02-04 22:49:00
@Title : Calculate Daily Employee Wage
'''

import random

EMP_RATE_PER_HOUR = 20
number = random.randint(0,1)
if number == 1:
    print("Employee is present")
    empHrs = 8
else:
    print("Employee is absent")
    empHrs = 0
print("Daliy Wage is : ",empHrs * EMP_RATE_PER_HOUR)