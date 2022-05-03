# list comprehension

x = [item ** 2 for item in range(1, 10, 1) if item % 2 == 0]

# working on the list comparison from 2 files

with open("file1.txt") as f_1:
    lis_1 = f_1.read()

with open("file2.txt") as f_2:
    lis_2 = f_2.readlines()

answer = [int(item) for item in lis_1 if item in lis_2]
print(answer)

# dictionary comprehension

statement = "What is the Airspeed Velocity of an Unladen Swallow?"

words = statement.split()

new_dict = {k:len(k) for k in words}
print(new_dict)


