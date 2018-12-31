"""
    Created on wed Nov  14 23:00:00 2018
    @authors:-saad el harchi
             -aziagba romuald
            
    this module is made to simulate a calculator.
"""
print
class projet:
    pi=3.1415926535
    var={}
    def variable(expression):
        cntr = 2
        value = ""
        var_name = ""
        while expression[cntr] != "=" :
            var_name += expression[cntr]
            cntr+=1
        cntr+=1
        for i in range(cntr,len(expression)):
            value += expression[i]    
        projet.var[var_name] = float(value)
        
    def pere(x,y,i,t):
        if x[i] == "pi" or x[i] == "Pi" or x[i] == "pI" or x[i] == "PI":
            fils_gauche=projet.pi
        elif x[i] in projet.var.keys():
            fils_gauche=projet.var[x[i]]
        else:
            try:
                fils_gauche=float(x[i])  
            except:
                fils_gauche=0.0
        pere=y[i+1]
        t.extend([fils_gauche,pere])

    def calculatrice(expression):
        #try:
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
                while e <len(expression) and expression[e] !='+' and expression[e] !='_' and expression[e] !='*' and expression[e] !='/':
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
            if '*' not in stock and '/' not in stock:
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
                        if stock[i+3]!='*' and stock[i+3]!='/':
                            i+=4
                        else:
                            i+=2
                    elif stock[i+1]=='/':
                        b=stock[i]/stock[i+2]
                        stockp.append(b)
                        if stock[i+3]!='*' and stock[i+3]!='/':
                            i+=4
                        else:
                            i+=2
                    else:
                        stockp.append(stock[i])
                        i+=2
                #indice=0
                
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
            
        #except:
            #print("Expression non valide !(math error)")

def parenthesage(expression):
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
    for i in range(len(expression)):
        if expression[i] == ")" :
            indice_f = i
            break
    for j in range(indice_f,0,-1):
        if expression[j] == "(" : 
            indice_o=j
            break
    exp_part=""
    for i in range(indice_o+1,indice_f):
        exp_part+=expression[i]
    
    """if exp_part[0] == "-" or exp_part[0] == "-":
        exp_part = "0"+exp_part
    """
    l=len(expression)
    """if projet.calculatrice(exp_part) < 0:
        return expression[0:indice_o-1]+str(projet.calculatrice(exp_part))+expression[indice_f+1:l]
    else:"""
    return expression[0:indice_o]+str(projet.calculatrice(exp_part))+expression[indice_f+1:l]