print("Welcome! to the intetractive personal data collector")
print()


name = input("Enter your name: ")
age = int(input("Enter your age: "))
height_cm = float(input("Enter your height in centimeters: "))
favourite_number = int(input("Enter your favourite number: "))

current_year = 2026
birth_year = current_year - age
age_in_months = age * 12
height_m = height_cm / 100

print()
print("PERSONAL INFORMATION")
print()
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height in centimeters: {height_cm} centimeters")
print(f"Height in meters: {height_m} meters")
print(f"Favourite Number: {favourite_number}")
print(f"Estimated Birth Year: {birth_year}")
print(f"Approximated age in months: {age_in_months}")

print()
print("COLLECTED INFORMATION")
print()

print(f"Name: {name} (Type: {type(name)}, ID: {id(name)})")
print(f"Age: {age} (Type: {type(age)}, ID: {id(age)})")
print(f"Height in centimeters: {height_cm} (Type: {type(height_cm)}, ID: {id(height_cm)})")
print(f"Height in meters: {height_m} (Type: {type(height_m)}, ID: {id(height_m)})")
print(f"Favourite Number: {favourite_number}(Type: {type(favourite_number)}, ID: {id(favourite_number)})")

print()
print("Thank You! for using this Personal Data Collector")
