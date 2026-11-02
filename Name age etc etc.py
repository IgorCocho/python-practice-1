name = input("What´s your name? :")
print(f"Hi. How are you {name}? ")
edad = int(input("How old are you...? :"))
if edad < 15:
    print(f"aww {edad} you are so yung.")
elif edad > 15 and edad < 25:
    print(f"{edad}, ohhh yung adult")
elif edad > 25 and edad< 85:
    print(f"{edad}... You're a senile old man. lol ")
else:
    print(f"{edad}... Huh... Sure... ")

