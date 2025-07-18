
try:
    print(x)
except:NameError:
    print("variable x is not defined")
finally:
    print("Everything went wrong")


x =c-1

if x < 0:
    raise Exception("sorry, no numbers below zero")