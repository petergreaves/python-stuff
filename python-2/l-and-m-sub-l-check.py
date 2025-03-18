'''

Write a program that asks the user to input an orbital quantum number
l and a magnetic quantum number
m sub l,  and then checks that the value of m sub l
  is consistent with the value of l.
'''

# vars and lists
lValues = [0, 1, 2, 3]
mSubLValues = [[0], [0, 1], [0, 1, 2], [0, 1, 2, 3]]
lValue = int(input("enter an l value: "))
mSubLValue = int(input("enter an m sub l value: "))
found = False

# find the list of m sub l
msublList = mSubLValues[lValue]
for v in msublList:
    if v == abs(mSubLValue):
        print(str(v) + " is a valid magnetic quantum number in an l orbital of type " + str(lValue))
        found = True
        exit(0)
#we fell thru to here
if not found:
    print(str(v) + " is not valid for the l orbital of type " + str(lValue))
