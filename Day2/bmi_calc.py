import math

weight = float(input("whats your weight?\n"))
height = float(input('whats your height?\n'))

bmi_calc = weight / pow(height, 2)

print(round(bmi_calc, 3))
print(f"{bmi_calc:.3f}")
print(math.floor(bmi_calc))
print(bmi_calc//1)
