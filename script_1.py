"""Write a script that takes in a string from the user. Print the string out backwards.
how i found [::-1] https://www.w3schools.com/python/python_howto_reverse_string.asp
"""

string= str(input("Enter a string: "))
"""[::-1] creates a slice that movers from the end of string to the front"""
string2 = string[::-1]

print(string2)