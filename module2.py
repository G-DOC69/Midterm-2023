def MSF(array):
    if len(array)>1:
        mid = len(array) // 2
        left =array[:mid]
        right=array[mid:]
        MSF(left)
        MSF(right)
        i=j=order=0
        while i<len(left) and j<len(right):
            if left[i] <= right [j]:
                array[order]=left[i]
                i+=1
            else:
                array[order]=right[j]
                j+=1
            order+=1
        while i<len(left):
            array[order]=left[i]
            i+=1
            order+=1
        while j<len(right):
            array[order]=right[j]
            j+=1
            order+=1
def subsetUtil ( A , subset = [] , index = 0 ):
    print(*subset)
    for i in range (index, len(A)):
        subset.append(A[i])
        subsetUtil(A,subset,i+1)
        subset.pop(-1)
while True:
    h1=input('Do you want any array to be sorted ? (Y/N) ')
    if h1.lower()=="yes" or h1.lower()=="y":
        x=[]
        print("Current array is empty : ",x)
        a=int(input('How many elements do you want in your array ? '))
        for m in range(0,a):
            element=float(input('Enter element : '))
            x.append(element)
        print("This is your current array : ",x)
        s=input('Which way do you want it to be sorted ? (merge, quick available) ')
        if s=="merge" or s=="MSF":
            MSF(x)
            print("Here's your merge-sorted array",x)
        else:
            print("there is no such function in our program yet")
    h2=input('Do you want to find all possible subsets in a set ? (Y/N) ')
    if h2.lower()=="yes" or h2.lower()=="y":
        A=[]
        print("Current set is empty ",A)
        a=int(input("How many elements do you want in your set ? "))
        for m in range (0,a):
            element=float(input('Enter element : '))
            A.append(element)
        print("This is your current set : ",A)
        print("Here are all possible subsets of your set : ")
        subsetUtil(A)
    h0=input('Do you want the program to start over ? (Y/N) ')
    if h0.lower()=="no" or h0.lower()=="n":
        break
    else:
        continue