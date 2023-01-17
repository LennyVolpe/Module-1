"""Write a script that takes in a string from the user. Print the string where all the lower case letters are shifted to the front and the spaces removed
 Keep the relative order of the lower case letters and upper case letters.
 how i fouind is upper: 
 https://www.geeksforgeeks.org/isupper-islower-lower-upper-python-applications/
 """

string1 = str(input("Enter a string: "))

string2 = str("") 
string3 = str("")

for x in string1:
    if x.isupper():
        string3+=x
    if x.islower():
        string2+= x

print(string2+string3)