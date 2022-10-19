import time
st = time.time()


def search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (high + low) // 2
        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1
        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1
        # means x is present at mid
        else:
            print(f"Element {x} is present at index {mid}")
            return mid
    # If we reach here, then the element was not present
    print(f"Element {x} is not present in the array")
    return None


print(search([2, 3, 4, 10, 40], 1))
et = time.time()
end_time = st-et
print(end_time)
