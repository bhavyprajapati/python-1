
def even_numbers():
    num = 0
    count = 0
    
    while count < 10:
        yield num
        num += 2
        count += 1

# Using the generator
for ev in even_numbers():
    print(ev)
