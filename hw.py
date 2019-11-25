
'''#HW2//Using Print The current weekday, week, month and year in separate statements.#
from datetime import datetime
now = datetime.now()
weekday=now.strftime("%cw")
print("current weekday:",weekday)
week=now.strftime("%w")
print("week:", week)
month=now.strftime("%m")
print("month:",month)
year=now.strftime("%y")
print("year:",year)'''

#HW3//Use two functions from the math library.#
import math
num1=int(input("Enter the number"))
num2=int(input("Enter the number"))
print('Factorial: ', math.factorial(num1))
print('Factorial: ', math.factorial(num2))

import math
num=int(input("Enter your number"))
print("sqrt: ",math.sqrt(num))

