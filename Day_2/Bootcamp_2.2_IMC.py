
# 2 lesson

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

height_float = float(height)
weight_float = float(weight)

IMC = (weight_float/(height_float**2))

IMC_int = int(IMC)

print (IMC_int)