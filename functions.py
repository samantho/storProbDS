####################  Imports  ####################
import math

#################### Functions ####################


# Combination: n Choose k
# binomial coefficient
# number of ways to select k items out of n, order doesn't matter
def choose(n, k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n-k))


# Permutation: n permute k
# number of ways to select k items out of n, order matters
def perm(n, k):
    return math.factorial(n) /  math.factorial(n-k)


# Multinomial Coefficients
# number of ways to divide n distinct objs into k distinct groups of sizes n1, n2, ... nr
# permutations of n objects where there are n1, n2 ... nk repeated objs
def n_choose_groups(n, n_list):
    if(sum(n_list) != n):
        print("all group sizes must add to n" ,sum(n_list))
        return
    ways = math.factorial(n)
    for x in n_list:
        ways /= math.factorial(x)
    return ways
    

# Basic Sampling
# ways to draw k samples from n elements
# can be with or without replacement and ordered or unordered
def basic_sample(n, k, ordered, replacement): 
    if(ordered and replacement):
        return math.pow(n, k)
    if(ordered and not replacement):
        return math.factorial(n) / math.factorial(n-k)
    if(not ordered and replacement):
        return choose(n, k)
    if(not ordered and not replacement):
        return choose(n + k - 1, k)

##### possibly conditional probability




################# Random Variables ################
# Each distribution's primary function returns: 
#   dictionary of probability density function, expected value, and variance

# Common parameters:
#       p is the probability of the event occurring
#       n is the number of trials
#       x is the the value of that probability
#       all will print the prob of all values 0 to n


# --- Bernoulli Random Variable ---
# X takes 2 values, success (1) or failure (0)
# each action must be independent
# Parameters: p is the probability of success
def B(p):
    return {"E": p, "Var": p*(1-p), 0: 1-p, 1: p}

def B_x_given_p(x, p, n=1):
    return math.pow(p, x) * math.pow(1-p, n-x)


# --- Binomial Random Variable ---
# X takes values {0, 1, .. n}
# frequency of an event in n of trials
# the event must be bernoulli and the trials must be independent
# Parameters: p is probability of the event, n is number of trials
def Bin(n, p, x=False, all=False):
    binomial = {"E": n*p, "Var": math.sqrt(n*p*(1-p))}   #, "EX^2": math.pow(n*p, 2) + (n * p * (1 - p))}
    def prob_of_x(x):
        return choose(n, x) * B_x_given_p(x, p, n)
    if(type(x) == int or type(x) == float):
        binomial.update({x: prob_of_x(x)})
    if(all):
        for i in range(n + 1):
            binomial.update({i: prob_of_x(i)})
    return binomial


# --- Poisson Random Variable ---
# X takes values WHAT TO WHAT
# approximately binomial for large n, small p, where lambda = np
# Parameters: mean or lambda is the mean number of events (> 0)
#       time is the time range the events happened in [0, t]
#       max is the value x prints up to
def Pois(mean, time = 1, x = False, max = False):
    poisson = {"E": mean, "Var": mean}
    mean = mean * time
    def prob_of_x(x):
        return math.pow(mean, x) * math.pow(math.e, -1 * mean) / math.factorial(x)
    if(type(x) == int or type(x) == float):
        poisson.update({x: prob_of_x(x)})
    if(max):
        for i in range(max + 1):
            poisson.update({i: prob_of_x(i)})
    return poisson