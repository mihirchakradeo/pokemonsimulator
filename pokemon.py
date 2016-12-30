import csv
import random

user = random.randint(0,150)
computer = random.randint(0,150)
diff=userHP=computerHP=0


# Retrieving information
with open('Pokemon.csv','rb') as f:
    temp = csv.reader(f, delimiter=',')
    for r in temp:
        if r[0]==str(user):
            print "---USER---"
            print r[0]
            print r[1]
            userPkmn = r[1]
            userHP = int(r[5])
            userATK = int(r[6])
            userDEF = int(r[7])
            userSpeed = int(r[10])
            print "HP: "+`userHP`
            print "ATK: "+`userATK`
            print "DEF: "+`userDEF`
            print "SPEED: "+`userSpeed`

        elif r[0]==str(computer):
            print "---COMPUTER---"
            print r[0]
            print r[1]
            computerPkmn = r[1]
            computerHP = int(r[5])
            computerATK = int(r[6])
            computerDEF = int(r[7])
            computerSpeed = int(r[10])
            print "HP: "+`computerHP`
            print "ATK: "+`computerATK`
            print "DEF: "+`computerDEF`
            print "SPEED: "+`computerSpeed`

print "FIGHT!"
diff1 = abs(userATK - computerDEF)
diff2 = abs(computerATK - userDEF)

print "Difference: "+`diff1`+" "+`diff2`
print "--------------------------"
#Calculating whose turn it is
if userSpeed>computerSpeed:
    #user goes first
    turn=0
else:
    #computer goes first
    turn=1


def userAttack():
    print userPkmn+" Attacks!"
    global computerHP
    computerHP -= diff1
    print "USER HP: "+`userHP`
    print "COMPUTER HP: "+`computerHP`
    print "-------------------------"

def computerAttack():
    print computerPkmn+" Attacks!"
    global userHP
    userHP -= diff2
    print "USER HP: "+`userHP`
    print "COMPUTER HP: "+`computerHP`
    print "-------------------------"


while 1:
    if (userHP>0) and (computerHP>0):
        if turn==0:
            userAttack()
            turn = 1
        elif turn==1:
            computerAttack()
            turn=0
    else:
        if userHP<0:
            print computerPkmn+" (Computer) Wins!"
            break
        else:
            print userPkmn+" (User) Wins!"
            break
