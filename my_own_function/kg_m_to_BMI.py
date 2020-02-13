
def BMI(weight,height):
    BMI= weight/height*height
    return "With a weight in kg of " + str(weight)+ " and an heigth in cm of " +str(height) +" your body mass index (BMI) is of "+ str(int(BMI)) + "."
print (BMI(50, 160))
