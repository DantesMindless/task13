# task1
def xyz():
    x = 1
    y = 2
    z = 3

print(xyz.__code__.co_nlocals)
#task2

def calc(x):
    def num(y):
        nonlocal x
        x = x**2
        return x * y
    return num


func = calc(3)
print(func(10))
# task3

nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]


def choose_func(nums: list, func1, func2):
    if all(num > 0 for num in nums):
        print( func1(nums))
    else:
        print( func2(nums))


def square_nums(nums):
    return [num ** 2 for num in nums]


def remove_negatives(nums):
    return [num for num in nums if num > 0]


choose_func(nums1, square_nums, remove_negatives)

choose_func(nums2, square_nums, remove_negatives)
