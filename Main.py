import random
daList = []

def rangen():
    rannum = random.randrange(1, 50)
    #print(rannum)
    if daList.count(rannum):
        #print('Double')
        return
    daList.append(rannum)
    daList.sort()
    return
    
while(len(daList) < 7):
    rangen()

print(daList)
