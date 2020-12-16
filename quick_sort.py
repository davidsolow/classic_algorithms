#Import input

import statistics as stat
text_file = open("file.txt", "r")
input = text_file.read().splitlines()
text_file.close()
input = [int(i) for i in input]

# Partition arrays for comparisions

def partition(A):
  count = 0                     #set comparison counter
  p = A[0]                      #pivot for comparison
  r = len(A)                    #endpoint
  i = 1                         #first integer to compare
  for j in range(1, r):         #Compare integers to pivot
    count += 1                  #Increment counter of comparisons
    if A[j] < p:
      A[j], A[i] = A[i], A[j]   #Swap numbers where needed
      i += 1
  A[0], A[i-1] = A[i-1], A[0]   #Place pivot where it belongs in array
  return i-1, count

#Choose Pivot based on "Median of Three" (pivot = median of first, middle, and last integers)

def ChoosePivot(A):
  l = A[0]                      #first integer
  if len(A) % 2 == 0:           #middle integer if even number of elements
    k = (len(A)//2)-1
    c = A[k]
  else:
    k = len(A)//2               #middle integer if odd number of elements
    c = A[k]
  r = A[-1]
  allthree = [l, c, r]
  medianofthree = stat.median(allthree)

  return A.index(medianofthree)

#Quicksort + Count of Number of Comparisons

def quicksort(A):
  if len(A) <= 1:                   #Base case, if only one element in array then nothing to sort/no comparisons
    return A, 0
  i = ChoosePivot(A)                #Get pivot from helper function
  A[0], A[i] = A[i], A[0]           #Bring pivot to front
  j, count = partition(A)           #Partition / make comparisons
  A[:j], l = quicksort(A[:j])       #Recursive call for left side of pivot
  A[j+1:], r = quicksort(A[j+1:])   #Recursive call for right side of pivot
  return A, l + r + count