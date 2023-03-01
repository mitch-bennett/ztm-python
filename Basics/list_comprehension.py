some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)

#nodup_dict = {k:v }
no_dup = list({char for char in some_list if some_list.count(char) > 1})
no_dup.sort()
print(no_dup)