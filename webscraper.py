import requests
from bs4 import BeautifulSoup
# Make a request
page = requests.get("Paste a Domain here")
soup = BeautifulSoup(page.content, 'html.parser')

# Create all_h1_tags as empty list
all_h1_tags = []

# Set all_h1_tags to all h1 tags of the soup
for element in soup.select('h1'):
    all_h1_tags.append(element.text)

# Create seventh_p_text and set it to 7th p element text of the page
seventh_p_text = soup.select('p')[6].text

print(all_h1_tags, seventh_p_text)

# Gibt dir alle h1 Elemente deren Text aus und auch das siebte p element
# return all h1 elemnts and there text and the sevent p element 
