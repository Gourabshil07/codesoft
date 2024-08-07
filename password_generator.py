import random
import string

print("Welcome to the Password Generator!")

def main():

    length= int(input("Enter the desired length of the password:"))
    lowerP=string.ascii_lowercase
    upperP=string.ascii_uppercase
    digitP=string.ascii_uppercase
    symbolsP=string.punctuation
    combine=lowerP+upperP+digitP+symbolsP
    x=random.sample(combine,length)
    password="".join(x)

    print(password)

      
    main()
    

main()

