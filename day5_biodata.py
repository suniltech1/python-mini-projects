# Personal Bio-Data Card Program

# Strings
full_name = input("Enter your full name: ")
city = input("Enter your city: ")

# Integer and Float
age = int(input("Enter your age: "))
height = float(input("Enter your height in meters: "))

# Boolean (yes/no → True/False)
student_input = input("Are you a student? (yes/no): ").strip().lower()
is_student = True if student_input == "yes" else False

# Tuple (immutable: birth date)
birth_day = int(input("Enter birth day: "))
birth_month = int(input("Enter birth month: "))
birth_year = int(input("Enter birth year: "))
dob = (birth_day, birth_month, birth_year)

# List (hobbies)
hobbies = []
print("Enter 3 hobbies:")
for i in range(3):
    hobby = input(f"Hobby {i+1}: ")
    hobbies.append(hobby)

# Set (languages - removes duplicates automatically)
languages = set()
print("Enter 3 languages (try repeating one to test set behavior):")
for i in range(3):
    lang = input(f"Language {i+1}: ")
    languages.add(lang)

# Dictionary (full profile)
profile = {
    "Full Name": full_name,
    "City": city,
    "Age": age,
    "Height": height,
    "Is Student": is_student,
    "Date of Birth": dob,
    "Hobbies": hobbies,
    "Languages": languages
}

# String indexing and len()
first_letter = full_name[0]

# Output Bio-Data Card
print("\n" + "="*40)
print("        PERSONAL BIO-DATA CARD")
print("="*40)

print(f"Name: {full_name} (type: {type(full_name)})")
print(f"First Letter of Name: {first_letter}")

print(f"City: {city} (type: {type(city)})")
print(f"Age: {age} (type: {type(age)})")
print(f"Height: {height} (type: {type(height)})")
print(f"Is Student: {is_student} (type: {type(is_student)})")

print(f"Date of Birth: {dob} (type: {type(dob)})")
print(f"Hobbies: {hobbies} (Total: {len(hobbies)})")

print(f"Languages: {languages} (Unique: {len(languages)})")

print("\nFull Profile Dictionary:")
print(profile)

print("="*40)