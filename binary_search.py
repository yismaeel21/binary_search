#!/bin/python3
def find_smallest_positive(xs, val = 0):
    left = 0
    right = len(xs)-1
    def go(left, right):
        mid = (left+right)//2
        if 0 == xs[mid]:
            return mid+1
        if left == right:
            if xs[mid] > 0:
                return mid
            else:
                return None
        if 0 < xs[mid]:
            return go(left, mid-1)
        if 0 > xs[mid]:
            return go(mid+1, right)

    if len(xs) == 0:
        return None
    if xs[0] > 0:
        return 0
    else:
        return go(left, right)

def count_repeats(xs,x):
    left = 0
    right = len(xs) - 1
   
    def fxOne(left,right):
        mid = (left + right)//2
        if xs[mid] == x:     #checking if the middle character is the one we are looking for
            if mid == 0 or xs[mid-1] > x: #base case for recursive purposes or if the index prior to the middle is greater than x, we return middle
                return mid
            #if xs[mid-1] >x:
             #   return mid  I tried having it this way but it didnt work at first
            else:
                return fxOne(left, mid-1)
       
        if left == right:    #we've reached the end without a solution, there are no recurrances
            return None
        if x > xs[mid]:   #if our value is greater than the middle value, we keep going until we find one that is equal
            return fxOne(left, mid -1)
        if x < xs[mid]:   #if our value is less than the middle value, we go from the middle + 1 to the end... essentially looking for when it equals it
            return fxOne(mid + 1, right)

    def fxTwo(left, right):
        mid = (left+ right)//2
        if xs[mid] == x:
            if mid == (len(xs)-1) or x > xs[mid+1]:  #Same as the one above but going from the right onwards
                return mid
            else:
                return fxTwo(mid + 1, right)
        if left == right:
            return None
        if xs[mid] > x:
            return fxTwo(mid + 1, right)
        if x > xs[mid]:
            return fxTwo(left, mid-1)
    
    if xs == []:
        return 0
    firstOne = fxOne(left, right)
    secondOne = fxTwo(left, right)
    
    if firstOne == None or secondOne == None:
        return 0
    else:
        return secondOne - firstOne + 1   #The difference between the second one and the first one, including the first term.


   

def argmin(f, lo, hi, epsilon=1e-3):
    '''
    Assumes that f is an input function that takes a float as input and returns a float with a unique global minimum,
    and that lo and hi are both floats satisfying lo < hi.
    Returns a number that is within epsilon of the value that minimizes f(x) over the interval [lo,hi]

    HINT:
    The basic algorithm is:
        1) The base case is when hi-lo < epsilon
        2) For each recursive call:
            a) select two points m1 and m2 that are between lo and hi
            b) one of the 4 points (lo,m1,m2,hi) must be the smallest;
               depending on which one is the smallest, 
               you recursively call your function on the interval [lo,m2] or [m1,hi]

    >>> argmin(lambda x: (x-5)**2, -20, 20)
    5.000040370009773
    >>> argmin(lambda x: (x-5)**2, -20, 0)
    -0.00016935087808430278
    '''
    low = lo
    high = hi
    def go(low, high):
        m1 = low + (high - low)/15
        m2 = low + (high- low)/20
        if high - low < epsilon:
            return high
        if f(m1) > f(m2):
            return go(m1, high)
        if f(m1) < f(m2):
            return go(low, m2)
    
    return go(low,high)
