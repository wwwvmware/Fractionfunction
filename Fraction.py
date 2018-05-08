def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n
   
class Fraction:
  def __init__(self,top,bottom):
    try:
      if top%1!=0 or bottom%1!=0:
        raise DecimalsError('DecimalsError')#抛出小数异常
      elif top<0 and bottom<0:
        raise RegativeError('RegativeError')
    except:
      print("请输入正确的小数或者负数")
    else:
      cfactor=gcd(top,bottom)
      self.num=top/cfactor
      self.den=bottom/cfactor
   
  def getNum(self):
    return self.num
   
  def getDen(self):
    return self.den
   
  def __add__(self,other):
    onum=other.getNum()
    oden=other.getDen()
    sumnum=self.num*oden+onum*self.den
    sumden=self.den*oden
    print(sumnum)
    print(sumden)
    onum=gcd(sumnum,sumden)
    sumnum=sumnum/onum
    sumden=sumden/onum
    return str(sumnum)+','+str(sumden)
   
  def __sub__(self,other):
    onum=other.getNum()
    oden=other.getDen()
    sumnum=self.num*oden-onum*self.den
    sumden=self.den*oden
    onum=gcd(sumnum,sumden)#出于节省变量重复使用onum作为gcd函数所求公约数的容器
    sumnum=sumnum/onum
    sumden=sumden/onum
    return str(sumnum)+','+str(sumden)
   
  def __mul__(self,other):
    onum=other.getNum()
    oden=other.getDen()
    mulnum=self.num*onum
    mulden=self.den*oden
    return str(mulnum)+','+str(mulden)
   
  def __truediv__(self,other):
    onum=other.getNum()
    oden=other.getDen()
    divnum=self.num*oden
    divden=self.den*onum
    return str(divnum)+','+str(divden)
   
  def __gt__(self,other):
    onum=other.getNum()
    oden=other.getDen()
    firstnum=self.num*oden
    secondnum=onum*self.den
    return firstnum>secondnum
   
  def __ge__(self,other):
    onum=other.getNum()
    oden=other.getDen()
    firstnum=self.num*oden
    secondnum=onum*self.den
    return firstnum>=secondnum
   
  def __lt__(self,other):
    onum=other.getNum()
    oden=other.getDen()
    firstnum=self.num*oden
    secondnum=onum*self.den
    return firstnum<secondnum
   
  def __le__(self,other):
    onum=other.getNum()
    oden=other.getDen()
    firstnum=self.num*oden
    secondnum=onum*self.den
    return firstnum>=secondnum
  def __ne__(self,other):
    onum=other.getNum()
    oden=other.getDen()
    firstnum=self.num*oden
    secondnum=onum*self.den
    return firstnum!=secondnum
f1=Fraction(-1,-2)
f2=Fraction(2,1)
print(f2/f1)
