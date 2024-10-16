
def bubble_sort(arr):
    n = len(arr)

    # Traverse through all elements in the list
    for i in range(n):
        # Flag to check if swapping happens, helps in optimizing the algorithm
        swapped = False

        # Last i elements are already sorted
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        # If no two elements were swapped, the list is already sorted
        if not swapped:
            break

    # Return the sorted list
    return arr


