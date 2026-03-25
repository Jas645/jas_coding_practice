import time
import math

drinks = {
    "Beer (pint)" : 2.0,
    "Wine (125ml)": 1.5,
    "Wine (250ml)": 3.0,
    "Spirit (25ml)": 1.0,
    "Cocktail (single)": 1.25,
    "Cocktail (double)": 2.5,
    "Ultranecrodeathpunch EXTREME" : 1000
    }

total_hours = float(input("How many hours will you be drinking for? "))
print(f"Alocnaut recommends you do not exceed {total_hours} units of alcohol in this time period.")
unit_target = float(input("NHS website for guidelines: https://www.nhs.uk/live-well/alcohol-advice/calculating-alcohol-units \nPlease drink responsibly.\nHow many units would you like to drink? "))


total_seconds = total_hours * 60 * 60

amount_drunk = 0
start_time = time.time()

while amount_drunk < unit_target:
    print("Available drinks")
    for i, (drink, units) in enumerate(drinks.items(), start = 1):
        print(f"{i}. {drink} ({units} units)")
    choice = int(input("\nChoose your drink by number: "))
    
    if choice < 1 or choice > len(drinks):
        print("Invalid choice! Try again.")
        continue
    
    drink_name = list(drinks.keys())[choice-1]
    drink_units = drinks[drink_name]
    print(f"You selected {drink_name} with {drink_units} units per drink")
    
    amount_drunk += drink_units 
    if amount_drunk > unit_target:
        amount_drunk = unit_target
        if amount_drunk == unit_target:
            break
        
    remaining_units = unit_target - amount_drunk
    seconds_per_unit = total_seconds / unit_target
    interval_seconds = seconds_per_unit * drink_units
    
    print(f"\nYou drank a {drink_name} ({drink_units} units).")
    print(f"Total so far: {amount_drunk:.2f} / {unit_target} units")
    print(f"Next reminder in {interval_seconds/60:.1f} minutes!")
    
    time.sleep(interval_seconds)

print(f"""You've reached your target number of drinks! \nHave a safe night! \nLove, Alconaut!""")