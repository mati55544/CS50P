def main():
    sentence = input("please type a something-\n")
    sentence = convert(sentence)    #to ask robert about that 
    print(sentence)




def convert(sentence):
    sentence = sentence.replace(":)","🙂")
    sentence = sentence.replace(":(","🙁")
    return sentence    ###why




main()


