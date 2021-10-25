# Statically scrape required items from all quests from https://oldschool.runescape.wiki/w/Quests/List
# Stephen Haugland
# 10/23/2021


import requests
import re
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd



def main():
    
    # Main dictionary to hold all required quest items
    allrequireditems = {
        
    }

    p = re.compile('^.*?(?= \()') #Regex key to pull out item
    page = requests.get('https://oldschool.runescape.wiki/w/Quests/List') # Get the main HTML page through request
    soup = BeautifulSoup(page.content, 'html.parser') # Parsing content using beautifulsoup
    links = soup.select("#mw-content-text > div > table:nth-child(6) tbody tr td:nth-of-type(2) a") # retrieve individual quest page links
    #mw-content-text > div > table:nth-child(6)
    #mw-content-text > div > table:nth-child(11)



    for quest in links:
        relativeURL = quest.get('href')
       
        print(relativeURL) #display innerText of each quest name
        questURL = "https://oldschool.runescape.wiki" + relativeURL

        questPage = requests.get(questURL)
       
        soup = BeautifulSoup(questPage.content, 'html.parser')  # Parsing content using beautifulsoup
        
        requiredItems = soup.select("#mw-content-text > div > table.questdetails.plainlinks > tbody > tr:nth-child(6) > td > div > ul > li")
       
        # print("RequiredItems: ")
        # print(requiredItems)

        
        for x in range(len(requiredItems)):
            itemData = requiredItems[x]
            string = itemData.get_text()
            soup2 = BeautifulSoup(str(itemData), 'html.parser')  # Parsing content using beautifulsoup
            item = soup2.find("a")['title']
            # If multiple of the same item are required
            string = string.split(' ',1)[0]
            if (containsNumber(string)):
                quantity = string
                if ("," in quantity):
                    quantity = re.sub(",","",string)
                print("Quantity: " + quantity)
                print("Item: " + item)              
            # If only one of the item is required
            else:
                quantity = 1
                print("Quantity: 1")
                print("Item: " + item)
            addiqpair(item,int(quantity),allrequireditems)
           
        print("\n")

    # print("Finished\n")

    print(allrequireditems)


    #EXCEL OUTPUT
    # df = pd.DataFrame(data=allrequireditems, index=[0])
    # df = (df.T)
    # print (df)
    # df.to_excel('AllRequiredQuestItems.xlsx')


def addiqpair(i,q, dictionary):
    # item is already in dictionary
    if (dictionary.get(i)):
        currentquantity = int(dictionary[i])
        q += currentquantity

    # item in NOT already in dictionary
    dictionary.update({i:q})

def containsNumber(value):
    for character in value:
        if character.isdigit():
            return True
    return False
    
if __name__ == "__main__":
    main()



# def setup():
#     websiteURL ="https://oldschool.runescape.wiki/w/Quests/List"
#     option = webdriver.ChromeOptions()
#     option.add_argument('--headless')
#     # option.add_argument('--no-sandbox')
#     # option.add_argument('--disable-dev-sh-usage')
#     driver = webdriver.Chrome("S:/Documents/Dev/chromedriver.exe",options=option)
#     driver.get(websiteURL)


    # session = HTMLSession()
    # response = session.get('https://oldschool.runescape.wiki/w/Quests/List')
    
    # # driver = setup()
    # soup = BeautifulSoup(response.content, 'html.parser') # Parsing content using beautiful soup