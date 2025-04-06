# Optional: Only works on some Windows terminals or use with color-enabled IDEs
RESET = "\033[0m"
BOLD = "\033[1m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
GREEN = "\033[92m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"

print(f"\n{MAGENTA}✨ Welcome to the Ultimate Adventure Mad Libs Game! ✨{RESET}")
print(f"\n{CYAN}🧹 Let's create your magical story at Hogwarts School of Witchcraft and Wizardry! 🧹{RESET}\n")

name = input("🧙 Your name: ")
place = input("🏰 Your Hogwarts house: ")
fav_novel = input("📚 Your favorite Professor: ")
fav_character = input("🧑‍🎓 Your favorite character from Harry Potter: ")
food = input("🍫 Your favorite Snack: ")
treasure = input("💎 A secret you want to find (e.g., Horcruxes, Basilisk): ")
superpower = input("✨ A superpower you wish to have: ")
animal = input("🐾 Your pet: ")
color = input("🎨 Your favorite color: ")
hobby = input("📖 Your favorite Subject: ")
wand_wood = input("🌲 What wood is your wand made of? ")
spell = input("🔮 Your favorite spell: ")
magical_creature = input("🐉 A magical creature you love: ")
best_friend = input("🧑‍🤝‍🧑 A friend you'd take with you to Hogwarts: ")
magical_object = input("🧳 A magical object you'd like to own: ")
common_room = input("🛋️ Favorite spot at Hogwarts (e.g., Library, Astronomy Tower): ")
house_trait = input("💫 A trait that defines your house (e.g., bravery, wisdom): ")

story = f"""
{YELLOW}🌟 Once upon a time, {name}, a proud {place} student known for their {house_trait},
embarked on a thrilling adventure at Hogwarts. With a {color} sky above and their pet {animal} by their side,
they wandered into the {common_room}, holding a {wand_wood} wand and dreaming of meeting {fav_character}.

Suddenly, a {magical_creature} appeared carrying a glowing {magical_object} that pointed toward the legendary {treasure}.
Guided by clues from "{fav_novel}" and accompanied by their loyal friend {best_friend}, {name} set out to find it.

But before the path could open, {name} had to master the spell "{spell}" and demonstrate the power of {superpower},
all while solving riddles based on {hobby}. It was no easy task—but their courage and curiosity lit the way.

After braving enchanted forests, mysterious hallways, and secret chambers,
{name} finally discovered the hidden vault where the {treasure} shimmered in the moonlight.

A grand feast of {food} awaited in the Great Hall, where {fav_character} raised a toast in {name}’s honor.
With laughter, magic, and friendship all around, it was truly a day to remember at Hogwarts. 🌈✨{RESET}
"""

print(story)
