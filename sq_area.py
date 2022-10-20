def sq_footage():
    length = int(input("What is the length in inches of your house? "))
    width = int(input("what is the width in inches of your house? "))
    area = length * width
    print(f"The square footage of your house is {area}.")
    
sq_footage()