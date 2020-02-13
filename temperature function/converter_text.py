def temp_converter(celsius):
    farenheit= (celsius*9/5)+32
    result=str(celsius) + " degrees Celsius are "+str(farenheit) +" degrees Farenheit "
    return result

print(temp_converter(21.5))
print(temp_converter(-7))
print(temp_converter(11))
print(temp_converter(0))