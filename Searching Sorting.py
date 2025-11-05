account_ids = [107, 203, 145, 322, 210, 178, 290, 155]

def linear_search(arr, target):
    for i in arr:
        if i == target:
            return True
    return False

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

search_id = 210
print("Linear Search:", linear_search(account_ids, search_id))

sorted_ids = sorted(account_ids)
print("Binary Search:", binary_search(sorted_ids, search_id))