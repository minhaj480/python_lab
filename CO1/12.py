data = {'b': 5, 'a': 2, 'd': 8, 'c': 1}

items = list(data.items())

for i in range(len(items)):
    for j in range(len(items) - i - 1):
        if items[j][1] > items[j + 1][1]:   
            items[j], items[j + 1] = items[j + 1], items[j]

asc_dict = dict(items)
print("Ascending order:", asc_dict)

for i in range(len(items)):
    for j in range(len(items) - i - 1):
        if items[j][1] < items[j + 1][1]:   
            items[j], items[j + 1] = items[j + 1], items[j]

desc_dict = dict(items)
print("Descending order:", desc_dict)
