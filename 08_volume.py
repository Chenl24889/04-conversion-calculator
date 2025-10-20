distance_dict = {
    "ml": 1000,
    "l": 1,
    "kl": .001,
    "Ml": .000001,
}
# get amount and units （assume they are valid）
amount = float(input("how much? "))
from_unit = input("From Unit? ")
to_unit = input("To Unit? ")

# multiply to get to our standard value...
multiply_by = distance_dict[to_unit]
standard = amount * multiply_by

# Divide to get to our desired value
divide_by = distance_dict[from_unit]
answer = standard / divide_by
print(f"There are {answer} {to_unit} in {amount} {from_unit} ")