from db import *


try:
    count1 = loadCount()
    q1 = int(input("How many 1?"))
    count2 = loadCount()
    q2 = int(input("How many 2?"))

    count1 -= q1
    saveCount(count1)

    count2 -= q2
    saveCount(count2)
except ValueError:
    print("Please try again in 1 min. At the moment operation is unavailable.")

