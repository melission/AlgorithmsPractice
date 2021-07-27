# https://afteracademy.com/blog/what-is-the-two-pointer-technique

def naiveTwoPointers(arr, num) -> bool:
    """O(n**2) complexity due to two loops"""
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            print(arr[i], arr[j])
            if arr[i]+arr[j] == num:
                return True
    return False



if __name__ == "__main__":
    print(naiveTwoPointers(arr=[2, 1, 2, 1], num=3)
          )

