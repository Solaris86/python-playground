import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# Option 1
# payer = random.choice(friends)

# Option 2
payer = friends[random.randint(0, len(friends) - 1)]


print(f"{payer} will pay the bill.")
