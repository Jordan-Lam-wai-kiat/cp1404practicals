import random

"""The smallest number would be 5 and the largest would be 20"""
print(random.randint(5, 20))  # line 1
"""the smallest number would be 3, while the largest would be 9, 4 will not be a valid number as any values returned would be in intervals of 2 starting from 3."""
print(random.randrange(3, 10, 2))  # line 2
"""The smallest number would be 2.5 and the largest would be 5.5"""
print(random.uniform(2.5, 5.5))  # line 3
"""Code to produce a random number between 1 and 100 inclusive."""
print(random.randint(1, 100))

