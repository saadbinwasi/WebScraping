# Amazon Product Page Web Scraper

A beginner-friendly Python script that extracts product title and price from Amazon product pages.

## Prerequisites

Install required libraries:
```bash
pip install requests beautifulsoup4 lxml
```

## How It Works

### Step 1: Import Libraries
```python
import requests
from bs4 import BeautifulSoup
```
- `requests`: Fetches the webpage HTML
- `BeautifulSoup`: Parses and extracts data from HTML

### Step 2: Set Up Headers
```python
headers = {
  'User-Agent': 'Mozilla/5.0...',
  'Accept-Language': 'en-US,en;q=0.5'
}
```
**Why?** Websites may block requests without a browser-like User-Agent. Headers make the request look like it's coming from a real browser.

### Step 3: Fetch the Webpage
```python
page = requests.get(product_url, headers=headers)
```
- Sends an HTTP GET request to the Amazon product URL
- Returns the HTML content of the page

### Step 4: Parse HTML
```python
soup = BeautifulSoup(page.content, features='lxml')
```
- Converts raw HTML into a searchable object
- `lxml` is the parser that processes the HTML structure

### Step 5: Extract Data
```python
title = soup.find('span', attrs={'id': 'productTitle'}).get_text().strip()
price = soup.find('span', attrs={'class': 'a-offscreen'}).get_text().strip()
```
- `soup.find()`: Searches for specific HTML elements
- `attrs={'id': 'productTitle'}`: Finds the `<span>` tag with `id="productTitle"`
- `.get_text()`: Extracts the text content
- `.strip()`: Removes extra whitespace

### Step 6: Store Results
```python
product_details['title'] = title
product_details['price'] = price
```
- Stores extracted data in a dictionary

### Step 7: Error Handling
```python
try:
    # extraction code
except Exception as e:
    print(f"Error getting product details: {e}")
    return None
```
- Catches errors if elements aren't found or the page structure changes

## Usage

1. Run the script:
```bash
python Amazon_productpage_webscraping.py
```

2. Enter an Amazon product URL when prompted:
```
Enter the product URL: https://www.amazon.com/...
```

3. View the results:
```python
{'title': 'Product Name', 'price': '$29.99'}
```

## Understanding HTML Selectors

To find the right selectors:
1. Open the Amazon product page in your browser
2. Right-click on the element you want (title/price)
3. Select "Inspect" to see the HTML
4. Look for unique attributes like `id` or `class`
5. Use those attributes in `soup.find()`

## Important Notes

- ⚠️ **Respect robots.txt**: Check if scraping is allowed
- ⚠️ **Rate Limiting**: Don't send too many requests too quickly
- ⚠️ **Website Changes**: HTML structure may change, requiring selector updates
- ⚠️ **Legal**: Ensure your scraping complies with Amazon's Terms of Service

