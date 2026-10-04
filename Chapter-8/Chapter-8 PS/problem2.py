def conversion(temp):
    converted_temp=(temp*1.8)+32
    return converted_temp
temperature=int(input("ENTER THE TEMPERATURE IN CELSIUS: "))
print(f"TEMPERATURE AFTER CONVERSION: {conversion(temperature)}")
print("END OF THE PROGRAM!!")