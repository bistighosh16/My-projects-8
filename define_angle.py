
def classify_angle(angle):
    if angle > 0 and angle < 90:
        return "Acute Angle (less than 90°)"
    elif angle == 90:
        return "Right Angle (exactly 90°)"
    elif angle > 90 and angle < 180:
        return "Obtuse Angle (greater than 90° but less than 180°)"
    else:
        return "Invalid angle. Please enter an angle between 0° and 180°."
angle = float(input("Enter the angle in degrees: "))
result = classify_angle(angle)
print(result)
