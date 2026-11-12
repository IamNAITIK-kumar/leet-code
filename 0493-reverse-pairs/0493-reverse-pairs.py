
class Solution(object):

    def merge(self, nums, low, mid, high):
        left = low
        right = mid + 1
        temp = []

        while left <= mid and right <= high:

            if nums[left] <= nums[right]:
                temp.append(nums[left])
                left += 1

            else:
                temp.append(nums[right])
                right += 1

        while left <= mid:
            temp.append(nums[left])
            left += 1

        while right <= high:
            temp.append(nums[right])
            right += 1

        for i in range(low, high + 1):
            nums[i] = temp[i - low]

    def countpairs(self, nums, low, mid, high):

        right = mid + 1

        for i in range(low, mid + 1):

            while right <= high and nums[i] > 2 * nums[right]:
                right += 1

            self.cnt += (right - (mid + 1))

    def merge_sort(self, nums, low, high):

        if low >= high:
            return

        mid = (low + high) // 2

        self.merge_sort(nums, low, mid)
        self.merge_sort(nums, mid + 1, high)

        self.countpairs(nums, low, mid, high)
        self.merge(nums, low, mid, high)

    def reversePairs(self, nums):
        self.cnt = 0

        n = len(nums)

        self.merge_sort(nums, 0, n - 1)

        return self.cnt
