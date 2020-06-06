# Github repository- Lavanya-B

def selectionSort(l):

    result = l[:]

    for elementIndex in range((len(result) - 1)):
        value = result[elementIndex]
        lowerIndex = elementIndex
        swapIndex  = None
        while lowerIndex < len(result):
            if result[lowerIndex] < value:
                value = result[lowerIndex]
                swapIndex = lowerIndex
            lowerIndex += 1
        if value != result[elementIndex]:
            result[swapIndex] = result[elementIndex]
            result[elementIndex] = value

    return result



print(selectionSort([33, 20, 12, 31, 2, 67]))