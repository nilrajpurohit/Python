# Repo Hub
# Service Bus
# ACA ACE
# Keywalt
# ADO Agnet
# Resource Group
# Subscriptions
# Private Endpoints

import math 
square_root = math.sqrt(4);
value = math.floor(square_root);
print(value)

# Multiple Imports
from math import sqrt, pi
print(sqrt(16))
print(pi)

# Aliasing Models
import math as m
print(m.sqrt(36))

# Aliasing Function
from math import factorial as fact
print(fact(5))

# Module Search Path
# Python searches modules in this order:
# Current directory
# Installed packages
# Standard library
# Paths listed in sys.path

import sys 
print(sys.path)