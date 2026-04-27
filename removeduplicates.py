def remove_duplicates(arr):
    result = []
    for num in arr:
        if num not in result:
            result.append(num)
    return result

print(remove_duplicates([1, 2, 2, 3, 4, 4]))