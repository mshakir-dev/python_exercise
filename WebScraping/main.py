from bs4 import BeautifulSoup
from urllib import request
from csv import writer

source = request.urlopen('http://coreyms.com')
print("\n\n--------------------------------------------------------\n\n")

print("Type: ", type(source))
print("Status: ", source.code)
print("Length in Bytes: ", source.length)

print("\n\n--------------------------------------------------------\n\n")

soup = BeautifulSoup(source, 'html.parser')

# Find All the Paragraph in the Website

for paragraph in soup.find_all('p'):
    print(paragraph.text)
print("\n\n--------------------------------------------------------\n\n")

# find All Url and Their href
for url_Link in soup.find_all('a'):
    print(url_Link.get('href'))

print("\n\n--------------------------------------------------------\n\n")

# Pandas Module is good write the table text

csv_file = open('posts.csv', 'w')
csv_writer = writer(csv_file)
csv_writer.writerow(['Main-Heading', 'Link Summary', 'Video URL'])

all_element = soup.find_all('article')
for article in all_element:
    headline = article.h2.a.text
    print(headline)

    summary = article.find('div', class_='entry-content').p.text
    print(summary)

    try:
        vid_src = article.find('iframe', class_='youtube-player')['src']

        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]

        yt_link = f'https://youtube.com/watch?v={vid_id}'
    except Exception as e:
        yt_link = None

    print(yt_link)

    print()

    csv_writer.writerow([headline, summary, yt_link])

csv_file.close()

# Youtube Tutorial from Youtube