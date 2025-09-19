print("Welcome to the ChatBot")
name = input("What is your name? ")
age = int(input(f"Hello {name}, how old are you? "))
print(f"Wow, {age}! Somebody's getting old!\n")
print('How can I assist you?')
print("1. Placeholder 1\n2. Placeholder 2\n3. Placeholder 3\n4. Exit")
selection = int(input("Please select a number: "))
if selection == 1:
    print("Option 1")
if selection == 2:
    print("Option 2")
if selection == 3:
    print("Option 3")
if selection == 4:
    print("Farewell!")