def myabs(x):
    if x<0:
        x = -x
    return x

while True:
    a = (input("> "))
    print(a, myabs(a))
