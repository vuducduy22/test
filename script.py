def twoSum(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                return[i, j]
    return None

if __name__ =="__main__":
    # Test case 1: Basic case
    nums1 = [2, 7, 11, 15]
    

                