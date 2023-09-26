# Kenean Nooks

# 9/26/23

# Travel Expense Calculator


budget = int(input('Enter Budget: '))
Dest = input('Enter your travel destination: ')
AssumedGas = int(input('How much do you think you will spend on gas?'))
ApproxHotel = int(input('Approximately, how much will you need for accomodation/hotel?'))
food = int(input('Last, how much do you need for food?'))
expenses = AssumedGas + ApproxHotel + food


print('------------Travel Expenses------------')
print(f'Location: {Dest}')
print(f'Initial Budget: {budget}\n')
print(f'Fuel: {AssumedGas}')
print(f'Accomodation: {ApproxHotel}')
print(f'Food: {food}\n')
print(f'Remaining Balance: {budget - expenses}')


