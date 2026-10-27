radius=84
pi=3.14
water_per_sq_meter=1.4

pond_area=pi*(radius**2)
print(f"Area of the pond: {pond_area} square meters")
total_water=pond_area*water_per_sq_meter
print(f"Total water in the pond (no decimals): {int(total_water)} liters")

