class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # length of the input list
        length = len(nums)
        
        # The answer array to be returned
        answer = [0]*length
        
        # answer[i] is initially the product of all numbers before i
        answer[0] = 1
        for i in range(1, length):
            answer[i] = nums[i - 1] * answer[i - 1]
        
        # R contains the product of all numbers after i
        R = 1;
        for i in reversed(range(length)):
            # For the index 'i', answer[i] contains the product of all numbers before i
            # R contains the product of all numbers after i
            answer[i] = answer[i] * R
            # R now contains the product of all numbers after i+1
            R *= nums[i]
        
        return answer
