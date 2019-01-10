from projet import *

i=1
while True:

    exp=input("[{}]>>> ".format(i))
    i+=1
    if exp == "exit":
        break
    elif exp == "":
        continue
    if exp[0] == "-" or exp[0] == "+":
        exp_p="0"+exp
    else:
        exp_p="0+"+exp
    if parenthesage(exp):
        if "=" not in exp_p :
            if "showvar" in exp_p:
                while "(" in exp_p:
                    exp_p = calcul(exp_p)
                projet.calculatrice(exp_p)
            elif "clear" in exp_p:
                while "(" in exp_p:
                    exp_p = calcul(exp_p)
                projet.calculatrice(exp_p)
            else:
                while "(" in exp_p:
                    exp_p = calcul(exp_p)
                print(exp," = ",projet.calculatrice(exp_p))
            
        elif "=" in exp_p :
            while "(" in exp_p:
                exp_p = calcul(exp_p)
            projet.calculatrice(exp_p)
        
    else: 
        print("Expression invalide !(verifiez les parenthése)")
        
    





























