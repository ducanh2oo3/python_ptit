for t in range(int(input())):
    arr = list(int(i) for i in input())
    for i in range(len(arr) - 1, 0, -1):
        if arr[i] >= 5:
            arr[i - 1] = arr[i - 1] + 1
        arr[i] = 0
        if arr[i] ==10:
            arr[i]=0
            arr[i-1]=arr[i-1]+1
    if arr[0] == 10:
        arr[0] = 0
        arr.insert(0, 1)
    for i in arr:
        print(i, end='')
    print()