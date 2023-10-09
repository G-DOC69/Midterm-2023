def SSF(array):
    for i in range(0,len(array)):
        for j in range (i+1,len(array)):
            if array[j]<=array[i]:
                array[i],array[j]=array[j],array[i]
def ISF(array):
    for i in range(1,len(array)):
        current_value=array[i]
        j=i-1
        while j>=0 and array[j]>current_value:
            array[j+1]=array[j]
            j=j-1
        array[j+1]=current_value
def BSF(array):
    for i in range (0,len(array)):
        for j in range (0,len(array)-i-1):
            if array[j]>=array[j+1]:
                temporary_value=array[j]
                array[j]=array[j+1]
                array[j+1]=temporary_value
def pair_sum(array):
    target_sum=float(input('what is your target sum ? '))
    for i in range(0,len(array)):
        for j in range (i+1,len (array)):
            if array[i]+array[j]==target_sum:
                print(array[i],",",array[j])
def matrix_func():
    Row = int(input("Enter the number of rows:"))
    Column = int(input("Enter the number of columns:"))
    matrix=[]
    print("Enter the entries row wise:")
    for row in range(Row):    
        a = []
        for column in range(Column):   
            a.append(int(input()))
        matrix.append(a)
    for row in range(Row):
        for column in range(Column):
            print(matrix[row][column], end="   ")
        print()
def substring_find():
    x=input("enter your string : ")
    z=input("enter your substring : ")
    c=[]
    for i in range(len(x)):
        if x[i] == z[0]:
            for j in range (0,len(z)):
                if x[i+j]==z[j]:
                    if len(z)-1 == j:
                        c.append(i)
    print("Here are positions of <",z,"> in your string : ",c)
while True:
    jh=input('Do you want any array to be sorted ? (Y/N) ')
    if jh.lower()=="yes" or jh.lower()=="y":
        x=[]
        print("Current array is empty : ",x)
        a=int(input('How many elements do you want in your array ? '))
        for m in range(0,a):
            element=float(input('enter element : '))
            x.append(element)
        print("This is your current array : ",x)
        s=input('Which way do you want it to be sorted ? (bubble,insertion,selection,available) ')
        if s=="bubble" or s=="BSF":
            SSF(x)
            print("Here's your bubble-sorted array",x)
        elif s=="insertion" or s=="ISF":
            ISF(x)
            print("Here's your insertion-sorted array",x)
        elif s=="selection" or s=="SSF":
            SSF(x)
            print("Here's your selection-sorted array",x)
        else:
            print("there is no such function in our program yet")
    kh=input("Do you want to find a target sum using pair of numbers in a given array ? (Y/N) ")
    if kh.lower()=="yes" or kh.lower()=="y":
        x=[]
        print("Current array is empty : ",x)
        a=int(input('How many elements do you want in your array ? '))
        for m in range(0,a):
            element=float(input('enter element : '))
            x.append(element)
        print("This is your current array : ",x)
        pair_sum(x)
    mh=input("Do you want to do a matrix output ? (Y/N) ")
    if mh.lower()=="yes" or mh.lower()=="y":
        matrix_func()
    sh=input("Do you want to find substring in a string ? (Y/N) ")
    if sh.lower()=="yes" or sh.lower()=="y":
        substring_find()
    hh=input('Do you want the program to start over ? (Y/N) ')
    if hh.lower()=="no" or hh.lower()=="n":
        break
    else:
        continue
# end