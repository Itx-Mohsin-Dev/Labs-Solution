print("\nP1")
# for i in range(1500,2701):
#     if (i%5==0) and (i%7==0):
#         print(i)

print("\nP2")
# msg = input("Enter the temperature in Celsius")
# f = (int(msg)/5)*9+32
# print(msg,"`C is equal to",f,"`F")

# msg1 = input("Enter the temperature in fahrenhiet")
# c = ((int(msg1)-32)/9)*5
# print(msg1,"`F is equal to ",c,"`C")


print("\nP3")
# f = 0
# while(f == 0):
#     n = int(input("Guess a number: "))
#     for i in range(1,10):
#         if i == n:
#             f = 1
#             print("well guessed ")
#             break 


print("\nP4")
# for i in range(5):
#     for j in range(i+1):
#         print("*",end="")
#     print("\n")

# k = 4
# for i in range(4):
#     for j in range(k):
#         print("*",end="")
#     k = k-1
#     print("\n")


print("\nP5 Sol1")
# output = ""
# word = input("Enter a word: ")
# length = len(word)
# k = 0
# l = length - 1

# # Create a list to hold the characters
# output_list = []
# for i in range(length):
#     output_list.append(word[l])  # Append the character from the end of the word
#     k += 1
#     l -= 1

# # Join the list into a string
# output = ''.join(output_list)
# print(output)


    
print("\nP5 Sol2")
# word = input("Enter a word")
# reversed_word = word[::-1]
# print("Reversed word is : ",reversed_word)
    
# a = input("Enter something")
# print(type(a))


print("\nP6")
# even = 0
# odd = 0
# numbers = (1,2,3,4,5,6,7,8,9,10)
# for i in range(len(numbers)):
#     if numbers[i]%2 == 0:
#         even = even + 1

# for i in numbers:
#     if i%2 != 0:
#         odd = odd + 1 

# print("\nEven numbers are : ",even)
# print("\nOdd numbers are : ",odd)

print("\nP7")
# datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0,-1), [5,12], {"class":'V',"section":'A'}]
# for i in datalist:
#     print(i," -> ",type(i))

print("\nP8")
# for i in range(7):
#     if i == 3 or i == 6:
#         continue
#     print(i,end=" ")

print("\nP9")
# f1 = 1
# print(f1,end=" ")
# f2 = 1
# print(f2,end=" ")
# f3 = f1 + f2
# while(f3 <= 50):
#     print(f3,end=" ")
#     f1 = f2
#     f2 = f3
#     f3 = f1 + f2


print("\nP9 Part")
# for i in range(1,51):
#     if i%3 == 0 and i%5 == 0:
#         print("FizzBuzz",end=" ")
#         continue
#     elif i%3 == 0:
#         print("Fizz",end=" ")
#         continue
#     elif i%5 == 0:
#         print("Buzz",end=" ")
#         continue
#     else :
#         print(i,end=" ") 


print("\nP10")
# l = []
# m = int(input("Enter rows: "))
# n = int(input("Enter Columns: "))
# for i in range(m):
#     row = []
#     for j in range(n):
#         row.append(i*j)
    
#     l.append(row)

# print(l)



print("\nP11")
# word = ""
# list = []
# list1 = []
# while(True):
#     word = input("Enter a word: ")
#     if(word == ""):
#         break 
#     list.append(word)

# for i in range(len(list)):
#     list1.append(list[i].lower())

# for i in range(len(list)):
#     print(list1[i],end=" ... ")


print("\nP12")
# l = []
# x = 0
# while(True):
#     dig = input("Enter a 4 digit binary number: ")
#     if dig == "":
#         break
#     l.append(dig)

# for i in range(len(l)):
#     dig = l[i]
#     if dig[0] == '1':
#         x += 8
#     if dig[1] == '1':
#         x += 4
#     if dig[2] == '1':
#         x += 2
#     if dig[3] == '1':
#         x += 1
    
#     if x%5 == 0:
#         print(dig," is divisible by 5")


print("\nP13")
# letter = 0
# digit = 0
# words = 1
# word = input("Enter a word: ")
# word = word.lower()
# for i in range(len(word)):
#     if word[i] >= 'a' and word[i] <= 'z':
#         letter = letter + 1
#     elif word[i] >= '0' and word[i] <= '9':
#         digit = digit + 1
#     elif word[i] == ' ':
#         words += 1

# print("Number of letters: ", letter)
# print("Number of digits: ", digit)
# print("Number of words: ", words)


print("\nP14")
a = 0
b = 0
c = 0
d = 0
password = input("Enter your password: ")
length = len(password)
if length > 6 and length < 16:
    for i in range(length):
        if password[i] >= 'a' and password[i] <= 'z':
            a = 1
            break        
    if a == 0:
        print("Invalid password...Your password should have a lower case letter!!!") 
    else:
        for i in range(length):
            if password[i] >= 'A' and password[i] <= 'Z':
                b = 1
                break 
        if b == 0:
            print("Invalid password...Your password should have an upper case letter!!!")
        else:
            for i in range(length):
                if password[i] >= '0' and password[i] <= '9':
                    c = 1
                    break
            if c == 0:
                print("Invalid password...Your password should have a digit!!!")
            else:
                for i in range(length):
                    if password[i] == '$' or password[i] == '@' or password[i] == '#':
                        d = 1
                        break
                if d == 0:
                    print("Invalid password...Your password should have a special character!!!")
                else:
                    print("Correct Password")
else:
        print("Invalid password...Your password should be between 6 and 16 characters!!!")

