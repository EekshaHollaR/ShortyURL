import random 
import string

CHARACTER_SET=string.ascii_letters+string.digits
#total: 62 char : Possibilities= 62^6=56800235584 unique code

def generate_short_code(length=6):
    generated_code="".join(random.choices(CHARACTER_SET,k=length))
    return generated_code

if __name__=="__main__":
    print("__Testing generate_short_code----")

    print("Generating 5 codes with default length(6)")
    for _ in range(5):
        print(generate_short_code())
    print("\n"+"-"*20+"\n")
    print("Generating 1 code with custom lenght (10):")
    print(generate_short_code(length=10))
    print("\n"+"---Test complete----")

