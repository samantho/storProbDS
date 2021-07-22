import math

from functions import *

probs = {
    "0": 0.1,
    "1": 0.2,
    "2": 0.4,
    "3": 0.3
}


# --- Basic Probability ---

#choose(10, 5)
#perm(10, 5)
#n_choose_groups(n=5, n_list=[1, 2, 2])
#basic_sample(n=5, k=3, ordered=False, replacement=True)


# --- Conditional Probability ---


# --- Discrete Random Variables ---

#discrete(probs)
#B(p=0.4)
#Bin(n=20, p=0.4, x=3)
#Pois(mean=4.6, x=5)
#Geom(p=0.0128, x=7)
#Hgeom(52, 5, 26, 2)


# --- Continuous Random Variables ---
#Exp(0.25, 5)
#U(0, 10)
print(Normal(1, 1, max=3))