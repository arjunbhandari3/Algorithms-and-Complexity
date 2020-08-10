
def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1


def binary_search(data, left, right, target):
    # base case
    if right >= left:
        # middle element
        middle = (right + left) // 2

        # at the middle
        if data[middle] == target:
            return middle

        # in right subarray
        elif data[middle] < target:
            return binary_search(data, middle+1, right, target)

        # in left subarray
        else:
            return binary_search(data, left, middle-1, target)

    else:
        # not present in the array
        return -1
