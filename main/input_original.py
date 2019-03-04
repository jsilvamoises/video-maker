# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 11:45:08 2019

checkout -b user-input

git remote add origin https://github.com/jsilvamoises/video-maker
git push origin user-input
@author: Usuario
"""
prefixes = {"0":"Who is","1":"What is","2":"The history of"}

selectedSentence =  ""
sizeSeparator = 40
query =""
def menu():
    print("_"*sizeSeparator)
    query = input("Informe o termo a ser pesquisado: ")   
    print("_"*sizeSeparator)
    print("Selecione a sentença desejada")
    print("_"*sizeSeparator)
    for p in prefixes:
        print("{} - {}".format(p,prefixes[p]))
    
    selectedSentence = input("OP: ")
    if(selectedSentence.isnumeric()):
        selectedSentence = prefixes[selectedSentence]
        query = selectedSentence+" "+query
        print("Opção escolhida.: ",query)
    
menu()
    
    

