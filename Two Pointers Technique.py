# https://afteracademy.com/blog/what-is-the-two-pointer-technique


"""Computation starts and the start and at the end of the array."""
def naiveTwoPointers(arr, num) -> bool:
    """O(n**2) complexity due to two loops."""
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            print(arr[i], arr[j])
            if arr[i]+arr[j] == num:
                return True
    return False


def effectiveBruteTwoPointers(arr, num) -> bool:
    """O(n) complexity. """
    start = 0
    end = len(arr)-1

    while start < end:
        current_sum = arr[start]+arr[end]
        if current_sum == num:
            return True
        elif current_sum > num:
            end -= 1
        elif current_sum < num:
            start += 1
    return False


if __name__ == "__main__":
    print(effectiveBruteTwoPointers(arr=[2, 1, 2, 1], num=3)
          )

