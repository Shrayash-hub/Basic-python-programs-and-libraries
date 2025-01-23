#checking palindrome
def palin(s):
  return s == s[::-1]

string = "racecar"
if palin(string):
  print("the string is palindrome")
else:
  print("string is not palindrome")
