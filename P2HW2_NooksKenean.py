# CTI-110
# P2HW2 - List
# Kenean
# 10/10/23


#Create a List, Take input
print("You'll be entering a list of grades, for modules 1-6")

lstOfGrades = [ float(input('For module 1: ')),
               float(input('For module 2: ')),
               float(input('For module 3: ')),
               float(input('For module 4: ')),
               float(input('For module 5: ')),
               float(input('For module 6: '))]

 
#Print lowest, highest, sum, and average values of lstofgrades respectively.    
print('\nLowest: ', min(lstOfGrades))
print('Highest: ', max(lstOfGrades))
print('Sum: ', sum(lstOfGrades))
print('Average: ', sum(lstOfGrades)/len(lstOfGrades))