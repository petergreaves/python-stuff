'''
Write down a similar Python instruction that will build the list of all possible values of the magnetic quantum number
m sub l for a state of the hydrogen atom with orbital quantum number l = 2
'''


lValue=3
mSubLValues = []
start = -lValue
end = lValue
k = start
while (k <= end):
    mSubLValues.append(k)
    k+=1
print ("The possible magnetic quantum number values m sub l for orbital quantum number",lValue, "are",mSubLValues)
