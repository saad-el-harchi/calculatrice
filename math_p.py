"""
    Created on wed Nov  14 23:00:00 2018
    @authors:-saad el harchi
            -aziagba romuald
            
    this module is made to simulate a calculater.
    to use it you need to call to methods of the modul:
        -math_p.scan()
        -math_p.calcul()
    then after the execution you can write in the console the expression to
    be calculated(+,-,*,/,^,r).
    no spaces are allowed .
"""
class math_p:
    expression=""
    def plus(a,b):
        """ a+b """
        print("=",a+b)
        return a+b
    def moins(a,b):
        """ a-b """
        print("=",a-b)
        return a-b
    def multi(a,b):
        """ a*b """
        print("=",a*b)
        return a*b
    def divi(a,b):
        """ a/b """
        print("=",a/b)
        return a/b
    def puiss(a,b):
        """ a**b """
        print("=",a**b)
        return a**b
    def racine(a,b):
        """ a**(1/b) """
        print("=",a**(1/b))
        return a**(1/b)
    def absolute(a):
        """ |a| """
        if a<0:
            print(-a)
            return -a
        else:
            print(a)
            return a
        
    def scan():
        """gets the mathematical expression given by the user"""
        global expression
        expression = input()
    def calcul():
        """calculates and prints the value of the expression"""
        e=1
        a=0
        b=0
        
        if  expression[0] == '-' :
            while expression[e] == "0" or expression[e] == "1" or expression[e] == "2" or expression[e] == "3" or expression[e] == "4" or expression[e] == "5" or expression[e] == "6" or expression[e] == "7" or expression[e] == "8" or expression[e] == "9" :
                a=a*10+-int(expression[e])
                e+=1
            while e+1<len(expression) and expression[e+1]!="\0":
                b=b*10+int(expression[e+1])
                e+=1

            for i in range(2,len(expression)):
                
                if expression[i] == '+':
                    math_p.plus(a,b)
                elif expression[i] == '-':
                    math_p.moins(a,b)
                elif expression[i] == '/':
                    math_p.divi(a,b)
                elif expression[i] == 'r':
                    math_p.racine(a,b)
                elif expression[i] == '*':
                    math_p.multi(a,b)
                elif expression[i] == '^':
                    math_p.puiss(a,b)
                
        else:
            e=0
            b=0
            while expression[e] == "0" or expression[e] == "1" or expression[e] == "2" or expression[e] == "3" or expression[e] == "4" or expression[e] == "5" or expression[e] == "6" or expression[e] == "7" or expression[e] == "8" or expression[e] == "9" :
                a=a*10+int(expression[e])
                e+=1
            while  e+1 < len(expression) and expression[e+1]!="\0":
                b=b*10+int(expression[e+1])
                e+=1
            for i in range(1,len(expression)):
                
                if expression[i] == '+':
                    math_p.plus(a,b)
                elif expression[i] == '-':
                    math_p.moins(a,b)
                elif expression[i] == '/':
                    math_p.divi(a,b)
                elif expression[i] == 'r':
                    math_p.racine(a,b)
                elif expression[i] == '*':
                    math_p.multi(a,b)
                elif expression[i] == '^':
                    math_p.puiss(a,b)
                
      
            
            
            
            
            
            
            
            
            
                