import requests
from bs4 import BeautifulSoup
from random import randrange
response = requests.get('https://bel.football/all-news').text
#print(response)

soup = BeautifulSoup(response, 'html.parser').find_all(attrs={'class': 'node widget-element widget css73'})

#with open('soup.html', 'wb') as file:
    #file.write(soup)
print(len(soup))

for elem in soup:
     if elem is not None:
        elem_1 = elem.find_all('a')
        for elem_2 in elem_1:

            #print(elem_2['href'])
            news = requests.get(f'https://bel.football{elem_2["href"]}').text
            soup_inner = BeautifulSoup(news, 'html.parser').find_all(attrs={'class': 'container_img'})
            for elem_1_0 in soup_inner:
                link = elem_1_0.find('img')

                img = requests.get(f'https://bel.football{link["src"]}').content

                with open(f'temp/image{randrange(0, 34906573209401248)}.jpeg', 'wb') as image:
                    image.write(img)



for i in range(2, 20):
    response = requests.get(f'https://bel.football/all-news?page={i}').text
    # print(response)

    soup = BeautifulSoup(response, 'html.parser').find_all(attrs={'class': 'node widget-element widget css73'})

    # with open('soup.html', 'wb') as file:
    # file.write(soup)
    print(len(soup))

    for elem in soup:
        if elem is not None:
            elem_1 = elem.find_all('a')
            for elem_2 in elem_1:

                # print(elem_2['href'])
                news = requests.get(f'https://bel.football{elem_2["href"]}').text
                soup_inner = BeautifulSoup(news, 'html.parser').find_all(attrs={'class': 'container_img'})
                for elem_1_0 in soup_inner:
                    link = elem_1_0.find('img')

                    img = requests.get(f'https://bel.football{link["src"]}').content

                    with open(f'temp/image{randrange(0, 34906573209401248)}.jpeg', 'wb') as image:
                        image.write(img)
