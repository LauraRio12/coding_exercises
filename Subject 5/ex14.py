

weather= input("Is it raining or sunny?")
temperature= input("Is it warm or cold?")

if weather=="raining" and temperature=="cold":
    print("Take an umbrella and a warm jacket.")
if weather=="raining" and temperature=="warm":
    print("Take an umbrella and a t-shirt.")
if weather=="sunny" and temperature== "cold":
    print("Take sunglasses and a warm jacket.")
if weather=="sunny" and temperature== "warm":
    print("Take sunglasses and a t-shirt")
else:
    print("Stay home!")
    
