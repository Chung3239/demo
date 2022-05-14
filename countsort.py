class solution:
    def CountSort(self, nums):
        bucket = [0 for _ in range(max(nums)+ 1)]
        for i in range(len(nums)):
            bucket[nums[i]] += 1
        i = 0
        for j in range(len(bucket)):
            while bucket[j] > 0:
                nums[i] = j
                bucket[j] -= 1
                i += 1
        return nums





if __name__ == "__main__":
    numbers = [5, 7, 2, 1, 1]
    a = solution()
    print(a.CountSort(numbers))