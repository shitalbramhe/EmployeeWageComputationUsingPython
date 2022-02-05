'''
@Author: Shital Bajait
@Date: 2022-02-04 17:33:00
@Last Modified by: Shital Bajait
@Last Modified time: 2022-02-05 17:16:00
@Title : Add part time Employee and Wage
'''

import random

EMP_RATE_PER_HOUR = 20
number = random.randint(0,1)
if number == 1:
    print("Employee is FullTime")
    empHrs = 8
else:
    print("Employee is PartTime")
    empHrs = 4
print("Daliy Wage is : ",empHrs * EMP_RATE_PER_HOUR)