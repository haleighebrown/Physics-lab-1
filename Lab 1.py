

import math


def rule_three():
    print ("Error in first value: ")
    DA = float(input())

    print("Error in second value: ")
    DB = float(input())

    Error_3 = math.sqrt((DA)**2+(DB)**2)
    return Error_3

def rule_four ():
    print ("Final calculated value: ")
    final_value = float(input())

    print("First Exponent: ")
    first_expo = float(input())

    print ("Error in first value: ")
    error_first = float(input())

    print ("First value: ")
    first_value = float(input())

    print("Second Exponent: ")
    second_expo = float(input())

    print("Error in second value: ")
    error_second = float(input())

    print("Second value: ")
    second_value = float(input())

    print("Third Exponent: ")
    third_expo = float(input())

    print("Error in Third value: ")
    error_third = float(input())

    print("Third value: ")
    third_value = float(input())

    error_final_value = final_value*math.sqrt((first_expo*(error_first/first_value))**2+(second_expo*(error_second/second_value))**2+(third_expo*(error_third/third_value))**2)
    return error_final_value


print(rule_three())


