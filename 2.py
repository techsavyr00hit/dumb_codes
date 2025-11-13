class solutions:
    def recurfact(n:int)->int:
        if n==0 or n ==1:
            return 1
        return n*solutions.recurfact(n-1)