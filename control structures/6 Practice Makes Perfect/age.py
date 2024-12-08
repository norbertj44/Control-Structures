age = int(input("enter your age: "))

if age < 13:
    age_group = "child"
elif 13 <= age <= 19:
    age_group = "teen"
elif 20 <= age <= 64:
    age_group = "adult"
else:
    age_group = "senior"

print(f"you belong to the '{age_group}' age group.")
