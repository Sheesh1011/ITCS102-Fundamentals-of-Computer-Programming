temp = eval(input("What is the temperature oustide today? "))

if temp <= 0:
        print("The temperature is BELOW FREEZING today")

elif temp >= 1 and temp <= 15:
        print("The temperature is EXTREMELY COLD today")

elif temp >= 16 and temp <= 30:
        print("The temperature is COLD today")

elif temp >= 31 and temp <= 38:
        print("The temperature is LUKEWARM today")

elif temp >= 39 and temp <= 42:
        print("The temperature is WARM today")

elif temp >= 43 and temp <= 50:
        print("The temperature is HOT today")

elif temp >= 51 and temp <= 60:
        print("The temperature is EXTREMELY HOT today")

elif temp >= 61:
        print("The temperature is BURNING HOT today")
