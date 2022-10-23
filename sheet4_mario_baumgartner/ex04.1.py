def search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            print(f"Element {x} is present at index {mid}")
            return mid
    print(f"Element {x} is not present in the array")
    return None


print(search([2, 3, 4, 10, 40], 1))
