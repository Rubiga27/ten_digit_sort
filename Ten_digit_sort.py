def ten_digit(A):
    return sorted(A,key=lambda x:((x/10)%10,-x))

A=list(map(int,input().split()))
print(ten_digit(A))

"""
Input 1:
A = [15, 11, 7, 19]
Output 1:
[7, 19, 15, 11]


Input 2:
A = [2, 24, 22, 19]
Output 2:
[2, 19, 24, 22]

"""
