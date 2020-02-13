


def fr_to_eu (francs):
    conversion= francs*0.91
    conversion_result= "For "+ str(francs)+ " francs, you will get " + str (conversion)+ " euros"
    print(conversion_result)
    if conversion> 50:
        print ("You can go to a nice restaurant")
    if conversion <50:
        print ("you can go to a pizzeria")


input_user= input ("How many francs you want to convert for your lunch? ")
final_message= fr_to_eu (float(input_user))

