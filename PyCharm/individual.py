#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == '__main__':
    temperature_celsius = float(input("Enter the temperature value in degrees Celsius: "))
    temperature_fahrenheit = temperature_celsius * 1.8 + 32
    temperature_kelvin = temperature_celsius + 273.15
    print("Fahrenheit temperature:", temperature_fahrenheit)
    print("Kelvin temperature:", temperature_kelvin)

