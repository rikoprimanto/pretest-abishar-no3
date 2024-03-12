def bubbleSort(arr):
    n = len(arr)
    outer = 1
    for i in range(n-1):
        print("outer #",1)
        for j in range(n-1,0+i,-1):
            kondisi = arr[j] > arr[j-1]
            if kondisi:
                arr[j],arr[j-1] = arr[j-1],arr[j]
            print(f"is data[{j}] > data[j-1] ? {kondisi} , Data :",arr)
    outer += 1

b = [3,2,5,1,8,9,6]
bubbleSort(b)