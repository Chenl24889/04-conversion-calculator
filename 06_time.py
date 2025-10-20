distance_dict = {
  "ms": 0.001,
  "s": 1,
  "min": 60,
  "hour": 3600,
  "day": 86400,
  "week": 604800,
  "month": 2629746,
  "year": 31556952
}
# get amount and units （assume they are valid）
amount = float(input("how much? "))
from_unit = input("From Unit? ")
to_unit = input("To Unit? ")

# multiply to get to our standard value...
multiply_by = distance_dict[to_unit]
standard = amount * distance_dict[from_unit]

# Divide to get to our desired value
divide_by = distance_dict[from_unit]
answer   = standard / distance_dict[to_unit]
print(f"There are {answer} {to_unit} in {amount} {from_unit} ")