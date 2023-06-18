
def merge_sort(input_list):
    if len(input_list) <= 1:
        return input_list
    mid = len(input_list) // 2
    left_half = input_list[:mid]
    right_half = input_list[mid:]
    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0
    # Merge smaller elements first
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    # If there are remaining elements in left or right half, append them to the result
    if left:
        merged.extend(left[left_index:])
    if right:
        merged.extend(right[right_index:])

    return merged


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    numbers = [5, 2, 8, 3, 1, 9, 4, 7, 6]
    sorted_numbers = merge_sort(numbers)
    print(sorted_numbers)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

