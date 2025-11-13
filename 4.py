def recurfibo(n:int)->int:
    if n<=1:        
        return n
    return recurfibo(n-1)+recurfibo(n-2) 