#(1:-) write a program to find the sum of all even numbers up to 50

# sum = 0
# for i in range(0,51):
#     if i % 2 == 0:
#         sum += i
# print("The sum of all even numbers up to 50 is:", sum)

#(2:-) write a program to find the sum of all odd numbers up to 50

# sum = 0
# for i in range(0, 51):
#     if i % 2 != 0:
#         sum += i
# print("The sum of all odd numbers up to 50 is:", sum)

#(3:-) write a program to find the 20 numbers in the  and there squired numbers

# for i in range(1, 21):
#     print(f"The number is {i} and its square is {i**2}")

# (4:-) Fibonacci series using a simple loop

# n = int(input("Kitne terms chahiye? "))

# a = 0
# b = 1
# print("Fibonacci series:")
# for i in range(n):
#     temp = a+b
#     a = b
#     b = temp
#     print(a, end=" ")


#(5:-) write a program to check whether a number is prime or not
# num = int(input("Enter a number: "))

# if num > 1:
#     for i in range(2, num):
#         if (num % i) == 0:
#             print(num, "is not a prime number")
#             break
#     else:
#         print(num, "is a prime number")
# else:
#     print(num, "is not a prime number")

#(6:-) write a program to find the factorial of a number

# num = int(input("Enter a number to find its factorial: "))
# fact = 1
# for i in range(1, num+1):
#     fact *= i
#     print(f"The factorial of", fact)

#(7:-) write a program to find the sum of digits of a number

# num = int(input("Enter a number to find the sum of its digits: "))

# sum = 0
# while num > 0 :
#     digit = num % 10
#     sum += digit
#     num //= 10
# print(f"The sum of the digits is: {sum}")

#(8:-) write a program to find the reverse of a number

# num = int(input("Enter a number to find its reverse: "))
# reverse = 0
# while num > 0:
#     digit = num%10
#     reverse = reverse * 10 + digit
#     num //= 10
# print(f"The reverse of the number is: {reverse}")