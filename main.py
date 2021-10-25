# Statically scrape required items from all quests from https://oldschool.runescape.wiki/w/Quests/List
# Stephen Haugland
# 10/23/2021


import requests
import re
from bs4 import BeautifulSoup
from selenium import webdriver



def main():
    
    allrequireditems = {
        "testing": "123"
    }


    p = re.compile('^.*?(?= \()') #Regex key to pull out item
    page = requests.get('https://oldschool.runescape.wiki/w/Quests/List') # Get the main HTML page through request
    soup = BeautifulSoup(page.content, 'html.parser') # Parsing content using beautifulsoup
    links = soup.select("#mw-content-text > div > table:nth-child(6) tbody tr td:nth-of-type(2) a") # retrieve individual quest page links
    
    for quest in links:
        relativeURL = quest.get('href')
       
        print(relativeURL) #display innerText of each quest name
        questURL = "https://oldschool.runescape.wiki" + relativeURL

        ## CHANGE BACK TO LINE ABOVE ONCE TESTING IS COMPLETE
        # questURL = "https://oldschool.runescape.wiki" + "/w/Doric%27s_Quest"

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
    # print(links)

    print("Finished\n")

    print(allrequireditems)


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





# def addToItemList(item, quantity):
#     freq = {}
#     for item in myList:
#         if (item in freq):
#             freq[item] += quantity
#         else:
#             freq[item] = 1
    
if __name__ == "__main__":
    main()



    # links = soup.select("table tbody tr rd.data-sort-value")
    # first10 = links[:10] #keep first 10 quest names
    # for quest in first10:
    #     print(quest.text) #display innerText of each quest name

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