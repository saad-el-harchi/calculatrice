from projet import *

  
while True:

    exp=input(">>> ")
    if exp == "exit":
        break
    elif exp == "":
        continue
    if exp[0] == "-" or exp[0] == "+":
        exp_p="0"+exp
    else:
        exp_p="0+"+exp
    if parenthesage(exp):
        while "(" in exp_p:
            exp_p = calcul(exp_p)
        print(exp," = ",projet.calculatrice(exp_p))
       
    else: 
        print("Expression invalide !(verifiez les parenthése)")
        
    





























