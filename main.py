# Statically scrape required items from all quests from https://oldschool.runescape.wiki/w/Quests/List
# Stephen Haugland
# 10/23/2021


import requests
from bs4 import BeautifulSoup
from selenium import webdriver



def main():
    page = requests.get('https://oldschool.runescape.wiki/w/Quests/List') # Get the main HTML page through request
    soup = BeautifulSoup(page.content, 'html.parser') # Parsing content using beautifulsoup

  
    links = soup.select("#mw-content-text > div > table:nth-child(6) tbody tr td:nth-of-type(2) a") # retrieve individual quest page links
    for quest in links:
        relativeURL = quest.get('href')
        print(relativeURL) #display innerText of each quest name
        questURL = "https://oldschool.runescape.wiki" + relativeURL
        questPage = requests.get(questURL)
        soup = BeautifulSoup(questPage.content, 'html.parser')  # Parsing content using beautifulsoup

        # requiredItems = soup.select("#mw-content-text > div > table.questdetails.plainlinks > tbody > tr:nth-child(6) > td > div > ul > li > a:nth-of-type(1)")
        # for items in requiredItems:
        #     print(items.get('title'))
        # print(soup.select("#mw-content-text > div > table.questdetails.plainlinks > tbody > tr:nth-child(6) > td > div > ul > li > a:nth-of-type(1)::before"))
        # if (text != "\0"):
        #     print(text)
        
        requiredItems = soup.select("#mw-content-text > div > table.questdetails.plainlinks > tbody > tr:nth-child(6) > td > div > ul > li")
        # print(requiredItems)

        
        for x in range(len(requiredItems)):
            print(requiredItems)
            # item = "NA"
            itemData = requiredItems[x]
            print(itemData[0])
            if (itemData[0].isdigit()):
                quantity = itemData[0]
                item = itemData[1].get('title')
            else:
                quantity += 1
                item = itemData[0].get('title')
            print(quantity + " x " + item)
        # print(requiredItems)
        print("\n")
    # print(links)

    print("Finished")








def addToItemList(item):
    print("count")
    
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