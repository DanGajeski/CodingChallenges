#Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.

def count_evens(nums):
  even_count = 0
  for n in nums:
    if n % 2 == 0:
      even_count += 1
  return even_count
  









#Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array. 
#Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.

def big_diff(nums):
	prev_min = nums[0]
	prev_max = nums[0]
	for n in nums:
		prev_min = min(prev_min, n)
		prev_max = max(prev_max, n)
	return prev_max - prev_min
  









#Return the "centered" average of an array of ints, which we'll say is the mean average of the values, 
#except ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value, 
#ignore just one copy, and likewise for the largest value. Use int division to produce the final average. You may assume that the array is length 3 or more.

def centered_average(nums):
  cur_min = nums[0]
  cur_max = nums[0]
  cur_sum = 0
  for n in nums:
    cur_min = min(cur_min, n)
    cur_max = max(cur_max, n)
    cur_sum += n
      
  return (cur_sum - cur_min - cur_max) / (len(nums) - 2)
  
  








#Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, 
#so it does not count and numbers that come immediately after a 13 also do not count.

def sum13(nums):
  sum_nums = 0
  for i in range(len(nums)):
    if nums[i] == 13:
      sum_nums += 0
    else:
      if nums[i-1] == 13 and i != 0:
        sum_nums += 0
      else:
        sum_nums += nums[i]
  return sum_nums
  
  








#Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 
#(every 6 will be followed by at least one 7). Return 0 for no numbers.

def sum67(nums):
  total = 0
  skiptoindex = -1
  for i in range(len(nums)):
    if nums[i] == 6 and i > skiptoindex:
      total += 0
      skiptoindex = nums[i:].index(7) + i
    else:
      if i > skiptoindex:
        total += nums[i]
      else:
        total += 0
  return total
  








#Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.

def has22(nums):
  for i in range(len(nums) - 1):
    if nums[i] == 2 and nums[i+1] == 2:
      return True
  else:
    return False
