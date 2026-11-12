class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num_zeros = 0
        index_zeros = []
        for i in range(len(nums)):
            if nums[i] == 0:
                num_zeros += 1
                index_zeros.append(i)

        if num_zeros == 0:
            product = 1
            for num in nums:
                product *= num
            return [int(product / nums[i]) for i in range(len(nums))]
        elif num_zeros == 1:
            product = 1
            for i in range(len(nums)):
                if i != index_zeros[0]:
                    product *= nums[i]
            result = [0 for i in range(len(nums))]
            result[index_zeros[0]] = product
            return result
        else:
            return [0 for i in range(len(nums))]