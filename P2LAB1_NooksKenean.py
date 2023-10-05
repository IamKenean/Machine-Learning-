#Kenean Nooks
#10/5/2023
#estimating gascost

#take mileage and gascost
mileage = float(input())
gascost = float(input())

#for 20, 75, and 500 miles...
miles20 = 20 
miles75 = 75
miles500 = 500

#calculate the cost of gas
gascost20 = (miles20/mileage) * gascost
gascost75 = (miles75/mileage) * gascost
gascost500 = (miles500/mileage) * gascost

#print the gascosts in a f string.
print(f'{gascost20:.2f} {gascost75:.2f} {gascost500:.2f}')

