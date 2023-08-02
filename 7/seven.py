def my_zip(s, nums):
    return ((s[i], nums[i]) for i in range(min(len(s), len(nums))))


string = "abcd"
numbers = (10, 20, 30, 40)

gen = my_zip(string, numbers)

print(gen)
for pair in gen:
    print(pair)