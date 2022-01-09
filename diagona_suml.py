#!/bin/python3
def diagonalDifference(arr):
    c_l = []
    d_l = []
    for i in range(n):
        d = arr[i][i]
        c = arr[i][n-i-1]
        c_l.append(c)
        d_l.append(d)  
    c_list_sum = sum(c_l)
    d_list_sum = sum(d_l)         
    return abs(c_list_sum-d_list_sum)
    
if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    diagonalDifference(arr)
