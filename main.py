daily_improvement.py
 ability = 1
day_in_cycle = 0
for _ in range(365):
    day_in_cycle += 1
    if day_in_cycle > 3 and day_in_cycle <= 7:
        ability *= 1.01
    if day_in_cycle == 7:
        day_in_cycle = 0
print(ability)
