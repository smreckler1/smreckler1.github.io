#Title: Shannon Reckler
#Date: 12112025
#Assignment Name: Final Project
#A brief description of the project: Use of loops, functions and module import to complete a program

import random
import time

# -----------------------------------
# Player Dictionary
# -----------------------------------
player = {
    "name": "",
    "energy": 100,
    "knowledge": 0,
    "inventory": {}
}

# Track whether a unique event occurred
unique_event_triggered = False

# -----------------------------------
# Utility: slow-print text
# -----------------------------------
def slow(text, delay=0.03):
    """Prints text slowly for effect."""
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

# -----------------------------------
# Introduction
# -----------------------------------
def intro():
    slow("📚 You slowly open your eyes...")
    slow("You find yourself lying on the cold marble floor of an ancient library.")
    slow("Towering shelves stretch endlessly into the shadows.")
    slow("A whisper echoes around you:")
    slow("'Seek the Lost Scrolls of Alexandria before the library reshapes itself again...'\n")

    player["name"] = input("What is your name, wanderer of knowledge? ")
    slow(f"\nWelcome, {player['name']}. Your quest begins now...\n")
    time.sleep(1)

# -----------------------------------
# Secret Room Event
# -----------------------------------
def secret_room_event():
    global unique_event_triggered
    unique_event_triggered = True

    slow("\n🔑 A loose stone shifts beneath your feet...")
    slow("A hidden doorway creaks open...")
    slow("You have discovered a SECRET ROOM!\n")
    time.sleep(1)

    event = random.choice(["ancient_orb", "crystal_tablet", "lost_scholar"])

    if event == "ancient_orb":
        slow("🔮 A glowing Ancient Orb sits on a pedestal.")
        gain = random.randint(15, 30)
        player["knowledge"] += gain
        slow(f"The orb fills your mind with wisdom. Knowledge +{gain}!")

    elif event == "crystal_tablet":
        slow("📜 A floating Crystal Tablet hums softly...")
        slow("You carefully take it—it pulses with forgotten magic.")
        player["inventory"]["crystal tablet"] = 1
        slow("You obtained a Crystal Tablet!")

    else:  # lost_scholar
        slow("👤 A ghostly scholar materializes before you.")
        slow("He shares ancient secrets before fading away...")
        player["energy"] += 20
        player["knowledge"] += 10
        slow("Energy +20! Knowledge +10!")

    time.sleep(1)

# -----------------------------------
# Hidden Passage Event
# -----------------------------------
def hidden_passage_event():
    global unique_event_triggered
    unique_event_triggered = True

    slow("\n🕯 A faint breeze brushes your arm...")
    slow("You pull aside a dusty tapestry...")
    slow("You have discovered a HIDDEN PASSAGE!\n")
    time.sleep(1)

    event = random.choice(["trap_dust", "glyph_room", "forgotten_archive"])

    if event == "trap_dust":
        slow("💨 A trap releases choking dust!")
        slow("You cough and stumble. Energy -15.")
        player["energy"] -= 15

    elif event == "glyph_room":
        slow("✨ You enter a room covered in glowing glyphs.")
        gain = random.randint(8, 20)
        player["knowledge"] += gain
        slow(f"You study the glyphs. Knowledge +{gain}!")

    else:  # forgotten_archive
        slow("📚 You find a tiny forgotten archive filled with scroll fragments.")
        player["inventory"]["scroll fragments"] = player["inventory"].get("scroll fragments", 0) + 3
        slow("You collect 3 Scroll Fragments!")

    time.sleep(1)

# -----------------------------------
# Main Exploration Events
# -----------------------------------
def explore_library():
    slow("You wander deeper into the ancient library...")
    time.sleep(1)

    # Rare secret room or hidden passage
    secret_chance = random.randint(1, 20)
    if secret_chance == 1:
        secret_room_event()
        return
    elif secret_chance == 2:
        hidden_passage_event()
        return

    # Standard exploration events
    event = random.choice(["tome", "ladder", "dust_spirit", "nothing"])

    if event == "tome":
        slow("📘 You discover a glowing ancient tome.")
        gained = random.randint(5, 20)
        player["knowledge"] += gained
        slow(f"You absorb its wisdom. Knowledge +{gained}!")

    elif event == "ladder":
        slow("🪜 You climb a tall rolling ladder to inspect a high shelf...")
        if random.randint(1, 10) <= player["knowledge"] // 10 + 2:
            slow("You find a ⭐ Bookmark of Insight!")
            player["inventory"]["insight bookmark"] = player["inventory"].get("insight bookmark", 0) + 1
            slow("Energy +10!")
            player["energy"] += 10
        else:
            slow("You slip slightly! Energy -5.")
            player["energy"] -= 5

    elif event == "dust_spirit":
        slow("🌬 A swirling dust spirit appears...")
        if random.randint(1, 10) <= player["knowledge"] // 10:
            slow("You calm the spirit with a phrase you recall. Knowledge +10!")
            player["knowledge"] += 10
        else:
            slow("The spirit startles you! Energy -10.")
            player["energy"] -= 10

    else:
        slow("The shelves groan softly as they shift around you...")

    time.sleep(1)

