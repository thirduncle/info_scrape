import requests
from bs4 import BeautifulSoup

# TODO: Add description as a column in DB.
#       Get direct link to radio show (instead of show's page).

base_url = 'https://info-war.gr/infowar-radio/'
bs = BeautifulSoup(requests.get(base_url).text, 'html.parser')

shows_list = []

def get_all_pages(first_page):
    url_list = []
    r = requests.get(first_page)
    bs = BeautifulSoup(r.text, 'html.parser')
    page_url = 'https://info-war.gr/infowar-radio/page/'
    url_list.append(base_url)
    for li in bs.find('ul', {'class': 'page-numbers'}).find_all('li'):
        try:
            chk_str = " ".join(li.a.attrs["class"])
            if chk_str == "next page-numbers":
                total_pages = li.find_previous_sibling().get_text()
            else:
                pass
        except AttributeError:
            pass
    for i in range(2, int(total_pages) + 1):
        page_url = page_url + str(i) + '/'
        url_list.append(page_url)
        page_url = 'https://info-war.gr/infowar-radio/page/'
    return url_list

def get_show_info(url):
    for div in bs.find('div',{'class': 'cb-grid-x cb-grid-4 clearfix'}).find_all('div', {'class' : 'cb-article-meta'}):
        shows_dict = {"date": "", "title": "", "link": ""}
        shows_dict["date"] = div.time['datetime']
        shows_dict["title"] = div.a.get_text()
        shows_dict["link"] = div.a["href"]
        shows_list.append(shows_dict)
    return shows_list

#print(get_all_pages(base_url))

create_table()

for page in get_all_pages(base_url):
    get_show_info(page)

#for item in shows_list:
    #print(item)

for item in shows_list:
    add_entry(item['date'], item['title'], item['link'])

#print(get_show_info(base_url))


menu = """
Choose your option:

1. Get current year's shows based on month.
2. Get past years' shows based on month.
3. View the full collection until now.
4. Exit

Your selection: """

welcome = "Welcome to InfoWar podcasts collection"

print()
print(welcome)


#for page in get_all_pages(base_url):
 #   get_show_info(page)



"""


while (user_input := input(menu)) != "4":
    if user_input == "1":
        pass
    elif user_input == "2":
        pass
    elif user_input == "3":
        pass
    else:
        print("Invalid option, please try again!")




"""