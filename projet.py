"""
    
    @authors:-saad el harchi
             -aziagba romuald
            
    this module consists of many functions that allows you to read
    a string and evaluate it:-mathematical expressions
                             -setting variables
"""
from math_p import *

a=math_p()

class projet:
    pi=3.1415926535
    e=2.71828182846
    var={}
    def varval(name):
        """
        takes a string as an argument and returns the value of the variable 
        with the given name
        """
        return projet.var[name]
    def variable(expression):
        """
        takes a string as an argument that containes a variable declarition or 
        a change of the value of an already declared variable 
        ( variables are stocked in a dictionary )
        
        """
        cntr = 2
        value = ""
        var_name = ""
        while expression[cntr] != "=" :
            var_name += expression[cntr]
            cntr+=1
        cntr+=1
        for i in range(cntr,len(expression)):
            value += expression[i]    
        projet.var[var_name] = float(projet.calculatrice(value))
        
    def pere(x,y,i,t):
        """
        this function separetes the expression to termes and operators if
        the expression is a mathematical one,else if the expression 
        contains a key word ( clear , showvar ) then the program executes 
        the associated function to the key word
        """
        if x[i] == "clear":
            print(projet.var)
            projet.var={}
            print(projet.var)
            fils_gauche = 0.0
        elif x[i] == "showvar":
            print(projet.var)
            fils_gauche = 0.0
        elif x[i] == "pi" or x[i] == "Pi" or x[i] == "pI" or x[i] == "PI":
            fils_gauche=projet.pi
        elif x[i] == "e":
            fils_gauche=projet.e
        elif "e" in x[i]:
            fils_gauche=a.exp(float(x[i][1:len(x[i]):1]))
        elif x[i] in projet.var.keys():
            fils_gauche=projet.var[x[i]]
        elif "cos" in x[i]:
            fils_gauche=a.cos(float(x[i][3:len(x[i]):1])/180*projet.pi)
        elif "sin" in x[i]:
            fils_gauche=a.sin(float(x[i][3:len(x[i]):1])*projet.pi)
        elif "tan" in x[i]:
            
            if "cotan" in x[i]:
                fils_gauche=a.cotan(float(x[i][5:len(x[i]):1]))
            else:
                fils_gauche=a.tan(float(x[i][3:len(x[i]):1]))
        elif "ln" in x[i]:
            fils_gauche=a.ln(float(x[i][2:len(x[i]):1]))
        else:
            try:
                fils_gauche=float(x[i])  
            except:
                fils_gauche=0.0
        pere=y[i+1]
        t.extend([fils_gauche,pere])

    def calculatrice(expression):
            """
            this function takes one string argument that doesn't contain brackets
            and mathematicaly evaluates it then returns its value
            """
            if "=" in expression:
                projet.variable(expression)
                return
            st=list()
            opp=" "
            stock=list()
            e=0
            for i in range(0,len(expression)):
                st.append("")
            for i in range(0,len(expression)):
                while e <len(expression) and expression[e] !='+' and expression[e] !='_' and expression[e] !='*' and expression[e] !='/' and expression[e] !='^':
                    st[i]+=expression[e]
                    e+=1
                if e < len(expression) :
                    opp+=expression[e]
                e+=1
            opp+="+ "
            while st[len(st)-1] == '':
                st.pop()
            for i in range(0,len(st)):
                projet.pere(st,opp,i,stock)
            stock.pop()
            a=stock[0]
            stockp=list()
            stock.extend(['+',0])
            if '*' not in stock and '/' not in stock and '^' not in stock:
                for i in range(1,len(stock),2):
                    if stock[i] == '+':
                        a+=stock[i+1]
                    elif stock[i] == '_':
                        a-=stock[i+1]
            else:
                i=0
                while i+1 <len(stock):
                    if stock[i+1]=='*':
                        b=stock[i]*stock[i+2]
                        stockp.append(b)
                        if stock[i+3]!='*' and stock[i+3]!='/' and stock[i+3]!='^':
                            i+=4
                        else:
                            i+=2
                    elif stock[i+1]=='/':
                        b=stock[i]/stock[i+2]
                        stockp.append(b)
                        if stock[i+3]!='*' and stock[i+3]!='/' and stock[i+3]!='^':
                            i+=4
                        else:
                            i+=2
                    elif stock[i+1]=='^':
                        b=stock[i]**stock[i+2]
                        stockp.append(b)
                        if stock[i+3]!='*' and stock[i+3]!='/' and stock[i+3]!='^':
                            i+=4
                        else:
                            i+=2
                    else:
                        stockp.append(stock[i])
                        i+=2
                
                
                oppl=list()
                for i in range(0,len(opp)):
                        oppl.append(opp[i])
                while '*' in oppl:
                    oppl.remove('*')
                while '/' in oppl:
                    oppl.remove('/')
                while ' ' in oppl:
                    oppl.remove(' ')
                oppl.pop()
                a=stockp[0]
                for i in range(0,len(oppl)):
                    if oppl[i]=='+':
                        a+=stockp[i+1]
                    if oppl[i]=='_':
                        a-=stockp[i+1]
            return a
            
        

def parenthesage(expression):
    """
    a boolean function that returns True if the given expression respects the
    correct bracketing system,or else returns False
    """
    cntr_parenthese=0
    for i in range(len(expression)):
        if expression[i] == "(" :
            cntr_parenthese+=1
        elif expression[i] == ")" and cntr_parenthese > 0:
            cntr_parenthese-=1
        elif expression[i] == ")" and cntr_parenthese == 0:
            return False
        else:
            continue
    if cntr_parenthese != 0 :
        return False
    else:
        return True



def calcul(expression):
    """
    this function decomposes the original expression in partial expressions
    in order to evaluate what is between brackets in order to give them 
    the priority
    """
    for i in range(len(expression)):
        if expression[i] == ")" :
            indice_f = i
            break
    for j in range(indice_f,-1,-1):
        if expression[j] == "(" : 
            indice_o=j
            break
    exp_part=""
    for i in range(indice_o+1,indice_f):
        exp_part+=expression[i]
    
    l=len(expression)
    
    return expression[0:indice_o]+str(projet.calculatrice(exp_part))+expression[indice_f+1:l]