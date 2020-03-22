
# python scraper to retrieve all my da-tah
import csv
# import pymongo
import requests
from bs4 import BeautifulSoup as bsoup
from bs4 import Comment

def open_file(filename):
    print ('open file')

def has_met_db():
    return False #TODO fix

def save_image(url,id):
    response = requests.post(url)  
    soup = bsoup(response.content, 'html.parser')
    links = soup.findAll('a')
    img_tag = links[-1] if len(links)>1 else links[0]
    #arr of each line in script
    img_src = img_tag['href']
    img_response = requests.post('https://www.wga.hu/' + img_src)
    print (img_src)
    temp_file = open('img_lib/img_'+str(id),'wb')
    temp_file.write(img_response.content)
    temp_file.close()
    return True

def init_db():
  print('todo')
  # client = pymongo.MongoClient()
  # met_db = client.met_db
  # met_collection = met_db.met_collection
  # open_file("wga.csv")


  # client = pymongo.MongoClient()
  # met_db = client.met_db
  # met_collection = met_db.met_collection
  # if not has_met_db():
  #   all_met_objs = get_objectlist()
  #   for oid in all_met_objs['objectIDs']:
  #     # orecord =get_object(oid)
  #     if oid <= 17:
  #       continue
  #     else:
  #       print(oid)
  #     met_collection.insert_one(get_object(oid))



if __name__ == "__main__":

    with open('wga.csv', newline='', encoding='latin-1') as f:
        reader = csv.reader(f)
        first = True
        counter = 0 
        for row in reader:
            if(first):
                col_names = row
                first = False
            else:
                save_image(row[6],counter)
            counter = counter + 1
