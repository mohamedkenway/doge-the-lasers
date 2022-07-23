from decimal import Decimal, localcontext
def bs(n):
    if n==0:
        return 0
    r=Decimal(2).sqrt()
    s=Decimal(2)+r
    b=int(n*r)
    bss=int(Decimal(b)/s)
    return(b*(b+1))/2-bs(bss)-bss*(bss+1)
def solution(str_n):
    with localcontext() as ctx:
        ctx.prec=102
        n=int(str_n)
        return(str(int(bs(n))))
