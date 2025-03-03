nums1: list[int] = []
nums: list[int] = [1, 3, 2, 5, 4]

num: int = nums[1]
nums[1] = 0

nums.clear()
nums.append(1)
nums.append(3)
nums.append(2)
nums.append(5)
nums.append(4)

nums.insert(3, 6)

nums.pop(3)

count = 0
for i in range(len(nums)):
    count += nums[i]

for num in nums:
    count += num

nums1: list[int] = [6, 8, 7, 10, 9]
nums += nums1
nums.sort()
