# Author: Taylor Hoss
# WSU ID: x432z869
# Program: Quick Sort Analysis
#

# for random number generation
import random
# for getting computation time
import time

# resource is used to set recursion limit in linux, sys for windows
# for setrecursionlimit()
import sys
# import resource

sys.setrecursionlimit(10000)
# resource.setrlimit(resource.RLIMIT_STACK, (resource.RLIM_INFINITY, resource.RLIM_INFINITY))

# main index swapping function
# Input: list, first index, last index
def partition(A, p, r):
    # pivot is the first element
    x = A[p]
    k = p
    j = r
    while True:
        while A[k] <= x and k < j:
            k += 1

        while A[j] >= x and j >= k:
            j -= 1

        if k < j:
            # swap A[k] and A[j]
            temp = A[k]
            A[k] = A[j]
            A[j] = temp

        else:
            break

    # swap A[k] and A[j]
    temp = A[p]
    A[p] = A[j]
    A[j] = temp
    return j


# recursive sorting functions
# input: List, first index, last index
def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)


# input: list, first index, last index
def rand_quicksort(A, p, r):
    if p < r:
        # pick random number to swap into last index
        index = random.randint(p, r)
        # swap A[k] and A[j]
        temp = A[r]
        A[r] = A[index]
        A[index] = temp

        # run partition like normal
        q = partition(A, p, r)
        rand_quicksort(A, p, q - 1)
        rand_quicksort(A, q + 1, r)

# seed the random number generator
random.seed()

MAX_RANGE = 10000

# user input
n = int(input("Enter number of integers (n):"))

# create array
a = [10001] * n

print("Distributions: \n1) Ascending order \n2) picked from uniform distribution over [0, 10,000]")

# get distribution
choice = int(input("Enter desired distribution:"))

if choice == 1:
    # get increment; 1st value is n+x, 2nd value is n+2x, etc.
    inc = int(input("Enter increment value for ascending order:"))
    for i in range(n):
        a[i] = n+(i+1)*inc

    # make another array for rand_quicksort
    b = a

    f = open('output.txt', 'w')
    f.write("original:\n")
    for i in range(n):
        f.write(str(i))
        f.write(": ")
        f.write(str(a[i]))
        f.write("\n")
    f.close

    start = time.time()
    quicksort(a, 0, len(a) - 1)
    end = time.time()

    f = open('output.txt', 'a')
    f.write("quicksorted:\n")
    f.write("quicksort computation time: ")
    f.write(str(end - start))
    for i in range(n):
        f.write(str(i))
        f.write(": ")
        f.write(str(a[i]))
        f.write("\n")
    f.close

    start = time.time()
    rand_quicksort(b, 0, len(b) - 1)
    end = time.time()

    f = open('output.txt', 'a')
    f.write("rand_quicksorted:\n")
    f.write("rand_quicksort computation time: ")
    f.write(str(end - start))
    for i in range(n):
        f.write(str(i))
        f.write(": ")
        f.write(str(b[i]))
        f.write("\n")
    f.close

if choice == 2:
    for i in range(n):
        a[i] = random.randint(0, MAX_RANGE)

    # make another array for rand_quicksort
    b = a

    f = open('output.txt', 'w')
    f.write("original:\n")
    for i in range(n):
        f.write(str(i))
        f.write(": ")
        f.write(str(a[i]))
        f.write("\n")
    f.close

    start = time.time()
    quicksort(a, 0, len(a) - 1)
    end = time.time()

    f = open('output.txt', 'a')
    f.write("quicksorted:\n")
    f.write("quicksort computation time: ")
    f.write(str(end - start))
    for i in range(n):
        f.write(str(i))
        f.write(": ")
        f.write(str(a[i]))
        f.write("\n")
    f.close

    start = time.time()
    rand_quicksort(b, 0, len(b) - 1)
    end = time.time()

    f = open('output.txt', 'a')
    f.write("rand_quicksorted:\n")
    f.write("rand_quicksort computation time: ")
    f.write(str(end - start))
    for i in range(n):
        f.write(str(i))
        f.write(": ")
        f.write(str(b[i]))
        f.write("\n")
    f.close
