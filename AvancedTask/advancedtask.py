#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == '__main__':
    angle = float(input("Enter the number of degrees the hour hand has rotated: "))
    all_minutes = angle * 2
    hours = int(all_minutes // 60)
    minutes = int(all_minutes - (hours * 60))
    print("Number of full hours:", hours)
    print("Number of full minutes:", minutes)
