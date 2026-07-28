from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import csv
import time

# Website URL

url = "https://tiedex.co.uk/collections/all-products"

# Chrome Driver
options = webdriver.ChromeOptions()
# options.add_argument("--headless")   # Uncomment to run headless
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get(url)

wait = WebDriverWait(driver, 10)


# Collect Product Links

product_links = set()

product_xpath = "//div[contains(@class,'product-grid-item')]//a[contains(@href,'/products/')]"

for page in range(20):

    print(f"\nScraping Page {page+1}")

    wait.until(
        EC.presence_of_all_elements_located((By.XPATH, product_xpath))
    )

    products = driver.find_elements(By.XPATH, product_xpath)

    for product in products:
        href = product.get_attribute("href")
        if href:
            product_links.add(href)

    print("Products Collected:", len(product_links))

    try:
        first_product = products[0]

        next_button = driver.find_element(
            By.XPATH,
            "//a[contains(@aria-label,'Next')]"
        )

        driver.execute_script("arguments[0].click();", next_button)

        wait.until(EC.staleness_of(first_product))

    except NoSuchElementException:
        print("No More Pages.")
        break

print("\nTotal Product Links:", len(product_links))


# Scrape Product Details
all_data = []

for count, link in enumerate(product_links, start=1):

    print(f"{count}. {link}")

    driver.get(link)

    time.sleep(2)

    soup = BeautifulSoup(driver.page_source, "html.parser")

    #Title
    title = ""

    title_tag = soup.find("h1")

    if title_tag:
        title = title_tag.get_text(strip=True)

    #Price
    price = ""

    price_selectors = [
        ".price",
        ".product__price",
        ".price-item",
        ".money"
    ]

    for selector in price_selectors:
        tag = soup.select_one(selector)
        if tag:
            price = tag.get_text(strip=True)
            break

    #Description
    description = ""

    description_selectors = [
        ".product__description",
        ".product-description",
        ".rte",
        ".description"
    ]

    for selector in description_selectors:
        tag = soup.select_one(selector)
        if tag:
            description = tag.get_text(" ", strip=True)
            break

    #Availability
    availability = "Out of Stock"

    page_text = soup.get_text(" ", strip=True).lower()

    if "in stock" in page_text:
        availability = "In Stock"
    elif "out of stock" in page_text:
        availability = "Out of Stock"
    elif "sold out" in page_text:
        availability = "Sold Out"

    all_data.append([
        title,
        price,
        description,
        availability,
        link
    ])


# Save CSV
with open("products.csv", "w", newline="", encoding="utf-8") as file:

    writer = csv.writer(file)

    writer.writerow([
        "Title",
        "Price",
        "Description",
        "Availability",
        "URL"
    ])

    writer.writerows(all_data)

driver.quit()
print("\nScraping Completed Successfully!")
print("Data saved to products.csv")