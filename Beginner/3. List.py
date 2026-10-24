justice_league = [
    "Superman",
    "Batman",
    "Wonder Woman",
    "Flash",
    "Aquaman",
    "Green Lantern",
]
print(f"Initial roster: {justice_league}\n")

count = len(justice_league)
print(f"Task 1 (Member Count): {count}")
print(f"Current List: {justice_league}\n")

justice_league.append("Batgirl")
justice_league.append("Nightwing")
print(f"Task 2 (Recruited Batgirl & Nightwing):")
print(f"Current List: {justice_league}\n")

justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print(f"Task 3 (Wonder Woman moved to leader position):")
print(f"Current List: {justice_league}\n")

justice_league.remove("Superman")
flash_idx = justice_league.index("Flash")
justice_league.insert(flash_idx + 1, "Superman")
print(f"Task 4 (Superman separated Flash and Aquaman):")
print(f"Current List: {justice_league}\n")

justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print(f"Task 5 (New Crisis Team Assembled):")
print(f"Current List: {justice_league}\n")

justice_league.sort()
print(f"Task 6 (Alphabetically Sorted Roster):")
print(f"Current List: {justice_league}")
print(f"The new leader at index 0 is: {justice_league[0]}")
