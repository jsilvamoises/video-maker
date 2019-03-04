# coding: utf8
from selenium import webdriver

from selenium.webdriver.common import by
trends = {}
# =====================================================
def findTrends():
    print(">> Initializing Chrome in hide mode")
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    browser = webdriver.Chrome(options=options)
    browser.get("https://trends.google.com/trends/trendingsearches/daily?geo=BR")
    print(">> Sucessfull Chrome open")
    selectTrends(browser)
# =====================================================
def selectTrends(browser):    
    #list = browser.find_elements_by_xpath("//md-list[@class='md-list-block']")
    temas = browser.find_elements_by_class_name("feed-item")    
    
    for i in range(len(temas)):
        l = temas[i]
        title = l.find_element_by_class_name("title").text
        #index = l.find_element_by_class_name("index").text
        #detail = l.find_element_by_tag_name("a").get_property("title")
        trends[int(i)] = title
    print(">> Closing Chrome")    
    browser.quit() 
    menu(trends) 
          
    
# ===================================================== 
def menu(trends):   
    print("="*50)
    print("Escolha o tema para o qual deseja criar o vídeo.")
    print("="*50)
    for t in trends:
        print("%2.0d - %s "%(t,trends[t]))    
        
    print("="*50)  
    op = input("OP Número.: ")
    print("="*50)
    if op.isnumeric() and int(op) < len(trends):
        tema = trends[int(op)]
        processarOpcaoEscolhida(tema)
        #processarOpcaoEscolhida(trends[int(op)])
    elif op == "99":
        print("Até Logo")
        exit(0)
    else:
        print("Valor inválido")
# ===================================================== 
def processarOpcaoEscolhida(text):  
    print("O Assunto escolhido foi %s"%text)
    print("="*50) 
    pass



findTrends()   