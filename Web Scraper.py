import requests
from bs4 import BeautifulSoup
import csv

# Send an HTTP request to the website
url = "http://quotes.toscrape.com/"
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find the quotes on the page
quotes = soup.find_all('div', class_='Quote')

# Create a list to store the extracted data
data = []

# Extract the quote, author, and tags for each quote
for quote in quotes:
    quote_text = quote.find('span', class_='text').text
    author = quote.find('small', class_='author').text
    tags = [tag.text for tag in quote.find('div', class_='tags').find_all('a', class_='tag')]
    data.append([quote_text, author, ', '.join(tags)])

# Store the extracted data in a CSV file
with open('Quotes.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Quote', 'Author', 'Tags'])  # header row
    writer.writerows(data)

print("Data extracted and saved to Quotes.csv!")  