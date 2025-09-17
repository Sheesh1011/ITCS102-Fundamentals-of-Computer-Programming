print("🦜 PARROT SIMULATOR – THE ECHO CHAMBER")
phrase = input("What will your parrot say? ")
freq = eval(input("How many times your parrot should say it? "))
print("\nListen to you parrot:")
for k in range(freq, 0, -1):
    print("🦜 Squawk!", phrase)
