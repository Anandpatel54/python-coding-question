#(1:-) write a program to check whether a number is positive, negative, or zero

# num = int(input("Enter a number: "))

# if num > 0:
#     print("The number is positive.")
# elif num == 0:
#     print("The number is zero.")
# else:
#     print("The number is negative.")


#(2:-) write a program to check weathe even or odd number

# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print("The number is even.")
# else:
#     print("The number is odd.")

#(3:-) write a program to check whether a number is divisible by 5 and 11

# num = int(input("Enter a number: "))
# if num % 5 == 0 and num % 11 == 0:
#     print("The number is divisible by both 5 and 11.")
# else:
#     print("The number is not divisible by both 5 and 11.")

#(4:-) write a program to check area calculation of a triangle

# print("******** AREA CALCULATION OF A TRIANGLE ********")
# print(""" Press 1 to get the area of swuare
# Press 2 to get the area of rectangle
# Press 3 to get the area of triangle
# Press 4 to get the area of circle""")

# choice  =  int(input("Enter your choice between 1-4:- "))
# if choice == 1:
#     side = float(input("Enter the side of the square: "))
#     area = side ** 2
#     print(f"The area of the square is {area} square units.")

# elif choice == 2:
#     length = float(input("Enter the length of the rectangle: "))
#     width = float(input("Enter the width of the rectangle: "))
#     area = length * width
#     print(f"The area of the rectangle is {area} square units.")

# elif choice == 3: 

#     base = float(input("Enter the base of the trimgle: "))
#     height = float(input("Enter the height of the triangle: "))
#     area = 0.5 * base * height  
#     print(f"The area of the triangle is {area} square units.")

# elif choice == 4:
#     radius = float(input("Enter the radius of the circle: "))
#     area = 3.14 * radius ** 2
#     print(f"The area of the circle is {area} square units.")

# else:
#     print("Invalid choice! Please select a number between 1 and 4.")


#(5:-) write a program to check whether passed letter is vowel or consonant

# letter = input("Enter a letter: ")
# if letter in "aeiou" or letter in "AEIOU":
#     print(f"{letter} is a vowel.")
# else:
#     print(f"{letter} is a consonant.")

#(6:-) write a program to check whether a year is leap year or not

# year = int(input("Enter a year: "))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.")

#(7:-) write a program to check it a number is a single digit , it a second digit or a third digit or up to 5 digit

# num = int(input("Enter a number: "))
# if num >= 0 and num< 9:
#     print("The number is a single digit.")
# elif num >= 10 and num <=99:
#     print("The number is a two-digit number.")
# elif num >= 100 and num<= 999:
#     print("The number is a three-digit number.")
# elif num >= 1000 and num <= 9999:
#     print("The number is a four-digit number.")

# else:
#     print("The number is a five-digit number or more.")


#  Fibonacci series using a simple loop

# n = int(input("Kitne terms chahiye? "))

# a, b = 0, 1

# print("Fibonacci series:")
# for i in range(n):
#     print(a, end=" ")
#     a, b = b, a + b

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
