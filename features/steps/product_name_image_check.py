from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep



@then('Every product on the search results page should have')
def check_product_name_image(context):
    products = context.driver.find_elements(By.XPATH, "//div[contains(@class , 'styles_product')]")

    for i, product in products(products, start=1):

         name = product.find_elements(By.XPATH, '//div[contains(@style,"--truncate")]]').text
         assert name.strip() != "", f"Product {i} has no name!"


         img = product.find_element(By.XPATH, "li[class*='CarouselItem'] img")
         src = img.get_attribute("src")
         assert src and "data:image" not in src, f"Product {i} has no valid image!"

    sleep(2)