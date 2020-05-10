import random
import os

daList = []

print("Number Generator V0.1\n")

userSel = int(input("Please select a number of numbers you would like: "))

def rangen():
    rannum = random.randrange(1, 50)
    #print(rannum)
    if daList.count(rannum):
        #print('Double found')
        return
    daList.append(rannum)
    daList.sort()
    return
    
while(len(daList) < userSel):
    rangen()
    
os.system('clear')

print("\nLucky numbers: ", daList)
