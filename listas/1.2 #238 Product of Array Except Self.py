class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        
        resultado =[1]*len(nums)
        pri=1

        for i in range(len(nums)):
            resultado[i]=pri
            pri *= nums[i]

        prd=1
        for i in reversed(range(len(nums))):
            resultado[i] *=prd
            prd *= nums[i]

        return resultado