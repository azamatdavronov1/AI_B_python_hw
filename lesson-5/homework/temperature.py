def convert_cel_to_far(cel):
    rounded = format(cel * 9/5 + 32, ".2f")
    return rounded


def convert_far_to_cel(far):
    rounded = format((far - 32) * 5/9, ".2f")
    return rounded


celcium = float(input("Enter temperature in Celcius: "))
print(celcium, " C = ", convert_cel_to_far(celcium), " F")


faren = float(input("Enter temperature in farenheit: "))
print(faren, " F = ", convert_far_to_cel(faren), " C")













