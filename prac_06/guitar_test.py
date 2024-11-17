from guitar import Guitar

guitar1 = Guitar("norman", 1984, 1934)
guitar2 = Guitar("gusberg", 1964, 3452)

print(guitar1.get_age()) # - Expected 40. Got 40
print(guitar2.get_age()) # - Expected 60. Got 60
print(guitar1.is_vintage()) # - Expected False. Got False
print(guitar2.is_vintage()) # - Expected True. Got True