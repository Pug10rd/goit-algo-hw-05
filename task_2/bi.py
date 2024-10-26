
def binary_search_with_upper_bound(array, target):
    left, right = 0, len(array) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = (left + right) // 2

        if array[mid] == target:
            return (iterations, array[mid])
        
        if array[mid] < target:
            left = mid + 1
        else:
            upper_bound = array[mid]
            right = mid - 1

    return (iterations, upper_bound)


array = [1.2, 2.5, 3.8, 4.6, 5.1, 6.3, 7.4, 9.0]
print(binary_search_with_upper_bound(array, 3.8)) 
print(binary_search_with_upper_bound(array, 5.4)) # дає upper_bound 6.3 згідно логіки бінарного пошуку
