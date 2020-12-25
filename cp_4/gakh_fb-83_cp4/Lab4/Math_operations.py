def fast_power(x,a,m): # you get x**a % m using Gorner scheme
       a_b=bin(a)[2:][::-1]
       #print(bin(a))
       x_ans=1
       x_temp=x
       for i in range(0,len(a_b)):
              if a_b[i] == '1':
                     x_ans = (x_ans*x_temp)%m
              x_temp = (x_temp**2)%m
       return x_ans
def generate_row(B,m): # you get array(row) for division inspection at B-basis for m(divisor)
       r=B%m
       ans=[1]
       while r!=1:
              ans.append(r)
              if r==0:
                     return ans
              r=r*B%m
       return ans
def get_numerals(x,B): # you get x at B-basis(as an array)
       if B==2:
              x_bin=bin(x)[2:][::-1]
              ans=[]
              for i in x_bin:
                     ans.append(int(i))
              return ans
       if B==16:
              x_hex=hex(x)[2:][::-1]
              ans=[]
              for i in x_hex:
                     ans.append(int('0x'+i))
              return ans
       if B==10:
              ans=[x%B]
              p=1
              while ans[-1]!=0:
                     p*=B
                     ans.append(x//p%B)
              return ans[:-1]
       else:
              return None
def check_mod(r_row,a_row,m): # you check primeness of a(True=prime), but firstly need to generate row with generate_row() for B-basis for m(divisor), get B-basis for a(number to inspect) - probably with get_numerals()
       ans=0
       if r_row[-1]==0:
              for i in range(0,len(r_row)):
                     ans+=a_row[i]*r_row[i]%m
       else:
              l=len(r_row)
              for i in range(0,len(a_row)):
                     ans+=a_row[i]*r_row[i%l]%m
       return not bool(ans%m)

