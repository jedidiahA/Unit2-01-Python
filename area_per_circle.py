#!/usr/bin/env python3

# Created by: Ms Raffin
# Created on: Apr. 27, 2021
# This program calculates and displays the area and perimeter of a
# circle with radius 12 mm.
import math


def main():
    print("For a circle that has a radius")
    print("of 12 mm:")
    print("")
    print("Area = {} mm^2".format(math.pi*12**2))
    print("Perimeter = {} mm".format(2*math.pi*12))


if __name__ == "__main__":
    main()
