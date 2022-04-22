# list comprehension

result = [item ** 2 for item in range(1, 10, 1) if item % 2 == 0]

# working on the list comparison from 2 files

with open("file1.txt", "r") as f_1:
    lis_1 = f_1.readlines()
    print(lis_1)

with open("file2.txt", "r") as f_2:
    lis_2 = f_2.read()


