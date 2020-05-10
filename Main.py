import random

daList = []

print("Number Generator V0.1\n")

userRetry = bool(1)

while(userRetry == 1):

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
    
    print("\nLucky numbers: ", daList)
    
    userCho = input("\nWould you like to try again? (yes or no) ")
    if userCho == ("yes"):
        daList.clear()
        userRetry = bool(1)
        
    if userCho == ("no"):
        userRety = bool(0)
        break

print("\nEnd")
