n=int(input())
for i in range(n):
    def factorial_find(A):
        if (A==0):
            return 1
        return factorial_find(A-1)*A
    print(factorial_find(int(input())))
