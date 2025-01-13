weight = int(input("Weight: "))
unit = input("(L)lb or (k)Kg: ")

if unit.upper() == 'L':
    converted = weight * 0.45
    print(f"You are  {converted} kilos")

else:
    convert = weight / 0.45
    print(f"Your are {convert} pounds")
