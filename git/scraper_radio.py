import requests
from bs4 import BeautifulSoup
import pymysql.cursors  


# Подключаемся к базе данных
def getConnection():
    connection = pymysql.connect(
        host='localhost', 
        user='root', 
        password='', 
        db='djangoradio', 
        charset='utf8mb4', 
        cursorclass=pymysql.cursors.DictCursor)
    print ("Connect to MySQL successful!")
    return connection 

# Получаем html из ссылки
def get_html(url):
    response = requests.get(url)
    return response.text


#Собираем все страницы, на которых есть радиостанции, используя пагинацию
def get_pagination_pages(base_url):
    allpages = [base_url + '?page=1']
    i = 1
    while True:
        i+=1
        mainurl = base_url + '?page=' + str(i)
        response = requests.get(mainurl, allow_redirects=False)
        if response.status_code !=200:
            break
        allpages.append(mainurl)
    return allpages


# Собираем ссылки радиостанций с одной страницы
def get_radiostations_links_from_page(html):
    soup = BeautifulSoup(html, 'lxml')
    alllinks = soup.find_all('a', class_='imagetip')
    links = []
    for a in alllinks:
        c = a.get('href')
        link = 'http://top-radio.ru/' + c
        links.append(link)
    return links


#Собираем ссылки всех радиостанций со всех страниц
def get_all_radiostation_links(url):    
    pages = get_pagination_pages(url)   # 12 страниц сайта, список 
    links = []
    for i in pages:
        radiostations_links = get_radiostations_links_from_page(get_html(i)) # i - одна ссылка сайта где много радистанций
        links.extend(radiostations_links)
    print("Всего ссылок на радиостанции: ", len(links))    
    return links
 

# Собираем теги с одной страницы
def get_name(soup):
    return soup.h1.text

def get_bitrate(soup):    
    bitrate = soup.find_all('span', class_='text')       
    return bitrate[0].text.split(' ')[1]

def get_genre(soup):
    genre = soup.find_all('span', class_='text')  
    return genre[1].text.split(':')[1]

def get_country(soup):
    country = soup.find_all('span', class_='text')  
    return country[2].text.split(':')[1]

def get_city(soup):
    city = soup.find_all('span', class_='text')  
    return city[3].text.split(':')[1]

def get_frequency(soup):
    frequency = soup.find_all('span', class_='text')  
    return frequency[4].text.split(':')[1]
   
def get_adress(soup):
    adress = soup.find_all('span', class_='text')  
    return adress[5].text.split(':')[1]

def get_telephone(soup):
    telephone = soup.find_all('span', class_='text')  
    return telephone[6].text.split(':')[1]

def get_email(soup):
    email = soup.find_all('span', class_='text')  
    return email[7].text.split(':')[1]

def get_date(soup):
    date = soup.find_all('span', class_='text')  
    return date[8].text.split(':')[1]

def get_site(soup):
    site = soup.find_all('span', class_='text')  
    return site[9].text.split(':')[1]
 

def start():
    
    base_url = 'http://top-radio.ru/online'
    connection = getConnection()
    links = get_all_radiostation_links(base_url)
    number_of_links = len(links)
    
    for link in links:  

        html = get_html(link)
        soup = BeautifulSoup(html, 'lxml')
        name = get_name(soup)
        bitrate = get_bitrate(soup)
        genre = get_genre(soup)
        country = get_country(soup)
        city = get_city(soup)
        frequency = get_frequency(soup)
        adress = get_adress(soup)
        telephone = get_telephone(soup)
        email = get_email(soup)
        date = get_date(soup)
        site = get_site(soup)
        try:
            cursor = connection.cursor()    
            sql = "INSERT INTO spider_post(name, bitrate, genre, country, city, frequency, adress, telephone, email, date, site) \
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
            rowCount = cursor.execute(sql, (name, bitrate, genre, country, city, frequency, adress, telephone, email, date, site))    
            connection.commit() 
        finally:        
            print(name, "- записано")              
    connection.close() 
    print("Работа завершена. \nВ базу данных добавлено", number_of_links, "записей.")


if __name__ == '__main__':
    start()