print("hello world")

# Write your program here
items = [1.45, 2, 0.25, 4.4, 1.9] # list of masses in kg
totItems = 0    # Set total items to inital value of 0
itemsValue = 0.0 # Set total value to inital value of 0.0
for item in items:                # Iterate through the list of items with each element as item
    totItems += 1
    itemsValue += item # add to the total  value
print ("Number of items:",totItems) # Print the total items
print ("Number of items:",len(items)) # Print the total items (len)
print ("Total value of items:",round(itemsValue,2)) # Print the total value
print ("Sum:",round(sum(items),2)) # Print the total value (sum)