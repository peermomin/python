import random

# 1️⃣ random.random() → Returns float in [0.0, 1.0)
print("random.random():", random.random())  # Example: 0.4352 (0 inclusive, 1 exclusive)

# 2️⃣ random.uniform(a, b) → Float in [a, b]
print("random.uniform(10, 20):", random.uniform(10, 20))  # Example: 14.76

# 3️⃣ random.randint(a, b) → Integer in [a, b]
print("random.randint(1, 6):", random.randint(1, 6))  # Simulates dice (1 to 6 inclusive)

# 4️⃣ random.randrange(start, stop, step) → Integer in [start, stop), like range()
print("random.randrange(0, 10, 2):", random.randrange(0, 10, 2))  # Even numbers: 0, 2, ..., 8

# 5️⃣ random.choice(seq) → Pick one item from sequence
colors = ['red', 'blue', 'green']
print("random.choice(colors):", random.choice(colors))  # Example: 'blue'

# 6️⃣ random.choices(seq, k=n) → Pick n items (with replacement, can repeat)
print("With replacement")
i = 0
for i in range(10):
    print("random.choices(colors, k=3):", random.choices(colors, k=2))  # Example: ['green','red']

# 7️⃣ random.sample(seq, k=n) → Pick n unique items (no replacement)
print("wihout replacement")
i = 0
for i in range(10):
    print("random.sample(colors, k=2):", random.sample(colors, k=2))  # Example: ['red', 'blue']

# 8️⃣ random.shuffle(list) → Shuffles the list in-place
deck = [1, 2, 3, 4, 5]
random.shuffle(deck)
print("random.shuffle(deck):", deck)  # Shuffled version like [3, 1, 4, 5, 2]

# 9️⃣ random.seed(n) → Fix randomness for reproducibility
random.seed(42)
print("random.random() with seed 42:", random.random())  # Same output every time

# 🔟 random.gauss(mu, sigma) → Returns float from Gaussian (normal) distribution
print("random.gauss(0, 1):", random.gauss(0, 1))  # Mean=0, StdDev=1, value like -0.15

# BONUS: Simulate a dice roll using randint
def roll_dice():
    return random.randint(1, 6)

print("You rolled a dice and got:", roll_dice())
