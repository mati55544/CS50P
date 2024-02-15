grocery_list = []

while True:

    try:
        items = input().upper()
        grocery_list.append(items)
    except EOFError:
        print()
        raise ValueError

x = set(grocery_list)
final = sorted(x)

for item in final:
    count = grocery_list.count(item)
    print(count, item)