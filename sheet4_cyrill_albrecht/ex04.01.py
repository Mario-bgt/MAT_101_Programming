def search(arr, target):
    highest_element = len(arr) - 1
    lowest_element = 0
    while lowest_element <= highest_element:
        middle_element = (lowest_element + highest_element) // 2
        if arr[middle_element] > target:
            highest_element = middle_element - 1
        elif arr[middle_element] < target:
            lowest_element = middle_element + 1
        else:
            print(f"Target {target} is at index {middle_element}")
            return middle_element
    print(f"Target {target} is not in the list")
    return None


search([1, 3, 4, 68, 87, 421, 12345, 34567], 12345)
