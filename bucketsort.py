class solution:
    def bucketsort(self, nums, bucksize = 100):
        if not nums:
            return
        bucket = []
        bucketcount = (max(nums) - min(nums)) // bucksize +1

        for i in range(bucketcount):
            bucket.append([])
        for i in range(len(nums)):
            bucket[nums[i]//bucksize].append(nums[i])
        nums.clear()
        for i in range(len(bucket)):
            bucket[i].sort()
            nums.extend(bucket[i])

        


        return nums



if __name__ == '__main__':
    a = solution()
    numbers = [12, 321, 432, 5, 43, 6, 45, 765, 7, 65, 876, 8, 67, 98, 679, 87, 987, 9]
    print(a.bucketsort(numbers))