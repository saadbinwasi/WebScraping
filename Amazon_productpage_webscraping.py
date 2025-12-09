import requests
from bs4 import BeautifulSoup

headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
  'Accept-Language': 'en-US,en;q=0.5'
}


def get_product_details(product_url:str) -> dict :
  product_details = {}

  # //get the product page content and create a soup
  page = requests.get(product_url, headers=headers)
  soup = BeautifulSoup(page.content, features='lxml')

  try:
    title = soup.find('span', attrs={'id': 'productTitle'}).get_text().strip()
    price = soup.find('span', attrs={'class': 'a-offscreen'}).get_text().strip()

    # Adding it to the product details dictionary
    product_details['title'] = title
    product_details['price'] = price

    return product_details
  except Exception as e:
    print(f"Error getting product details: {e}")
    return None


product_url = input("Enter the product URL: ")
product_details = get_product_details(product_url)
print(product_details)