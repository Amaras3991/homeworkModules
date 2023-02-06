import random
import string
import datetime




# 1. Write a Python program to generate a random color hex, a random alphabetical string,
# random value between two integers (inclusive) and a random multiple of 7 between
# 0 and 70. Use random.randint()



# def rand_color():
#     r = lambda: random.randint(0,255)
#     print(f"Random color hex is " '#%02X%02X%02X' % (r(),r(),r()))
# rand_color()



# def rand_alphabetical_str():
#     print((f"Random letter is {random.choice(string.ascii_letters)}"))
# rand_alphabetical_str()

# def rand_value():
#     val = random.randint(1, 10)
#     print(f"Random value between two integers is {val}")
# rand_value()


# def rand_multiple():
#     multiple = random.randint(0, 10) * 7
#     print(f"Random multiple of 7 between 0 and 70 is {multiple}")
# rand_multiple()



# 2. Write a Python program to select a random element from a list, set,
# dictionary-value, and file from a directory. Use random.choice()

# my_lst = [1, 2, "abc", 8, "qwe"]
# my_set = (5, 9, "abc", 2)
# my_dict = {
#     "name": "Sam",
#     "lastname": "Smith",
#     "age": 25
# }
# def rand_elem():
#     print(f"Random element from a list is {random.choice(my_lst)}")
#     print(f"Random element from a set is {random.choice(my_set)}")
#     key = random.choice(list(my_dict))
#     print(f"Random element from a dictionary-value is {my_dict[key]}")
#
# rand_elem()



# 3. Write a Python program that generates random alphabetical characters, alphabetical strings, and alphabetical
# strings of a fixed length. Use random.choice()

# def alphabetical():
#     print(f"Random alphabetical character is {random.choice(string.ascii_letters)}")
#     str = ""
#     for i in range(random.randint(1, 20)):
#         str += random.choice(string.ascii_letters)
#     print(f"Random alphabetical string is {str}")
#     str1 = ""
#     for i in range(5):
#         str1 += random.choice(string.ascii_letters)
#     print(f"Random string of fixed lenght is {str1}")
#
# alphabetical()





# 4. Write a Python program to construct a seeded random number generator, also generate a float
# between 0 and 1, excluding 1. Use random.random()



# def rand_float():
#     num = random.random()
#     print(f"Random float number between 0 and 1 is {num}")
# rand_float()



# 5. Write a Python program to generate a random integer between 0 and 6 - excluding 6, random integer between
# 5 and 10 - excluding 10, random integer between 0 and 10, with a step of 3 and random date between two dates.
# Use random.randrange()

# def rand_int():
#     num = random.randint(0, 6)
#     print(f"Random integer between 0 and 6 - excluding 6 is {num}")
#     num1 = random.randint(5, 10)
#     print(f"Random integer between 5 and 10 - excluding 10 is {num1}")
#     num2 = random.randrange(0, 10, 3)
#     print(f"Random integer between 0 an 10 with a step of 3 is {num2}")
#
# rand_int()


# 6.Write a Python program to shuffle the elements of a given list. Use random.shuffle()

# my_lst = ["a", "b", "c", "d"]
# random.shuffle(my_lst)
# print(f"Shuffled list is {my_lst}")


# 7. Write a Python program to generate a float between 0 and 1, inclusive and generate a random float within a
# specific range. Use random.uniform()

# def generate_float():
#     print(f"Random float number between 0 and 1 is {random.uniform(0, 1)}")
#     print(f"Random float number within a specific rang is {random.uniform(2.0, 4.0)}")
#
# generate_float()
