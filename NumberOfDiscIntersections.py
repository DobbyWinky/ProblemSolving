# We draw N discs on a plane. The discs are numbered from 0 to N − 1. An array A of N non-negative integers, specifying the radiuses of the discs, is given. The J-th disc is drawn with its center at (J, 0) and radius A[J].

# We say that the J-th disc and K-th disc intersect if J ≠ K and the J-th and K-th discs have at least one common point (assuming that the discs contain their borders).

# The figure below shows discs drawn for N = 6 and A as follows:

#   A[0] = 1
#   A[1] = 5
#   A[2] = 2
#   A[3] = 1
#   A[4] = 4
#   A[5] = 0


# There are eleven (unordered) pairs of discs that intersect, namely:

# discs 1 and 4 intersect, and both intersect with all the other discs;
# disc 2 also intersects with discs 0 and 3.
# Write a function:

# def solution(A)

# that, given an array A describing N discs as explained above, returns the number of (unordered) pairs of intersecting discs. The function should return −1 if the number of intersecting pairs exceeds 10,000,000.

# Given array A shown above, the function should return 11, as explained above.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [0..100,000];
# each element of array A is an integer within the range [0..2,147,483,647].


def solution(A):
    if len(A)==0:
        return 0
    n=len(A)
    S=[0]*n
    E=[0]*n
    CS=[0]*n
    CE=[0]*n

    for i in range(n):
        if (i-A[i]<=0):
            S[i]=0
        else:
            S[i]=i-A[i]
        if (i+A[i])>n-1:
            E[i]=n-1
        else:
            E[i]=i+A[i]     
        CS[S[i]]+=1
        CE[E[i]]+=1
    
    CCS=[0]*n
    CCE=[0]*n
    CCS[0]=CS[0]
    CCE[0]=CE[0]

    for i in range(1, n):
        CCS[i]=CS[i]+CCS[i-1]
        CCE[i]=CE[i]+CCE[i-1]
    s=0
    for i in range(n):
        if i==0:
            s+=(CCS[i]-CS[i])*CS[i]+CS[i]*(CS[i]-1)//2
        else:
            s+=(CCS[i]-CCE[i-1]-CS[i])*CS[i]+CS[i]*(CS[i]-1)//2
    if s>10000000:
        return -1
    return s
