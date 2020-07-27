def add(num):
    nums = num.split("+")
    print(int(nums[0]) + int(nums[1]))

def decrease(num):
    nums = num.split("-")
    print(int(nums[0]) - int(nums[1]))

    
def mult(num):
    nums = num.split("*")
    print(int(nums[0]) * int(nums[1]))

def devision(num):
    nums = num.split("/")
    print(int(nums[0]) / int(nums[1]))
def remain(num):
    nums = num.split("%")
    print(int(nums[0]) % int(nums[1]))
def tavan(num):
    nums = num.split("**")
    print(int(nums[0]) ** int(nums[1]))

while True:
    num = input("Operator: ")
    nums = num.split(' ')
    if '+' in nums:
        add(num)
    elif '-' in nums:
        decrease(num)
    elif '*' in nums:
        mult(num)
    elif '/' in nums:
        devision(num)
    elif '%' in nums:
        remain(num)
    elif '**' in nums:
        tavan(num)
