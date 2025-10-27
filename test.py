import os
import time
import random

# Clear the screen (works on Windows, Mac, Linux)
os.system('cls' if os.name == 'nt' else 'clear')

# Ask a silly question
answer = input("🤔 Quick question... what's 1 + 1? ")

# Wait dramatically
print("\nCalculating your genius response...")
time.sleep(1.5)

# Clear again for effect
os.system('cls' if os.name == 'nt' else 'clear')

# List of witty compliments
messages = [
    "🎉 Good job, Einstein! Even if it’s wrong, your enthusiasm is unmatched!",
    "👏 Well done! I can feel your brain overheating from that effort!",
    "😎 Incredible. That answer just broke the laws of mathematics!",
    "🔥 Genius detected. NASA is on the line, they want your number!",
    "🧠 Outstanding! You’ve successfully participated in the world’s easiest quiz!"
]

# Print a colorful “Good Job” banner
print("\033[92m")  # set text color to green
print("╔═══════════════════════════════╗")
print("║         🌟 GOOD JOB! 🌟        ║")
print("╚═══════════════════════════════╝")
print("\033[0m")  # reset color

# Print a random funny message
print(random.choice(messages))
print("\n")

time.sleep(3)
input("Press Enter to exit 😁 ")
