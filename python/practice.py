# 3. Determine if a number is even or odd:
#    - Using the modulus operator (`%`).
#    - Using the floor division method.
#    - Using bitwise operations (`&`).
# a=6
# if a&2==0:
#     print("this is even number")
# else:
#     print("this is odd number")

# 4. Check if a number is positive or negative.
# n=int(input("enter a value:"))
# if n>0:
#     if n<0:
#         print("negative number is:",n)
#     else:
#         print("positive number is:",n)
# else:
#     print("negative number is:",n)
# 5)5. Find the maximum of three numbers.
# a=(5,3,4,9)
# print(max(a))
# 6. Print the multiplication table of a given number.
# for i in range(1,11):
#     print("18 *",i,"=",18*i)


# 9. Count even numbers in a given range.
# count=0
# for i in range(1,10):
#     if i%2==0:
#         print(i)
#         count=count+1
# print("count of even numbers:",count)
# 10. Count odd numbers in a given range.
# count=0
# for i in range(1,11):
#     if i%2!=0:
#         print(i)
#         count=count+1
# print("total odd numbers are:",count)

# 11. Swap two variables without using a temporary variable.
# a=10
# b=20
# a,b=b,a
# print(a,b)

# 12. Use the ternary operator for decision-making.
# a=1
# result="True" if a>2 else "False"
# print(result)





# date=19-05-2025
# 1)(1,10)sum of odd numbers
# sum=0
# for i  in range(1,11):
#     if i %2!=0:
#         print(i)
#         sum=sum+i
# print("total odd numbers:",sum)

# 2)sum of even numbers from(1,10)
# sum=0
# for i in range(1,11):
#     if i%2==0:
#         print(i)
#         sum=sum+i
# print("sum of even numbers:",sum)

# 3)sum of all digits
# sum=0
# for i in range(1,11):
#     print(i)
#     sum=sum+i
# print("sum of all numbers:",sum)
# 4)find the greatest of 2 numbers
# num1,num2=20,40
# if num1>num2:
#     print(num1)
# else:
#     print(num2)
# 5)find the greatest of three numbers/
# num1,num2,num3=40,60,50
# if num1>num2:
#     print(num1)
# elif num2>num3:
#     print(num2)
# else:
#     print(num3)

# 6)print(1,10) prime numbers
# for num in range(2, 11):
#     is_prime = True  # Assume number is prime

#     # Check if divisible by any number between 2 and num - 1
#     for i in range(2, num):
#         if num % i == 0:
#             is_prime = False  # Found a divisor, so not prime
#             break  # No need to check further

#     # If is_prime is still True, print the number
#     if is_prime:
#         print(num)

# 7)Chech whether the year is leap year or not
# year=2021
# if year%400==0:
#     if year%100==0:
#         if year%4000==0:
#             print("leap year")
#         else:
#             print("not a leap year")
#     else:
#         print("not a leap year")
# else:
#     print(" not a leap year")
# 8). Find all even numbers within a specified range.
# for i in range(10,20):
#     if(i%2==0):
#         print(i)

# 9)Find all odd numbers within a specified range
# for i in range(10,20):
#     if i%2!=0:
#         print(i)

# 9). Count even numbers in a given range.
# count=0
# for i in range(10,20):
#     if i%2==0:
#         print(i)
#         count=count+1
# print("the count of even numbers are:",count)

# 20. Reverse a number.
# for i in range(10,1,-1):
#     print(i)
# 21. Check if a number is a palindrome.


