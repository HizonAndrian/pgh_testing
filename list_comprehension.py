# List comprehension = A concise way to create lists in Python
#                      Compact and Easier to read than traditional loops
#                      [expression for value in iterable if condition]

num_list = [1, 2 , 4, 5]
name_list = ["andrian", "kesian"]
doubles = [x[0].upper() + x[1:] for x in name_list if x == "andrian"]
print(doubles)