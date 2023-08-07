def hoare_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]
    less, equal, greater = partition(arr[:-1], pivot)
    return hoare_sort(less) + equal + hoare_sort(greater)

def partition(arr, pivot):
    less, equal, greater = [], [], []
    for x in arr:
        if x < pivot:
            less.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            greater.append(x)
    return less, equal, greater


numbers = [5, 8, 9, 4, 2, 9, 1, 8]
sorted_numbers = hoare_sort(numbers)
print(sorted_numbers) 