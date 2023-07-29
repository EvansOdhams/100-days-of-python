#1. Create a greeting for your program
#2. Ask the user for the city that they grew up in
#3. Ask the user for the name of their pet
#4. Combine the name of there city and pet and output the band name
#5. Make sure the input cursor shows on a new line.

print("Hi there\n")
city = input("Enter the city where you were born: \n")
pet = input("Add the name of your pet \n")

band_name = city + " " + pet
print("Your band name is " + band_name)