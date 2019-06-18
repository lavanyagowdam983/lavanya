def input1():
    a=int(input("enter a:"))
    b=int(input("enter b:"))
    c=int(input("enter c:"))
    return a,b,c

def max1(a,b,c):
    if(a>=b) and (a>=c):
        larg=a

    elif(b>=c):
        larg=b
    else:
        larg=c
    return larg

def output(lag):
    print("largest is:",lag)

def main():

    a,b,c=0,0,0
    lag=0
    a,b,c=input1()
    lag=max1(a,b,c)
    output(lag)

main()
