import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService

def get_product_details(driver, product_list):
    details = []
    products = driver.find_elements(By.XPATH, product_list)
    for product in products:
        name = product.find_element(By.XPATH, ".//h2").text
        price = product.find_element(By.XPATH, ".//span[@class='a-offscreen']").text
        details.append([name, price])
    return details

def main():
    # Set the path to your ChromeDriver executable
    chrome_driver_path = '/path/to/chromedriver'

    # Set the URL and product to search for
    url = 'https://www.amazon.com'
    search_query = 'laptop'

    # Set the path to save the CSV file
    output_file = 'output.csv'

    # Set the XPath for the product list
    product_list_xpath = "//div[@data-component-type='s-search-result']"

    # Set up the Chrome driver
    service = ChromeService(chrome_driver_path)
    driver = webdriver.Chrome(service=service)

    # Open Amazon and search for the product
    driver.get(url)
    search_box = driver.find_element(By.ID, 'twotabsearchtextbox')
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)

    # Wait for the product list to load
    driver.implicitly_wait(10)

    # Get and print the product details
    product_details = get_product_details(driver, product_list_xpath)
    for detail in product_details:
        print(detail)

    # Save the product details to a CSV file
    with open(output_file, 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Name', 'Price'])
        csv_writer.writerows(product_details)

    # Close the browser
    driver.quit()

if __name__ == "__main__":
    main()
