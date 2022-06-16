"""
def twoSum(nums, target):  
        values = {}
        for index, value in enumerate(nums):
            if target - value in values:
                return [values[target - value], index]
            else:
                values[value] = index

print(twoSum([3,2,4],6))

def maxSubArray(nums):
        
        :type nums: List[int]
        :rtype: int
        
        if len(nums) == 1:
            return nums[0]
            
        sum_result = [0 for i in range(len(nums))]
        sum_result[0] = nums[0]
        for i in range(1,len(nums)):
            if sum_result[i-1] < 0:
                sum_result[i] = nums[i]
            else:
                sum_result[i] = sum_result[i-1] + nums[i]
        return max(sum_result),sum_result
        
    *** second Way
    
        sum_result = nums[0]
        result = 0
        for i in range(1,len(nums)):
          sum_result = max(nums[i], sum_result + nums[i]);
          result = max(result, sum_result);
        return result
print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))


def moveZeroes(nums):
        
        #Do not return anything, modify nums in-place instead.
        
        nums.sort(key=lambda n:n==0)
        return nums
print("move zeroes: ", moveZeroes([0,1,0,3,12]))


def containsDuplicate(nums):
    return len(set(nums)) == len(nums)
print(containsDuplicate([1,2,3,1]))

def rotate(nums,k):
    k = k % len(nums)
    nums[:]  = nums[-k:] + nums[:-k]
    return nums
print(rotate([1,2,3,4,5],2))

def find_longest_word(word_list):  
    longest_word =  max(word_list.split(), key=len)
    return longest_word
print(find_longest_word("fun&!! time"))
print(find_longest_word("I love dogs"))

def get_first_duplicate(array):
    seen = set()
    for i in array:
        if i in seen:
            return i
        seen.add(i)
    return -1
print(get_first_duplicate([2,4,2,5,7,17,17]))
""" 