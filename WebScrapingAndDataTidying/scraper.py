from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

def buildBeers(htmlList):
    beers = []
    for html in htmlList:
        htmlOpen = urlopen(html)
        htmlSoup = BeautifulSoup(htmlOpen, 'html.parser')
        htmlRows = htmlSoup.findAll("tr")
        #searches each table and assigns each variable to the column name
        for tableRow in htmlRows:
            cells = tableRow.findAll("td")
            entry = {
                "Number":cells[0].text,
                #stripping off /n tags for the Beer name.
                "Beer":cells[1].text.strip(),
                "Brewery":cells[2].text,
                #the cell here is stripped in a particular way to facilitate a clean dataset.
                #This is where the scraper will break if it breaks in the future!
                "Location":cells[3].text.replace('\t','').replace('             ',' ').strip(),
                "Style":cells[4].text,
                "ABV":cells[5].text,
                "IBU":cells[6].text}
            #Does not add headers to the list.
            if entry["Number"] == "#": 
                continue
            else:
                beers.append(entry)
        
    for row in beers:
        print(beers)
    #saves the dataframe to a csv, total of 109 data entries.    
    df = pd.DataFrame(beers)
    df.to_csv("beersRAW.csv", header ={"Number", "Beer", "Brewery","Location", "Style", "ABV", "IBU"})

def main():
    htmlList = []
    #Builds a list of pages to visit. There are eleven pages of ten entries.
    for i in range(1,12):
        htmlList.append("http://www.ipabeer.com/database?page="+str(i))
    #builds the beers list
    buildBeers(htmlList)

if __name__ == "__main__": main()

