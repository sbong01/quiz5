#Quiz5
#problem 1
def tire_pressure(pres):
    if pres < 28:
        print("Tire pressure is low.")
    else:
        return None

#problem 2
def thermostat(temp):
    if temp <= 52:
        print("The heater is on.")
    elif 52 < temp < 71:
        print("Heater and AC are off.")
    else:
        print("AC is on.")

#problem 3
def fru(fruit):
    if fruit == "banana":
        print("Banana it is!")
    elif fruit == "cherry":
        print("I cherish you!")
    elif fruit == "apple":
        print("I applesolutely like you!")
    elif fruit == "orange":
        print("Orange you glad to see me?")
    elif fruit == "melon":
        print("You are one in a Melon.")


#for exercise
tire_pressure(10)
tire_pressure(30)
thermostat(33)
thermostat(60)
thermostat(80)
fru("banana")
fru("cherry")
fru("apple")
fru("orange")
fru("melon")
