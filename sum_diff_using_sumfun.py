def input1(arr):
    size=int(input("enter the size of n:"))
    for x in range(size):
        n=int(input("enter the values of n:"))
        arr.append(n)
        x+=1
    return arr

def sum_n(arr):
    add=0
    add=sum(arr)
    return add
        

def output(arr,res):
    print("sum of",arr,"is:",res)


def main():
    arr=[]
    arr=input1(arr)
    res=sum_n(arr)
    output(arr,res)

main()

