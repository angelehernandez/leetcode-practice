class Solution:
    def find_median(self, nums: list[int]) -> float:
        nums_length = len(nums)
        half_length = int(nums_length/2)

        if nums_length%2 == 0:
            left = nums[half_length - 1]
            right = nums[half_length]
            return (left + right)/2
        else:
            return nums[round(half_length)]

    def merge(self, nums1: list[int], nums2: list[int]) -> list[int]:
        merged_nums = []

        while (len(nums1) != 0) and (len(nums2) != 0):
            if nums1[0] > nums2[0]:
                merged_nums.append(nums2[0])
                nums2.pop(0)
            else:
                merged_nums.append(nums1[0])
                nums1.pop(0)

        # one of the lists are empty

        while len(nums1) != 0:
            merged_nums.append(nums1[0])
            nums1.pop(0)

        while len(nums2) != 0:
            merged_nums.append(nums2[0])
            nums2.pop(0)

        return merged_nums


    def mergeSort(self, nums: list[int]) -> list[int]:
        # Base case. A list of zero or one elements is sorted, by definition.
        if len(nums) <= 1:
            return nums

        # Recursive case. First, divide the list into equal-sized sublists
        # consisting of the first half and second half of the list.
        # This assumes lists start at index 0.
        left = []
        right = []
        for i, x in enumerate(nums):
            if i < (len(nums))/2:
                left.append(x)
            else:
                right.append(x)

        # Recursively sort both sublists.
        left = self.mergeSort(left)
        right = self.mergeSort(right)

        # Then merge the now-sorted sublists.
        return self.merge(left, right)
            
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        merged_nums = nums1 + nums2
        sorted_nums = self.mergeSort(merged_nums)
        median = self.find_median(sorted_nums)
        return median

if __name__=="__main__":
    sol = Solution()
    sol.findMedianSortedArrays([1,3], [2])