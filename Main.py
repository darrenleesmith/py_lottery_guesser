import random

daList = []

print("Number Generator v0.3")

userRetry = bool(1)

while(userRetry == 1):

    userSel = int(input("\nPlease select a number of numbers you would like: "))

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
    
    print("\nLucky numbers: ", daList)
    daList.clear()
    
    userCho = input("\nWould you like to try again? (type no to exit) ")
    if userCho == ("no"):
        break

print("\nEnd")
