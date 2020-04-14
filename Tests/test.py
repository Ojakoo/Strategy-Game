print("hello")

# change all but string to int
list1 = ["n","1","2"]

for i in range(len(list1)):
    try:
        list1[i] = int(list1[i])
    except ValueError:
        pass

#change all to int
list2 = ["0","1","2","3"]

list2 = [int(i) for i in list2]
print(list2)

#change range to int
list3 = ["0","1","2","3"]
print(range(1,2))

print(list)