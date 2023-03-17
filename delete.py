hatlist = [1, 2, 3, 4, 5]
print("Original list content:", hatlist)
hatlist[2] = hatlist[3]
print("New list content:", hatlist)
del hatlist[3]
print("New list content:", hatlist)
print("New list length:", len(hatlist))