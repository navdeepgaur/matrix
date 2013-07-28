# Please fill out this stencil and submit using the provided submission script.





## Problem 1
def myFilter(L, num): return [x for x in L if x%num != 0]



## Problem 2
def myLists(L): 
     L2 = [list(range(l)) for l in L]
     L3 = [[l+1 for l in l2] for l2 in L2]
     return L3




## Problem 3
def myFunctionComposition(f, g): return {x:g[f[x]] for x in f.keys() }


## Problem 4
# Please only enter your numerical solution.

complex_addition_a = 5 + 3j 
complex_addition_b = 0 + 1j
complex_addition_c = -1 + 0.001j
complex_addition_d = 0.001 + 9j



## Problem 5
GF2_sum_1 = 1
GF2_sum_2 = 0
GF2_sum_3 = 0


## Problem 6
def mySum(L):
    current = 0
    for x in L:
        current = current + x
    return current



## Problem 7
def myProduct(L): 
    current = 1
    for x in L:
        current = current * x
    return current



## Problem 8
def myMin(L): return min(L)



## Problem 9
def myConcat(L): 
    current = ""
    for estr in L:
      current = current + estr
    return current




## Problem 10
def myUnion(L):
    current = set()
    for eset in L:
      current = current | eset
    return current


