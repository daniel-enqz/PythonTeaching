# Styling
class color:
    BOLD = '\033[1m'
    END = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    BLANCO = '\033[98m'


# Options
parts = {
  "CPU": ["Rayzen7", "CoreI7", "Rayzen5"],
  "MOTHERBOARD": ["Gigabyte Z690 Aorus Pro", "ASRock Z690 Taichi"],
  "GPU_GRAPHIC_CARD": ["Nvidia GeForce RTX 3090 Ti", "Nvidia GeForce RTX 3080"],
  "RAM": [8, 16, 32],
  "PRIMARY_STORAGE_SSD": ["WD Black SN850", "WD Black SN770"],
  "PSU": ["Corsair RM750x", "Seasonic Prime Titanium TX-1000"], # Power Supply
  "CASE": ["Fractal Design Meshify 2 Compact", "Lian Li O11 Air Mini"]
}
order = ["CPU", "MOTHERBOARD", "GPU_GRAPHIC_CARD", "RAM", "PRIMARY_STORAGE_SSD", "PSU", "CASE"]

# User Interaction
user_parts = []
user_name = (input("What's your name?\n ------>"))
print("Welcome {}, this is Computer Builder".format(user_name))
print("Choose your preferred number")

for i in range(len(parts)):
    current_part = order[i]
    print("Choose your {}".format(current_part))
    for i in range(len(parts[current_part])):
        print([i + 1], parts[current_part][i])
    user_choice = input("----->")
    user_parts.append(parts[current_part][i-1])

# Final output
print("Congrats {}, here's your computer".format(user_name))
for i in range(len(order)):
    current_part = order[i]
    print("Your {}:".format(current_part), user_parts[i])
