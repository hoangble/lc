class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans1 = self.get_elements_first_only(nums1, nums2)
        ans2 = self.get_elements_first_only(nums2, nums1)
        return[list(ans1), list(ans2)]

    
    def get_elements_first_only(self, nums1, nums2):
        num1_only = set()
        exist_in_num2 = set(nums2)

        for n in nums1:
            if n not in exist_in_num2:
                num1_only.add(n)
        return num1_only
