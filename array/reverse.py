'''
Input  : arr[] = {1, 2, 3}
Output : arr[] = {3, 2, 1}

Input :  arr[] = {4, 5, 1, 2}
Output : arr[] = {2, 1, 5, 4}
'''
def reverse_array(array, start, end):
    if start >= end:
        return

    # in-place reversal, as it doesn't create a new copy of the array
    # it just swaps the element in-place, so it doesn't require any extra space.
    array[start], array[end] = array[end], array[start]
    reverse_array(array, start+1, end-1)

# the function is called recursively n/2 times -> O(n)
# function calls are added to the call stack, as the function is called n/2 times
# the max depth of the call stack is n/2

arr = [1, 2, 3, 4, 5, 6]
reverse_array(arr, 0, len(arr)-1)
print(arr)
