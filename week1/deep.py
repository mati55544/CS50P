#get_input = input("what is the answer to the great Question of life, the Universe, and Everything?")
#if get_input == 42:
#    print("yes")
#elif get_input == "forty-two":
#    print("yes")
#elif get_input == "forty two":
#    print("yes")
#else:
#    print ("no") 

def meaning_of_life():
    meaning = ponder(input("What is the Answer to the Great Question of Life, the Universe, and Everything? "))
    # Warning:  meaning was already pondered upon! So meaning is either 'Yes' or 'No' 
    # Still want to ponder again on `Yes` or `No` ?
    print(meaning)  # ponder on the pondered meaning and print the result 

def ponder(meaning):
    # print(type(meaning))
    return 'Yes' if str(meaning).lower() in ('42', 'forty-two', 'forty two') else 'No'

meaning_of_life()