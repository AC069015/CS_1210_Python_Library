# Author: Anthony Cunningham Section A01
# Homework 7

# Sorting Method Codes
def selectionSort(L):
    i = 0
    while i < len(L):
        minIndex = findMinIndex(L, i)
        L[i], L[minIndex] = L[minIndex], L[i]
        i = i + 1
       
def findMinIndex(L, startIndex):
    minIndex = startIndex
    currIndex = minIndex + 1
    while currIndex < len(L):
        if L[currIndex] < L[minIndex]:
            minIndex = currIndex
        currIndex = currIndex + 1
    return minIndex

def insertionSort(L):
    i = 1
    while i < len(L):
        itemToMove = L[i]
        j = i-1
        while ((j>=0) and (itemToMove<L[j])):
            L[j+1] = L[j]
            j = j-1

        L[j+1] = itemToMove

        i = i + 1
        
    return

def mergeSort(L):
    if (len(L) < 2):
        return 
    else:
        middleIndex = len(L)//2
        left = L[:middleIndex]
        right = L[middleIndex:]
        
        mergeSort(left)
        mergeSort(right)
        
        mergedL = merge(left, right)
        
        L[:] = mergedL[:]
        return

def merge(L1, L2):
    mergedL = []
    iL1 = 0
    iL2 = 0

    while iL1 != len(L1) and iL2 != len(L2):
        if L1[iL1] <= L2[iL2]:
            mergedL.append(L1[iL1])
            iL1 = iL1 + 1
        else:
            mergedL.append(L2[iL2])
            iL2 = iL2 + 1

    mergedL.extend(L1[iL1:])
    mergedL.extend(L2[iL2:])

    return mergedL

def builtinSort(L):
    L.sort()

# code from geekviewpoint.com
def quickSort( aList ):
    _quicksort( aList, 0, len( aList ) - 1 )
 
def _quicksort( aList, first, last ):
    if first < last:
      pivot = partition( aList, first, last )
      _quicksort( aList, first, pivot - 1 )
      _quicksort( aList, pivot + 1, last )
 
 
def partition( aList, first, last ) :
    pivot = first + random.randrange( last - first + 1 )
    swap( aList, pivot, last )
    for i in range( first, last ):
      if aList[i] <= aList[last]:
        swap( aList, i, first )
        first += 1
 
    swap( aList, first, last )
    return first
 
 
def swap( A, x, y ):
  A[x],A[y]=A[y],A[x]

# code from geeksquiz.com
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
 
    if l < n and arr[i] < arr[l]:
        largest = l
 
    if r < n and arr[largest] < arr[r]:
        largest = r
 
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
 
        heapify(arr, n, largest)
 
def heapSort(arr):
    n = len(arr)

    for i in range(n, -1, -1):
        heapify(arr, n, i)
 
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


##########

import random

def mixup(L):
    newL = L[:]
    length = len(L)
    for i in range(length):
        newIndex = random.randint(i,length-1)
        newL[newIndex], newL[i] = newL[i], newL[newIndex]
    return(newL)

##########

import time

def timeSort(sortfn, L):
    t1 = time.time()
    sortfn(L)
    t2 = time.time()
    return (t2 - t1)

def timeAllSorts(L):

    Lcopy = L[:]
    sTime = timeSort(selectionSort, Lcopy)
    Lcopy = L[:]
    iTime = timeSort(insertionSort, Lcopy)
    Lcopy = L[:]
    mTime = timeSort(mergeSort, Lcopy)
    Lcopy = L[:]
    biTime = timeSort(builtinSort, Lcopy)
    
    print("{}\t sel: {:.2f}\t ins: {:.2f}\t merge: {:.2f}\t builtin: {:.2f}".format(len(L), sTime, iTime, mTime, biTime))


###### Code to test data and generate graphs of data.
import pylab

