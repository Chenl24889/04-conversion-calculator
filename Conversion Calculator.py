# Generates Headings (eg: ---- Heading ----) 1 usage from did import Instruction
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# Displays instructions
def instructions():
    statement_generator("Instructions", "-")

    print('''
conversion calculator 
- volume
- mass
- distance
- time 
    ''')


def num_check(question):

    while True:
        try:
            num = float(input(question))
            if num <= 0:
                print("Please enter a number that is more than zero.")
                continue
            return num
        except ValueError:
            print("Please enter a numeric value.")


# Display instructions if requested
want_instructions = input("Press <enter> to see the instructions or any key to continue. ")

if want_instructions == "":
    instructions()

valid_type = {"volume", "mass", "distance", "time"}

while True:
    calc_type = input("calc_type: ").strip().lower()
    if calc_type == "xxx":
        print("Thank you using conversion calculator!!!^-^")
        break
    if calc_type not in valid_type:
        print("Please enter a valid calculation type.")
        continue

    if calc_type == "volume":
            # get amount and units （assume they are valid）
            amount = float(num_check("how much? "))
            from_unit = input("From Unit? ")
            to_unit = input("To Unit? ")
            distance_dict = {
           "ml": 1000,
           "l": 1,
           "kl": .001,
           "Ml": .000001,
           }
            # multiply to get to our standard value...
            multiply_by = distance_dict[to_unit]
            standard = amount * multiply_by

            # Divide to get to our desired value
            divide_by = distance_dict[from_unit]
            answer = standard / divide_by
            print(f"There are {answer} {to_unit} in {amount} {from_unit}. ")

    if calc_type == "time":
            # get amount and units （assume they are valid）
            amount = float(num_check("how much? "))
            from_unit = input("From Unit? ")
            to_unit = input("To Unit? ")
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

            # multiply to get to our standard value...
            multiply_by = distance_dict[to_unit]
            standard = amount * distance_dict[from_unit]

            # Divide to get to our desired value
            divide_by = distance_dict[from_unit]
            answer = standard / distance_dict[to_unit]
            print(f"There are {answer} {to_unit} in {amount} {from_unit} ")

    if calc_type == "distance":
          # get amount and units （assume they are valid）
          amount = float(num_check("how much? "))
          from_unit = input("From Unit? ")
          to_unit = input("To Unit? ")
          distance_dict = {
                "mm": 1000,
                "cm": 100,
                "m": 1,
                "km": .001,
            }
          # multiply to get to our standard value...
          multiply_by = distance_dict[to_unit]
          standard = amount * multiply_by

          # Divide to get to our desired value
          divide_by = distance_dict[from_unit]
          answer = standard / divide_by
          print(f"There are {answer} {to_unit} in {amount} {from_unit}. ")

    if calc_type == "mass":
          # get amount and units （assume they are valid）
           amount = float(num_check("how much? "))
           from_unit = input("From Unit? ")
           to_unit = input("To Unit? ")
           distance_dict = {
                 "mg": 1000,
                 "g": 1,
                 "kg": .001,
                 "t": .000001,
            }
           # multiply to get to our standard value...
           multiply_by = distance_dict[to_unit]
           standard = amount * multiply_by

           # Divide to get to our desired value
           divide_by = distance_dict[from_unit]
           answer = standard / divide_by
           print(f"There are {answer} {to_unit} in {amount} {from_unit}. ")


