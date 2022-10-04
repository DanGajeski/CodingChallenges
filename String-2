#Given a string, return a string where for every char in the original, there are two chars.

def double_char(str):
  new_string = ''
  for i in range(len(str)):
    new_string = new_string + str[i] + str[i]
  return new_string
  








#Return the number of times that the string "hi" appears anywhere in the given string.

def count_hi(str):
  hi_count = 0
  for i in range(len(str) - 1):
    if str[i:i+2] == "hi":
      hi_count += 1
  return hi_count
  









#Return True if the string "cat" and "dog" appear the same number of times in the given string.

def cat_dog(str):
  cat_num = 0
  dog_num = 0
  for i in range(len(str) - 2):
    if str[i:i+3] == "cat":
      cat_num += 1
    if str[i:i+3] == "dog":
      dog_num += 1
  if cat_num == dog_num:
    return True
  else:
    return False
    
 
 
 
 
 
 
 
 
 
#Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.

def count_code(str):
  f2 = "co"
  l1 = 'e'
  cool_count = 0
  for i in range(len(str) - 3):
    if str[i:i+2] == f2 and str[i+3] == l1:
      cool_count += 1
  return cool_count
  








#Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences 
#(in other words, the computation should not be "case sensitive"). Note: s.lower() returns the lowercase version of a string.

def end_other(a, b):
  if len(a) > len(b):
    if b.lower() == a[(len(a) - len(b)):].lower():
      return True
    else:
      return False
  elif len(b) > len(a):
    if a.lower() == b[(len(b) - len(a)):].lower():
      return True
    else:
      return False
  else:
    if a.lower() == b.lower():
      return True
    else:
      return False
      









#Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.

def xyz_there(str):
  for i in range(len(str) - 2):
    if str[i:i+3] == "xyz" and str[i-1] != '.':
      return True
  return False
