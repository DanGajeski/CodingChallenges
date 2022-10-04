#Given an array of ints, return True if 6 appears as either the first or last element in the array. The array will be length 1 or more.

def first_last6(nums):
  if nums[0] == 6 or nums[len(nums)-1] == 6:
    return True
  else:
    return False
    








#Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal.

def same_first_last(nums):
  if len(nums) == 1:
    return True
  elif len(nums) > 1  and nums[0] == nums[len(nums)-1]:
    return True
  else:
    return False
    








#Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}.

def make_pi():
  return [3,1,4]
  









#Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last element. Both arrays will be length 1 or more.

def common_end(a, b):
  if a[0] == b[0] or a[len(a) - 1] == b[len(b) - 1]:
    return True
  else:
    return False
    









#Given an array of ints length 3, return the sum of all the elements.

def sum3(nums):
  return nums[0] + nums[1] + nums[2]
  








#Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.

def rotate_left3(nums):
  new_nums = nums[1:]
  new_nums.append(nums[0])
  return new_nums
  








#Given an array of ints length 3, return a new array with the elements in reverse order, so {1, 2, 3} becomes {3, 2, 1}.

def reverse3(nums):
  reverse_nums = []
  reverse_nums.append(nums[2])
  reverse_nums.append(nums[1])
  reverse_nums.append(nums[0])
  return reverse_nums
  








#Given an array of ints length 3, figure out which is larger, the first or last element in the array, and set all the other elements to be that value. 
#Return the changed array.

def max_end3(nums):
  max_list = []
  if nums[0] > nums[len(nums)-1]:
    for n in nums:
      max_list.append(nums[0])
  else:
    for n in nums:
      max_list.append(nums[len(nums)-1])
  return max_list
  







#Given an array of ints, return the sum of the first 2 elements in the array. If the array length is less than 2, 
#just sum up the elements that exist, returning 0 if the array is length 0.

def sum2(nums):
  if len(nums) > 1:
    return nums[0] + nums[1]
  elif len(nums) == 1:
    return nums[0]
  else:
    return 0
    








#Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements.

def middle_way(a, b):
  middle_array = []
  middle_array.append(a[1])
  middle_array.append(b[1])
  return middle_array
  









#Given an array of ints, return a new array length 2 containing the first and last elements from the original array. 
#The original array will be length 1 or more.

def make_ends(nums):
  first_last_array = []
  if len(nums) == 1:
    first_last_array.append(nums[0])
    first_last_array.append(nums[0])
    return first_last_array
  elif len(nums) > 1:
    first_last_array.append(nums[0])
    first_last_array.append(nums[len(nums) - 1])
    return first_last_array
    








#Given an int array length 2, return True if it contains a 2 or a 3.

def has23(nums):
  if nums[0] == 2 or nums[0] == 3 or nums[1] == 2 or nums[1] == 3:
    return True
  else:
    return False
