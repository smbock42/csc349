import sys
# [1]
# [1,1,2]
# [1,2,2] - 2
# [1,1,2,3,3] - 4
# [1,1,2,2,3]
# [1,1,2,2,3,3,4] - 6
# [1,2,2,3,3,4,4]
# [1,2,2,3,3,4,4,5,5] -8
# []

def main():
    filename = sys.argv[1]
    with open(filename) as file:
        numbers = [line.rstrip() for line in file]
    #number = recurse(numbers, 0, len(numbers)-1)
    number = recurse(numbers)
    
    print(number)
    return number

# 1,1,2,2,3 = mid = 2
# 1,2,2,3,3 = mid = 2
# 1,2,2,3,3,4,4 -mid = 3 -1
# 1,2,2,3,3,4,4,5,5
# 1,2,2,3,3,
def recurse(arr):
    
    if len(arr) == 1:
        return arr[0]

    mid = len(arr)//2
    #check if mid is even
    if mid %2 != 0:
        #if odd, make mid even
        mid -= 1
    mid_value = arr[mid]
    prev_value = arr[mid-1]
    next_value = arr[mid+1]
    if mid_value != prev_value and mid_value != next_value:
        return mid_value
    if mid_value == next_value:
        return recurse(arr[mid+2:])
    else:
        return recurse(arr[:mid-1])


    


if __name__ == "__main__":
    main()
