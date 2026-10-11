import random
import time

ROSTER = [
    {"name": "Python Sensei", "hp": 100, "attack": (5, 20), "phrase": "Where are your PRs?!"},
    {"name": "Cyborg Bob", "hp": 110, "attack": (5, 10), "phrase": "Beep boop!"},
    {"name": "Deadline Student", "hp": 80, "attack": (10, 40), "phrase": "It works on my machine!"},
    {"name": "Idit the Debugger", "hp": 95, "attack": (8, 22), "phrase": "Fixed it. Ship it!"},  # --- ADD HERE ---
]

# =====================================================================

def battle(fighter1, fighter2):
    """Fight two bots 1v1. They take turns dealing random damage until one hits 0 HP.

    Returns the winning fighter dict (the champion keeps leftover HP).
    """
    print(f"\n{'='*40}")
    print(f"⚔️ {fighter1['name']} VS {fighter2['name']} ⚔️")
    print(f"{'='*40}")
    time.sleep(1)
    
    hp1, hp2 = fighter1['hp'], fighter2['hp']
    
    while hp1 > 0 and hp2 > 0:
        # First fighter attacks
        dmg1 = random.randint(*fighter1['attack'])
        hp2 -= dmg1
        print(f"🥊 {fighter1['name']} deals {dmg1} damage! ({fighter2['name']}: {max(0, hp2)} HP)")
        time.sleep(0.5)
        
        if hp2 <= 0:
            print(f"\n🏆 VICTORY! {fighter1['name']} shouts: «{fighter1['phrase']}»")
            return fighter1
            
        # Second fighter attacks
        dmg2 = random.randint(*fighter2['attack'])
        hp1 -= dmg2
        print(f"🥊 {fighter2['name']} deals {dmg2} damage! ({fighter1['name']}: {max(0, hp1)} HP)")
        time.sleep(0.5)
        
        if hp1 <= 0:
            print(f"\n🏆 VICTORY! {fighter2['name']} shouts: «{fighter2['phrase']}»")
            return fighter2

def run_tournament(fighters):
    """Run a battle-royale tournament: shuffle the roster, then the winner of each
    match stays in the arena and immediately fights the next challenger.

    Needs at least two fighters. Prints the absolute champion at the end.
    """
    print("📢 WELCOME TO THE TOURNAMENT!")
    if len(fighters) < 2:
        print("Not enough fighters! Make a Pull Request!")
        return
        
    random.shuffle(fighters)
    
    # Simplified "Battle Royale" - the winner fights the next challenger
    champion = fighters[0]
    for challenger in fighters[1:]:
        champion = battle(champion, challenger)
        print("\n" + "🌟"*10)
        print(f"CURRENT CHAMPION: {champion['name']}")
        print("🌟"*10)
        time.sleep(2)
        
    print(f"\n🎉 ABSOLUTE TOURNAMENT CHAMPION: {champion['name']}! 🎉")

if __name__ == "__main__":
    # Start the tournament when this file is run directly
    run_tournament(ROSTER)

print("adar")
