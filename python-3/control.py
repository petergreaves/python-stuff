def doSomething(x):
    print("Have done this", x, "times")

x = 0

while True:
    s = input("enter something or q to quit: ")
    if s == "q":
        print("bye - you did something", x, "times")
        break
    else:
        x += 1
        doSomething(x)
