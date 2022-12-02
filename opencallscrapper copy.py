#### OPENCALLS SCRAPPER BY FRAN
####

## Fazer um aumento da pesquisa para a proxima pagina caso os resultados sejam poucos
## Fazer um programa que fica a correr durante varias pesquisas e depois fecha
## Criar um sistema de flags que despertam multiplas pesquisas (ex: em varios paises, varios anos)



from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

## See past researches and writes a new one



def printPast():
    past = open('pastresearch.txt','r')
    print("PESQUISAS JA FEITAS NO PASSADO")
    for line in past:
        print(line[:-1])
    past.close
    
    ##searchfor = str(input("What do you want to search for :"))
def saveSearch(searchfor):
    present = open('pastresearch.txt','a')
    present.write("%s\n" % searchfor)
    present.close
    return (searchfor)

## Start Browser
def goOnline(searchfor):
    print("Starting Browser Chrome")
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    
    frst_click = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[3]/span/div/div/div/div[3]/div[1]/button[1]")
    frst_click.click()
    
    search_box = driver.find_element(By.NAME,"q")
    search_box.send_keys(searchfor)
    search_box.send_keys(Keys.RETURN)
    
    # wait for the page to load
    
    time.sleep(5)
    
    # get all the links
    ## meter aqui um while alive para ir correndo em varias paginas
    keep_searching = True
    while keep_searching:
        links = driver.find_elements(By.TAG_NAME,"a")

        # write found links in newres
        print("Getting new Links")
        newres = open('newresults.txt','w')

        for link in links:
            if link.get_attribute("href") != None:
                newres.write("%s\n" % link.get_attribute("href"))
        newres.close

        print("Getting new Links Done")
        # prepare found links and old ones in lists
        print("Preparing Lists for Comparing")

        oldbook = open('seenresults.txt','r')
        newbook = open('newresults.txt','r')

        old_links = []
        new_links = [] 

        for line in oldbook:
            x = line[:-1]
            old_links.append(x)
            #print("I APPENDED TO OLD_LINKS ")
        for line in newbook:
            x = line[:-1]
            new_links.append(x)
            #print("I APPENDED TO New_LINKS ")

        oldbook.close
        newbook.close

        print("Preparing Lists for Comparing DOne")

        # clean google results from new_list
        print("Cleaning GOOGLE Results (if a not google adress is here please contact FranceIt Department")
        googlelinks = open("googlelinks.txt",'w')
        rm_google = []
        for a in new_links:
            if 'google' in a:
                googlelinks.write(a)
                rm_google.append(a)
        for rm in rm_google:
            if rm in new_links:
                new_links.remove(rm)

        googlelinks.close
        print("Cleaning GOOGLE Results DONE")

        # compare twe two lists

        old_links.sort()
        new_links.sort()

        rmlinks = []

        for c in new_links:
            for a in old_links:
                if c == a:
                    rmlinks.append(c)

        for rm in rmlinks:
            if rm in new_links:
                new_links.remove(rm)


        # append new results to oldbook
        print("Appending results to seenresults.txt")

        oldbookappend = open("seenresults.txt",'a')

        for nl in new_links:
            oldbookappend.write("%s\n" % nl)

        oldbookappend.close
        print("Appending results Done")


        # print new links 
        print("Printing New Links\n")

        for d in new_links:
        	print(d)

        whttodo = str(input("\n\nPres 'y' or yes if you want to search the next page\nIgnore if you wish to make a new search or exit the application"))
        if whttodo == 'y' or whttodo == "yes":
            nextpage = driver.find_element(By.LINK_TEXT,"Next")
            nextpage.click()
        else :
            keep_searching = False
    print("Printing New Links DONE")

    # close the browser
    driver.close()

itsRunning = True
print("#### OPENCALLS SCRAPPER BY FRAN ####")

while itsRunning:
    searchfor = str(input("What do you want to search for :"))
    saveSearch(searchfor)
    goOnline(searchfor)
    keepGoing = str(input("Press 'q' or exit if you wish to terminate\nPress 'pp' or printpast if you want to see already done and saved searches\nelse just press enter\n"))
    if keepGoing == "pp" or keepGoing == 'printpast':
        printPast()
    if keepGoing == "exit" or keepGoing == 'q':
        itsRunning = False