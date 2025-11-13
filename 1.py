class solutions:
    def recurpalind(s:str)->int:
        if len(s)==1:
            return True
        if s[0]!=s[-1]:
            return False
        return solutions.recurpalind(s[1:-1])