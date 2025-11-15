
List1 = ['apple', 'banana', 'mango']
search_item = "mango"

found = False

for item in List1:
    if item == search_item:
        found = True
        break

if found:
    print(search_item, "found in the list!")
else:
    print(search_item, "not found in the list.")
