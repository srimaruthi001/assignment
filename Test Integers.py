#test List for integers

def testList(a):
    print(isListOfInts(a))

        
def isListOfInts(b):

    if not type(b) == list:

        raise ValueError("Input is not of List")

    if len(b) == 0:

        res = True

    else:

        res = all(isinstance(item, int) for item in b)

    return res

    

testList((1,2))   