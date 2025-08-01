# 🔹 1. Built-in Modules
# These come pre-installed with Python — you don’t have to install or write them.

import math


# The math module provides mathematical functions like:
# Basic math functions

# num = int(input('Enter Numnber: '))
# print(math.sqrt(num)) # square root

print(math.pow(2,3)) # power

print(math.exp(2)) # exponential

# Trigonometry
print(math.sin(0)) # in radians
print(math.degrees((math.pi)/6))
print(math.cos(math.radians(30))) # cos(30deg) = cos(pi/6)

# Constants (like π and e)
print(math.pi)
print(math.e)

# Logarithms

print(math.log(4)) # Natural Base e
print(math.log2(8))
print(math.log10(100))

# Rounding and Comparison

print(math.floor(3.101)) # 3
print(math.ceil(4.12)) # 5
print(round(5.47)) # built in function 5.5
print(math.trunc(3.3333)) # 3
print(math.isclose(0.1+0.2,0.3))


# Factorial And Combinatorics

print(math.factorial(6))
print(math.comb(4,2))
print(math.perm(4,2))