def bestCase(minN = 1000, maxN = 20000, step = 2000):
    listSizes = list(range(minN, maxN, step))
    runTimesInsertion = []
    runTimesSelection = []
    runTimesMerge = []
    runTimesBuiltIn = []
    runTimesQuick = []
    runTimesHeap = []
    for listSize in listSizes:
        listToSort = list(range(listSize))
        insertionTimes = timeSort(insertionSort, listToSort)
        runTimesInsertion.append(insertionTimes)
        selectionTimes = timeSort(selectionSort, listToSort)
        runTimesSelection.append(selectionTimes)
        mergeTimes = timeSort(mergeSort, listToSort)
        runTimesMerge.append(mergeTimes)
        builtinTimes = timeSort(builtinSort, listToSort)
        runTimesBuiltIn.append(builtinTimes)
        quickTimes = timeSort(quickSort, listToSort)
        runTimesQuick.append(quickTimes)
        heapTimes = timeSort(heapSort, listToSort)
        runTimesHeap.append(heapTimes)
    pylab.xlabel('List Size')
    pylab.ylabel('Time (seconds)')
    pylab.title('Best Case Running Times')
    pylab.plot(listSizes, runTimesInsertion, color = 'k')
    pylab.plot(listSizes, runTimesSelection, color = 'r')
    pylab.plot(listSizes, runTimesMerge, color = 'y')
    pylab.plot(listSizes, runTimesBuiltIn, color = 'g')
    pylab.plot(listSizes, runTimesQuick, color = 'b')
    pylab.plot(listSizes, runTimesHeap, color = 'm')
    pylab.show()

def averageCase(minN = 1000, maxN = 20000, step = 2000):
    listSizes = list(range(minN, maxN, step))
    runTimesInsertion = []
    runTimesSelection = []
    runTimesMerge = []
    runTimesBuiltIn = []
    runTimesQuick = []
    runTimesHeap = []
    for listSize in listSizes:
        listToSort = mixup(list(range(listSize)))
        insertionTimes = timeSort(insertionSort, listToSort)
        runTimesInsertion.append(insertionTimes)
        selectionTimes = timeSort(selectionSort, listToSort)
        runTimesSelection.append(selectionTimes)
        mergeTimes = timeSort(mergeSort, listToSort)
        runTimesMerge.append(mergeTimes)
        builtinTimes = timeSort(builtinSort, listToSort)
        runTimesBuiltIn.append(builtinTimes)
        quickTimes = timeSort(quickSort, listToSort)
        runTimesQuick.append(quickTimes)
        heapTimes = timeSort(heapSort, listToSort)
        runTimesHeap.append(heapTimes)
    pylab.xlabel('List Size')
    pylab.ylabel('Time (seconds)')
    pylab.title('Average Case Running Times')
    pylab.plot(listSizes, runTimesInsertion, color = 'k')
    pylab.plot(listSizes, runTimesSelection, color = 'r')
    pylab.plot(listSizes, runTimesMerge, color = 'y')
    pylab.plot(listSizes, runTimesBuiltIn, color = 'g')
    pylab.plot(listSizes, runTimesQuick, color = 'b')
    pylab.plot(listSizes, runTimesHeap, color = 'm')
    pylab.show()

def worstCase(minN = 1000, maxN = 20000, step = 2000):
    listSizes = list(range(minN, maxN, step))
    runTimesInsertion = []
    runTimesSelection = []
    runTimesMerge = []
    runTimesBuiltIn = []
    runTimesQuick = []
    runTimesHeap = []
    for listSize in listSizes:
        unreversedListToSort = list(range(listSize))
        listToSort = unreversedListToSort[::-1]
        insertionTimes = timeSort(insertionSort, listToSort)
        runTimesInsertion.append(insertionTimes)
        selectionTimes = timeSort(selectionSort, listToSort)
        runTimesSelection.append(selectionTimes)
        mergeTimes = timeSort(mergeSort, listToSort)
        runTimesMerge.append(mergeTimes)
        builtinTimes = timeSort(builtinSort, listToSort)
        runTimesBuiltIn.append(builtinTimes)
        quickTimes = timeSort(quickSort, listToSort)
        runTimesQuick.append(quickTimes)
        heapTimes = timeSort(heapSort, listToSort)
        runTimesHeap.append(heapTimes)
    pylab.xlabel('List Size')
    pylab.ylabel('Time (seconds)')
    pylab.title('Worst Case Running Times')
    pylab.plot(listSizes, runTimesInsertion, color = 'k')
    pylab.plot(listSizes, runTimesSelection, color = 'r')
    pylab.plot(listSizes, runTimesMerge, color = 'y')
    pylab.plot(listSizes, runTimesBuiltIn, color = 'g')
    pylab.plot(listSizes, runTimesQuick, color = 'b')
    pylab.plot(listSizes, runTimesHeap, color = 'm')
    pylab.show()

