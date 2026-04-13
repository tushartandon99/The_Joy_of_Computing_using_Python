#anagram --> ek hi word ke letters se dusra word banana (listen -> silent)

str1=input("Enter the First string : ")
str2= input("Enter the second string : ")
if(sorted(str1)==sorted(str2)):
    print("These are Anagrams")
else:
    print("These are not anagrams")
