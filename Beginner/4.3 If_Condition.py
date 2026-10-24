australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
uae = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
india = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

first_input = input("Enter the first city: ")
second_input = input("Enter the second city: ")

city_one = first_input.strip().title()
city_two = second_input.strip().title()


def find_country(city):
    if city in australia:
        return "Australia"
    elif city in uae:
        return "UAE"
    elif city in india:
        return "India"
    return None


country_one = find_country(city_one)
country_two = find_country(city_two)

if country_one is None or country_two is None:
    print('Output: "where are you from?"')
elif country_one == country_two:
    print(f'Output: "Both cities are in {country_one}"')
else:
    print('Output: "They don\'t belong to the same country"')
