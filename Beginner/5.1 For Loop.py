import random

rolls=[random.randint(1, 6) for _ in range(20)]
count_6=0
count_1=0
count_two_6s_in_row=0

for i in range(len(rolls)):
    if rolls[i]==6:
        count_6+=1
    if rolls[i]==1:
        count_1+=1
    if i > 0 and rolls[i] == 6 and rolls[i - 1] == 6:
        count_two_6s_in_row+=1

print(f"  All simulated rolls: {rolls}")
print(f"  Number of times a 6 was rolled: {count_6}")
print(f"  Number of times a 1 was rolled: {count_1}")
print(f"  Number of times two 6s were rolled back-to-back: {count_two_6s_in_row}")
