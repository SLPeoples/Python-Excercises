#Samuel L. Peoples

#use of a default greeting and parameter
def SayHello(Greeting = "Hello"):
    print(Greeting)

#adds two values    
def DisplaySum(Value1, Value2):
    print(str(Value1) + ' + ' + str(Value2) + ' = ' + str((Value1+Value2)))

#variable arguments    
def DisplayMulti(argCount = 0, *varArgs):
    print(str(argCount)+' arguments', varArgs)

#if statement example
def testVal(val):
    if val == 5:
        print('val is five')
    elif val == 6:
        print('val is six')
    else:
        print('val is ' +str(val))

#Determines whether a user-input is valid
def secretNum():
    gotIt = False
    while gotIt == False:
        one = int(input("Type a number between one and ten "))
        two = int(input("Type a number between one and ten "))
        if(one >= 1) and (one <=10):
            if(two >= 1) and (two <=10):
                print('your num is '+str(one*two))
                gotIt == True
                break
            else:
                print ("val2 bad")
        else:
            print ("val1 bad")
        print('Try Again')
     
#Overloaded
def DisplayMulti(*varArgs):
     for arg in varArgs:
         if arg.upper() == 'CONT':
             continue
             print('Continue..'+arg)
         elif arg.upper() == 'BREAK':
             break
             print('Break..'+arg)
         print('Good..'+arg)
#sets
def sets():
    colors = set(['red','blue','green','orange'])
    objects = set(['vase', 'ball', 'car','orange'])
    uni = colors.union(objects)
    inter = colors.intersection(objects)
    diff = colors.difference(objects)
    for item in colors:
        print(item)
    for item in objects:
        print(item)
    print ('***union***')
    for item in uni:
        print(item)
    print ('***intersection***')
    for item in inter:
        print(item)
        print ('***difference***')
    for item in diff:
        print(item)
     
#lists
def lists():
    listA = [0,1,2,3]
    listB = [4,5,6,7]
    listA.extend(listB)
    print(listA)
    listA.append(-2)  
    print(listA)
    listA = [0,1,2,3]
    listB = [4,5,6,7]
    listA += listB
    print (listA)
    for value in listA[2:5]:
        print(value)
    
#tuples
def tuples():
    myTuple = (1,2,3,(4,5,6,(7,8,9)))
    
    for val1 in myTuple:
        if type(val1)== int:
            print (val1)
        else:
            for val2 in val1:
                if type(val2)==int:
                    print ("\t", val2)
                else: 
                    for val3 in val2:
                        print ("\t\t", val3)
def main():
    #SayHello()
    #SayHello("GoodBye")
    #DisplaySum(2, 2)
    #DisplayMulti(4)
    #DisplayMulti(2,3,'H')
    #testVal(1)
    #testVal(5)
    #testVal(6)
    #secretNum()
    #DisplayMulti('Start','CONT','Continue','CONT','CONT','BREAK', 'Broken')
    #sets()
    #lists()
    tuples()

if __name__ == "__main__": main()