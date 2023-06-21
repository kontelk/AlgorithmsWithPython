def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]

    # Recursively sort the left and right halves
    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    # Merge smaller elements first
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # If there are leftover elements in either array, add them to the result
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1

    return result


numbers = [10, 2, 1, 5, 7, 3, 4, 8, 6, 9]
sorted_numbers = merge_sort(numbers)
print(sorted_numbers)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

