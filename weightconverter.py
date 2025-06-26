#weight converter:make this converter continous until the 100kg or pound person is found,then print century found and stop the loop
#take the weight and unit of the user using input  ,45kg=100pounds
#check if the unit is kg or pounds(lbs)
#if the weight is in kg,convert to pound and viceversa
while True:
    weight = float(input("Enter your weight: "))
    unit = input("Enter (K) for kgs and (L) for pounds: ")# You can use .lower() or .upper()
    if unit.upper() == 'K':
        converted = weight / 0.45
        if converted == 100:
            print("century found")
            break
        print(f'You are {converted} pounds')
    elif unit.lower() == 'l':
        converted = weight * 0.45
        if converted != 100:
            print(f'You are {converted} kgs')
        else:
            print("century found")
            break
    else:
        print("Invalid input. Please enter K or L.")
#weight converter:make this converter continous until the 100kg or pound person is found,then print century found and stop the loop
#take the weight and unit of the user using input  ,45kg=100pounds
#check if the unit is kg or pounds(lbs)
#if the weight is in kg,convert to pound and viceversa
while True:
    weight = float(input("Enter your weight: "))
    unit = input("Enter (K) for kgs and (L) for pounds: ")# You can use .lower() or .upper()
    if unit.upper() == 'K':
        converted = weight / 0.45
        if converted == 100:
            print("century found")
            break
        print(f'You are {converted} pounds')
    elif unit.lower() == 'l':
        converted = weight * 0.45
        if converted != 100:
            print(f'You are {converted} kgs')
        else:
            print("century found")
            break
    else:
        print("Invalid input. Please enter K or L.")
