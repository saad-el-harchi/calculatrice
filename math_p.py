"""
    
    @authors:-saad el harchi
             -aziagba romuald
    
    this module consists of many functions that represent predefined 
    mathematical functions :-cos
                            -sin
                            -tan
                            -cotan
                            -exp
                            -ln
"""
import math

class math_p:
    
    expression=""
    epsilone=0.000001
    inf=100
    e=2.71828182846
   
    def exp(self,x):
        """
        takes exactly one argument and returns e^x using the limited 
        development of e.
        """
        if x == 1:
            return math_p.e
        elif x == 0:
            return 1
        else:
            dev=0.0
            fact=1.0
            dev+=1+x
            for i in range(2,math_p.inf):
                fact*=i
                dev+=(x**i)/fact
            return dev
    
    def cos(self,x):
        """
        takes one argument and returns the cosin value of x.
        """
        
        if x <360 :
            dev=0.0
            fact=1.0
            dev+=1
            for i in range(2,math_p.inf,2):
                fact*=i*(i-1)
                dev+=((-1)**(i//2+1))*((x**(i))/fact)
            return dev
        else:
            while x >= 360:
                x-=360
            dev=0.0
            fact=1.0
            dev+=1
            for i in range(2,math_p.inf,2):
                fact*=i*(i-1)
                dev+=((-1)**(i//2+1))*((x**(i))/fact)
            return dev
    def sin(self,x):
        """
        takes one argument and returns the sin value of x.
        """
        if x <360 :
            dev=0.0
            fact=1.0
            dev+=x
            for i in range(1,math_p.inf,2):
                fact*=i*(i-1)
                dev+=((-1)**((i//2)+1))*((x**(i)/fact))
            return dev
        else:
            while x >= 360:
                x-=360
            dev=0.0
            fact=1.0
            dev+=x
            for i in range(1,math_p.inf,2):
                fact*=i*(i-1)
                dev+=((-1)**((i//2)+1))*((x**(i)/fact))
            return dev
    def tan(self,x):
        """
        takes one argument and returns the tangent value of x usig both 
        projet.cos and projet.sin .
        """
        return math_p.sin(self,x)/math_p.cos(self,x)
    def cotan(self,x):
        """
        takes one argument and returns the tangent value of x usig both 
        projet.tan .
        """
        return 1/math_p.tan(self,x)
    def ln(self,x):
        """
        takes exactly one argument and returns ln(x) using the limited 
        development of ln(1+(x-1)).
        """
        t = (x-1)/(x+1)
        tc = t*t
        s1 = t
        n = 0
        while True:
            n += 1
            t *= tc*(2*n-1)/(2*n+1)
            s2 = s1 + t
            if s2 == s1:
                break
            s1 = s2
        return 2*s2  
    
        
        
            
            
            
            
            
            
            
            
                