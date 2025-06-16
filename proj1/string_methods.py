name  = "supraja aravamudhan"

print(len(name)) # Length of the string
print(name[0]) # First character of the string
print(name[-1]) # Last character of the string
print(name.find("ra")) # Find the index of substring "ra"
print(name.count("a"))
print(name.rfind("a")) # Find the last index of substring "a"
print(name.capitalize()) # Capitalize the first character
print(name.replace("raja", "rav")) # Replace "supraja" with "s"

print(name.upper())
print(name.isalpha()) # Check if all characters are alphabetic
print(name.isalnum()) # Check if all characters are alphanumeric

phone = "123-456-7890"
print(phone.count("-")) # Count the number of hyphens
print(phone.replace("-", "")) # Remove hyphens
print(phone.split("-")) # Split the string into a list
print(phone.split("-")[0]) # Get the first part of the phone number
print(phone.split("-")[1]) # Get the second part of the phone number
print(phone.casefold()) # Case insensitive comparison
print(name.startswith("supraja")) # Check if the string starts with "supraja

#different ways to check if a string is empty
print(name == "") # Check if the string is equal to an empty string
print(len(name) == 0) # Check if the length of the string is zero
print(not name) # Check if the string is falsy (empty)
print(bool(name)) # Convert the string to a boolean (True if not empty, False if empty)

#different string concatenation methods
name1 = "supraja"
name2 = "aravamudhan"
print(name1 + " " + name2) # Using + operator
print(" ".join([name1, name2])) # Using join method
print(f"{name1} {name2}") # Using f-string formatting
print("%s %s" % (name1, name2)) # Using old-style formatting
# Using format method
print("{} {}".format(name1, name2)) # Using format method
# Using string interpolation
print(name1 + " " + name2) # Using + operator
# Using string interpolation with % operator
print("%s %s" % (name1, name2)) # Using old-style formatting
# Using string interpolation with format method
print("{} {}".format(name1, name2)) # Using format method
# Using string interpolation with f-string formatting
print(f"{name1} {name2}") # Using f-string formatting
# Using string interpolation with join method
print(" ".join([name1, name2])) # Using join method
name1.join(['praveen'])

