#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == '__main__':
    number_1 = int(input("Enter first number - "))
    number_2 = int(input("Enter second number - "))
    number_3 = int(input("Enter third number - "))
    number_4 = int(input("Enter the fourth number - "))
    sum_1_2 = number_1 + number_2
    sum_3_4 = number_3 + number_4
    division_result = sum_1_2 / sum_3_4
    print("Result: %.2f" %
          division_result)
