# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    for i in range(elements):
        if len(arrA) == 0 or len(arrB) == 0:
            return merged_arr[:i] + arrA + arrB
        if arrA[0] > arrB[0]:
            merged_arr[i] = arrB.pop(0)
        else:
            merged_arr[i] = arrA.pop(0)
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO

    l = len(arr)
    if l > 1:
        new_arr = l // 2
        leftarr = arr[:new_arr]
        rightarr = arr[new_arr:]
        arrA = merge_sort(leftarr)
        arrB = merge_sort(rightarr)
        arr = merge(arrA, arrB)
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
