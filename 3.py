class solutions:
    def gcd(a:int,b:int)->int:
        if b==0:
            return a
        return solutions.gcd(b,a%b)