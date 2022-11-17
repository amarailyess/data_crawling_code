from bs4 import BeautifulSoup 
import requests
import pandas as pd

class BrazilCarsCrawling:
    baseUrl = "https://www.cars.com"
    data = []
    def start_request(self,url):
        source = requests.get(url)
        print(source)
        soup = BeautifulSoup(source.text, features='lxml')
        return soup


    def getItems(self,url):
        soup = self.start_request(url=url)
        items = soup.findAll("a", {"class": "vehicle-card-link"})
        next_url = soup.find("a", {"id": "next_paginate"})
        return next_url,items

    def getDataItem(self, soup):
            label = soup.find("h1", {"class":"listing-title"}).text
            price = soup.find("span", {"class": "primary-price"}).text
            features = soup.find("dl", {"class": "fancy-description-list"})
            ext_color = features.findChild("dt",string =  "Exterior color").find_next_sibling("dd").text
            int_color = features.findChild("dt",string =  "Interior color").find_next_sibling("dd").text
            fuel_type = features.findChild("dt",string =  "Fuel type").find_next_sibling("dd").text
            transmission = features.findChild("dt",string =  "Transmission").find_next_sibling("dd").text
            mileage = features.findChild("dt",string =  "Mileage").find_next_sibling("dd").text
            d = dict({"label":label, "price" : price, "ext_color" : ext_color, "int_color":int_color, "fuel_type" : fuel_type, "transmission" : transmission, "mileage": mileage})
            return d

    def getData(self, url):
        next_url,items = self.getItems(url)
        print (url,'...')
        for item in items:
            item_url = self.baseUrl + item['href']
            print("\t item:", item['href'])
            soup  = self.start_request(item_url)
            d = self.getDataItem(soup=soup)
            self.data.append(d)
                   
        if next_url:
            next_url = self.baseUrl + next_url['href']
            self.getData(next_url)
        else:
            df = pd.DataFrame(data=self.data)
            df.to_csv("data.csv")
            print("finish.")


if __name__ == "__main__":
    bc = BrazilCarsCrawling()
    bc.getData("https://www.cars.com/shopping/brazil-in/?page=41")