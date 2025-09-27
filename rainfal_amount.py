
def rainfall_message(rainfall):
    if rainfall == 0:
        return "No rainfall. It's a dry day."
    elif rainfall < 20:
        return "Light rainfall. You might need an umbrella."
    elif rainfall < 50:
        return "Moderate rainfall. Carry rain gear and be cautious."
    elif rainfall < 100:
        return "Heavy rainfall. Travel with care!"
    else:
        return "Very heavy rainfall. It's better to stay indoors for safety."
rainfall = float(input("Enter the rainfall amount in mm: "))
message = rainfall_message(rainfall)
print(message)

