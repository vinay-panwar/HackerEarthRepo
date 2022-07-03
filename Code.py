T = int(input()) #number of test cases

for i in range(T) :
    ls = input().split()#first is length array and second is lenght of sub array
    A = input().split()  # array 
    N = int(ls[0]) #length of Array
    K = int(ls[1]) # length of sub array
    A = [int(x) for x in A]
    A.sort(reverse=True)
    add = 0
    val = 0
    for i in range(K) :
        count = A.count(A[val])
        #print(A[val])
        if count == 1 :
            add += A[val]
        else :
            for i in range(count) :
                add +=A[val]
        val +=1
        #print(add)
    print(add)
