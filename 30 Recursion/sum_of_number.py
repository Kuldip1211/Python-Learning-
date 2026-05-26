def totalsum(n):
    if(n == 0):
        return 0
    else : 
        return n + totalsum(n-1)
    
ans = totalsum(15);
print(ans);