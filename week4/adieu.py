import inflect
# p = inflect.engine()

# text = ["Adieu", "adieu","to"]


# while True:
#     try:
#         n = input("name: ")
#     except KeyboardInterrupt:
#         print()
#         break
#     text.append(n)
# text[2] = "to" + text[2]

# if len(text) == 3:
#     new_text = p.join(text, conj='')
# elif:
# print(new_text)
p = inflect.engine()

lst = [ ]

while True:

    try:

        name = input("Names: ")

        lst.append(name)

    except KeyboardInterrupt:

        print ("\n")  

        break

for name in lst:

    mylist = p.join((lst), final_sep=",")

print(f"Adieu, adieu, to {mylist}")
