#Given a string and a non-negative int n, return a larger string that is n copies of the original string.

def string_times(str, n):
  copies = ''
  count = list(range(0, n))
  # OR for i in range(n):
  for number in count:
    copies = copies + str
    # OR copies += str
    
  return copies










#Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars,
#or whatever is there if the string is less than length 3. Return n copies of the front;

def front_times(str, n):
  front_copies = ''
  front = str[:3] # slice ignores out of range instances
  for i in range(n):
    front_copies += front
    
  return front_copies
  









#Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".

def string_bits(str):
  every_other = ''
  every_other_two = ''
  
  
  num_of_chars = len(str)
  num_every_other = range(0, num_of_chars, 2)
  for char in num_every_other:
    every_other += str[char]
    
  return every_other
  








#Given a non-empty string like "Code" return a string like "CCoCodCode".

def string_splosion(str):
  str_list_len = range(len(str))
  sploded_word = ''
  for i in str_list_len:
    sploded_word += str[:i + 1]
    
  return sploded_word
  









#Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, 
#so "hixxxhi" yields 1 (we won't count the end substring).

def last2(str):
  if len(str) < 3:
    return 0
  else:
    last_2 = str[-2:]
    last_2_end = str.rfind(last_2)
  
    index = 0
    count = 0
    start = 0
    while index != last_2_end:
    #count = 0
      index = str.find(last_2, start)
      count += 1
      start = index + 1

    return count - 1
    









#Given an array of ints, return the number of 9's in the array.

def array_count9(nums):
  nine_count = 0
  for n in nums:
    if n == 9:
      nine_count += 1
  return nine_count
  









#Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.

def array_front9(nums):
  if 9 in nums[:4]:
    return True
  else:
    return False
    








#Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.

def array123(nums):
  for n in range(len(nums)-2):
    if nums[n] == 1 and nums[n+1] == 2 and nums[n+2] == 3:
      return True
  return False
  









#Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. 
#So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.

def string_match(a, b):
  double_count = 0
  target_string = min(len(a), len(b))
  for i in range(target_string - 1):
    if a[i] == b[i] and a[i+1] == b[i+1]:
      double_count += 1
  return double_count
