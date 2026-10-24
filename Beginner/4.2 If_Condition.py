australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
uae = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
india = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

user_input = input("Enter a city name: ")
city_name = user_input.strip().title()

if city_name in australia:
    print(f'Output: "{city_name} is in Australia"')
elif city_name in uae:
    print(f'Output: "{city_name} is in UAE"')
elif city_name in india:
    print(f'Output: "{city_name} is in India"')
else:
    print(f'Output: ""{user_input.strip()}" Where are you?."')