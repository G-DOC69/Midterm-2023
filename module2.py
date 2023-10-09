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
        s=input('Which way do you want it to be sorted ? (merge, quick available) ')
        if s=="merge" or s=="MSF":
            MSF(x)
            print("Here's your merge-sorted array",x)
        else:
            print("there is no such function in our program yet")