dict = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00

}

total = 0 
while True:
    try:
        item = input("Item: ").strip().title()
        for order in dict:
            if order == item:
                total = total + (dict[order])
                print(f'Total: ${total:.2f}')
    #except ValueError:

    except KeyboardInterrupt:
        print("have a good day")
        break 