# -----------------------------------
# Choose a Library Section
# -----------------------------------
def choose_section():
    slow("You reach a grand intersection of glowing hallways.")
    slow("Three enchanted signs hover in the air:")
    slow("📘 History Wing")
    slow("🔮 Arcane Wing")
    slow("🐉 Mythology Wing")

    valid = {"history", "arcane", "mythology", "h", "a", "m"}
    while True:
        raw = input("\nWhich way do you go? (history / arcane / mythology): ")
        choice = raw.strip().lower()
        if choice in valid:
            if choice == "h":
                choice = "history"
            elif choice == "a":
                choice = "arcane"
            elif choice == "m":
                choice = "mythology"
            break
        else:
            slow("I didn't understand that. Please type 'history', 'arcane', or 'mythology' (or h/a/m).")

    if choice == "history":
        slow("\n📘 You step into the History Wing...")
        slow("Ancient knowledge settles into your mind.")
        player["knowledge"] += 7
        slow("Knowledge +7!")

    elif choice == "arcane":
        slow("\n🔮 You walk into the Arcane Wing...")
        slow("Magic sparks unpredictably around you.")
        energy_change = random.choice([-10, -5, 0, +5])
        knowledge_gain = random.randint(5, 15)
        player["energy"] += energy_change
        player["knowledge"] += knowledge_gain
        if energy_change < 0:
            slow(f"The magic drains you. Energy {energy_change}.")
        elif energy_change > 0:
            slow(f"A magical surge empowers you! Energy +{energy_change}.")
        else:
            slow("You feel nothing change...")
        slow(f"Knowledge +{knowledge_gain}!")

    else:  # mythology
        slow("\n🐉 You enter the Mythology Wing...")
        slow("Statues of legendary beasts watch silently from the shadows.")
        roll = random.randint(1, 10)
        if roll <= 3:
            slow("A stone gargoyle startles you! Energy -8.")
            player["energy"] -= 8
        elif roll <= 7:
            slow("You study a runic tablet. Knowledge +8!")
            player["knowledge"] += 8
        else:
            slow("A mythical guardian blesses you. Energy +10!")
            player["energy"] += 10

    time.sleep(1)

# -----------------------------------
# Final Challenge – Determine if Player Finds Scrolls
# -----------------------------------
def find_scrolls():
    global unique_event_triggered

    # Ensure at least one unique event occurred
    if not unique_event_triggered:
        slow("\n✨ A sudden shimmer catches your eye...")
        slow("A mystical apparition briefly appears, whispering forgotten secrets.")
        gained = random.randint(5, 15)
        player["knowledge"] += gained
        slow(f"Knowledge +{gained} from the mystic encounter!")
        unique_event_triggered = True

    slow("\n🔎 You reach the deepest chamber of the ancient library...")
    time.sleep(1)

    if player["knowledge"] >= 25 and player["energy"] > 0:
        end_game()
        return True
    else:
        end_game()
        return False

# -----------------------------------
# Grand Endings
# -----------------------------------
def end_game():
    slow("\nThe library trembles as you reach the final chamber...")

    if player["knowledge"] >= 25 and player["energy"] > 0:
        # SUCCESS ENDING
        slow("\n✨ A pedestal rises from the marble floor, bathed in golden light.")
        slow("The Lost Scrolls of Alexandria unseal themselves as you approach.")
        slow("Ancient glyphs swirl upward, circling your body like ribbons of fire.")
        slow("You touch the scrolls—")
        slow("\nAnd everything *erupts* inside you.")
        slow("A tidal wave of forgotten history, myth, science, and magic pours into your mind.")
        slow("You feel every civilization, every scholar, every lost voice whispering their truths to you.")
        slow("Your thoughts expand outward, stretching beyond the library, beyond time itself.")
        slow("In this moment, you understand everything humans once knew... and everything they were meant to discover.")
        slow("\nThe library bows to you — its new master of knowledge.")
        slow("Light consumes your vision, pulling you upward—")
        slow("When it fades, you awaken not in your world, but in a place shaped by your newfound wisdom.")
        slow("\n***You have reclaimed the Lost Scrolls of Alexandria.***")
        slow("***The forgotten knowledge of humanity now lives within you.***")

    else:
        # FAILURE ENDING
        slow("\n⚠️ The chamber darkens. The floor shakes beneath your feet.")
        slow("Shelves twist unnaturally, groaning like wounded beasts.")
        slow("The walls begin to close in, stone grinding against stone.")
        slow("You sprint toward an exit — any exit — but the passages collapse faster than you can run.")
        slow("Books fall. Lanterns shatter. The air thickens like quicksand.")
        slow("\nA whisper echoes behind you:")
        slow("   'All knowledge must be earned.'")
        slow("A final blast of cold air slams into you — and everything goes black.")
        slow("\nYou snap awake in your own bed, heart racing.")
        slow("The dream dissolves around you… but something lingers.")
        slow("You remember the chance you had… the knowledge you *almost* grasped…")
        slow("And the aching realization that you left the Lost Scrolls unfound.")
        slow("\n***You failed to retrieve the Lost Scrolls of Alexandria.***")
        slow("***The wisdom of the ancient world remains forever beyond your reach.***")

# -----------------------------------
# Stats Summary
# -----------------------------------
def show_stats():
    slow("\n📊 --- Your Stats ---")
    slow(f"Name: {player['name']}")
    slow(f"Energy: {player['energy']}")
    slow(f"Knowledge: {player['knowledge']}")
    if player['inventory']:
        slow("Inventory:")
        for item, qty in player['inventory'].items():
            slow(f"  - {item}: {qty}")
    else:
        slow("Inventory: Empty")
    slow("------------------\n")

# -----------------------------------
# MAIN GAME LOOP
# -----------------------------------
def main():
    intro()

    # player explores the library 3 times
    for _ in range(3):
        explore_library()
        choose_section()

    # final challenge
    find_scrolls()

    # show stats at the end
    show_stats()

    slow("\n📘 Thank you for playing! Until next time, seeker of knowledge!\n")

# -----------------------------------
# Run the Game
# -----------------------------------
if __name__ == "__main__":
    main()