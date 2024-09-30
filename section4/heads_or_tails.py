import random

heads_or_tails = random.randint(0, 1)
if heads_or_tails == 1:
    print(f"{heads_or_tails} - heads")
else:
    print(f"{heads_or_tails} - tails")