eng = input("Enter the alpha:")
print(eng)

alpha = "a,e,i,o,u"


if (eng.isdigit()):

    print("Given character is Not an Alphabet")

elif (alpha.__contains__(eng)):
    print("vowel")

else:
    print("consonant")