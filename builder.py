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
  "CPU": [["Rayzen7", 5000], ["CoreI7", 6000], ["Rayzen5", 2000]],
  "MOTHERBOARD": [["Gigabyte Z690 Aorus Pro", 7000], ["ASRock Z690 Taichi", 10000]],
  "GPU_GRAPHIC_CARD": [["Nvidia GeForce RTX 3090 Ti", 32000], ["Nvidia GeForce RTX 3080", 16000]],
  "RAM": [["8GB", 4500], ["16GB", 5000], ["32GB", 10000]],
  "PRIMARY_STORAGE_SSD": [["WD Black SN850", 7250], ["WD Black SN770", 8345]],
  "PSU": [["Corsair RM750x", 13200], ["Seasonic Prime Titanium TX-1000", 8450]], # Power Supply
  "CASE": [["Fractal Design Meshify 2 Compact", 3400], ["Lian Li O11 Air Mini", 5500]]
}
order = ["CPU", "MOTHERBOARD", "GPU_GRAPHIC_CARD", "RAM", "PRIMARY_STORAGE_SSD", "PSU", "CASE"]

# User Interaction
user_parts = []
user_price = 0
user_name = (input("What's your name?\n ------>"))
print("Welcome {}, this is Computer Builder".format(user_name))
print("Choose your preferred number")

for i in range(len(parts)):
    current_part = order[i]
    print("✅ Choose your {}".format(current_part))
    for i in range(len(parts[current_part])):
        print([i + 1], parts[current_part][i][0], "Price: ${}".format(parts[current_part][i][1]))
    user_choice = 10
    while user_choice > len(parts[current_part]) or user_choice < 0:
        user_choice = int(input("----->"))
    user_parts.append(parts[current_part][user_choice -1][0])
    user_price += parts[current_part][user_choice -1][1]
# Final output
print("Congrats {}, here's your computer ❤️".format(user_name))
for i in range(len(order)):
    current_part = order[i]
    print("✅ Your {}:".format(current_part), user_parts[i])
print("🏔️ Final Price: ${}".format(user_price))
