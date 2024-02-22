import emoji

# print(emoji.emojize('Python is :thumbs_up:'))


def main():
    words = input("input:")
    print(emoj(words))


def emoj(em):

    return emoji.emojize(em)


# # if __name__=="main":
# #     main()

main()
