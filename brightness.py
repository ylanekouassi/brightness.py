import screen_brightness_control as sbc

print(f"Current brightness level: {sbc.get_brightness()}")

b_level = input("Enter brightness level: ")

sbc.set_brightness(b_level)