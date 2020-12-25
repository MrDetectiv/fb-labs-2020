def GCD_recursive(a,b):
           if (a*a+b*b==0):
                  return None
           elif (a*b==0):
                  return max(a,b)
           if (a%b == 0):
                  return b
           else:
                  return GCD_recursive(b,a%b)
def GCD(a,b):
       d=GCD_recursive(a,b)
       if d is None:
              return None
       else:
              return abs(d)
def reverse_mod(a,m):
       if a>m:
              tmp=a
              a=m
              m=tmp
       if  GCD(a,m)!=1:
              return None
       #print("a={}, m={}".format(a,m))
       if a==1:
              return 1
       x=[m//a]
       r=[m, a, m%a]
       while r[len(r)-1]!=1:
              x.append(r[len(r)-2]//r[len(r)-1])
              r.append(r[len(r)-2]%r[len(r)-1])
       #print("x: {}".format(x))
       #print("r: {}".format(r))
       i=len(x)-1
       #j=len(r)-2
       b=1
       c=-x[len(x)-1]
       while i>0:
              #print("{} * {} + {} * {} = 1".format(r[j-1], b, r[j], c))
              #j-=1
              i-=1
              b_copy=b
              b=c
              c=b_copy-c*x[i]
       #print("{} * {} + {} * {} = 1".format(r[0], b, r[1], c))
       return c%m


class LINEAR_EQUATION:
       def __init__(this, a, b, n):
              this.a = a
              this.b = b
              this.n = n
       def print(this):
              print("Equation: {} * x = {} mod ( {} )".format(this.a%this.n, this.b%this.n, this.n))
       def solve(this):
              if this.a==0 or this.n==0 or this.n==1:
                     return None              
              d=GCD(this.a,this.n)
              if d>1:
                     if this.b%d!=0:
                            return None
                     else:
                            a=this.a//d
                            b=this.b//d
                            n=this.n//d
                            x0=reverse_mod(a,n)*b%n
                            x = []
                            for i in range(1,d):
                                   x.append(x0+i*n)
                            return x
              else:
                     return [reverse_mod(this.a,this.n)*this.b%this.n]
class XY_LINEAR_EQUATION:
       def __init__(this, X1, Y1, X2,Y2,n):
              this.X1 = X1
              this.Y1 = Y1
              this.X2 = X2
              this.Y2 = Y2
              this.n = n
       def print(this):
              print("XY Equation: {} = {} * a + b mod ( {} )".format(this.Y1%this.n, this.X1%this.n, this.n))
              print("                        {} = {} * a + b mod ( {} )".format(this.Y2%this.n, this.X2  %this.n, this.n))
       def solve(this):
              LQ = LINEAR_EQUATION((this.X1-this.X2)%this.n, (this.Y1-this.Y2)%this.n, this.n)
              #LQ.print()
              a=LQ.solve()
              if a is None:
                     #print("lin eq returned None!!!!")
                     return None
              b=[]
              for i in a:
                     b.append((this.Y1-i*this.X1)%this.n)
              result = []
              for i in range(0,len(a)):
                     result.append((a[i],b[i]))
              return result

                     
       
       
