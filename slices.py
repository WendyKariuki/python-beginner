# Copying the entire list.
list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)

# Copying some part of the list.
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)

my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1]
print(new_list)

my_list = [10, 8, 6, 4, 2]
new_list = my_list[-1:1]
print(new_list)
my_list = [0, 3, 12, 8, 2]

print(5 in my_list)
print(5 not in my_list)
print(12 in my_list)