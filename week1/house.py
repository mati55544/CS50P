name = input("what's your name ?")

match name:
    case "Harry":
        print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Ron":
        print("gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("who?")
