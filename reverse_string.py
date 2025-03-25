def reverse_string(s):
   reverse_str=""
   for i in s:
      reverse_str=i+reverse_str
   return reverse_str
string=input("Enter a string:") 
print("the reverse string is:",reverse_string(string))
