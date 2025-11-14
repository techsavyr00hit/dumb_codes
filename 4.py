def recurfibo(a:int,b:int,iter:int,count:int)->int:
    if iter==count:
        return a
    return recurfibo(b,a+b,iter,count+1)