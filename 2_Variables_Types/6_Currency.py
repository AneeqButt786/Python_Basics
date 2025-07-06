"""
Here is a mini project for your practice.

Currency Converter is used to find the currencies in USD Dollars ($)
"""
pesos = int(input('What do you have left in pesos? '))
soles = int(input('What do you have left in soles? '))
reais = int(input('What do you have left in reais? '))

pes_to_usd = pesos * 0.00025
sol_to_usd = soles * 0.28
rea_to_usd = reais * 0.21

total = pes_to_usd + sol_to_usd + rea_to_usd

print(total)