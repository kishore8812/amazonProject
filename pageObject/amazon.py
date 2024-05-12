import time
import keyboard
from utilities.readProperties import ReadConfig

from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime
from selenium.webdriver import ActionChains
from datetime import datetime, timedelta
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Amazon:
        text_google_search_xpath = "//textarea[@title='Search']"
        search_results_xpath = "//div[@role='presentation']/ul/li/div[1]/div[2]/div[1]/div[1]/span"
        web_search_results_xpath = ".//h3"
        text1_google_search_xpath = "//textarea[@aria-label='Search']"
        text_phone_number_xpath = "//input[@type='email']"
        text_password_number_xpath = "//input[@type='password']"
        Sign_button_click_xpath = "//input[@type='submit']"
        All_category_button_xpath = "//label[@id='searchDropdownDescription']/parent::div"
        All_category_list_xpath = "//label[@id='searchDropdownDescription']/parent::div/select/option"
        text_amazonsearch_bar_xpath = "//input[@placeholder='Search Amazon.in']"
        min_price_slider_xpath = "//div[@class='a-section a-spacing-mini sf-range-slider-row']/div[1]/div[1]/input"
        max_price_slider_xpath = "//div[@class='a-section a-spacing-mini sf-range-slider-row']/div[1]/div[2]/input"
        text_min_price = "//input[@placeholder='Min']"
        text_max_price= "//input[@placeholder='Max']"
        button_go_xpath = "//span[contains(text(),'Go')]/parent::span/input"
        item_price_xpath = "//span[@class='a-price-whole']"
        button_page_2_xpath = "//a[contains(text(),'Next')]"

        rating_xpath = "//span[@class='a-icon-alt']"
        products_with_five_star_xpath = "//span[contains(text(),'5.0 out of 5 stars')]/parent::i/parent::a/parent::span/parent::span/parent::div/parent::div/parent::div/div[1]"
        product_name_with_5star_xpath = "//span[contains(text(),'5.0 out of 5 stars')]/parent::i/parent::a/parent::span/parent::span/parent::div/parent::div/parent::div/div[1]/h2/a"
        button_previous_xpath = "//a[contains(text(),'Previous')]"
        add_to_cart_xpath = "//input[@id='add-to-cart-button']/parent::span"
        exit_button_xpath = "//a[@aria-label='Exit this panel and return to the product page. ']"
        cart_button_xpath = "//div[@id='nav-cart-count-container']"
        cart_item_text_xpath = "//span[@class='a-truncate-cut']/parent::span"
                # "//div[@class='sc-list-overwrap']/parent::div/div[3]/div[4]/div[1]/div[3]/ul/li/span/a/span/span/span[1]"
        button_cart_xpath = "//input[@aria-labelledby='attach-sidesheet-view-cart-button-announce']/parent::span"



        def __init__(self, driver):
                self.driver = driver

        def searchbar(self, search):
                self.driver.find_element(By.XPATH, self.text_google_search_xpath).send_keys(search)
                time.sleep(2)
                results = self.driver.find_elements(By.XPATH, self.search_results_xpath)
                items = len(results)
                print(items)

                for result in results:
                        print(result.get_attribute('innerText'))#it will print all the search results in the search bar after entering the word amazon

                for result in results:
                        if result.get_attribute('innerText') == "Amazon":
                                result.click() #It will search for Amazon word and then click on the Amazon word
                                break

                time.sleep(2)
                eles = self.driver.find_elements(By.XPATH, self.web_search_results_xpath)
                print(len(eles))

                for ele in eles:
                        print(ele.get_attribute('innerText')) #it will print all the search results in the web page




        def amazon_login(self, search_1, email, password):

                ele = self.driver.find_element(By.XPATH, self.text1_google_search_xpath).send_keys(search_1)
                action = ActionChains(self.driver)
                action.send_keys(Keys.ENTER).perform()
                self.driver.implicitly_wait(10)

                eles = self.driver.find_elements(By.XPATH, self.web_search_results_xpath)
                print(len(eles))

                for ele in eles:
                        if ele.get_attribute('innerText') == "Sign in":
                                ele.click()
                                break
                        break

                self.driver.implicitly_wait(10)
                ele = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, self.text_phone_number_xpath))
                )
                ele.send_keys(email)
                ele = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, self.text_password_number_xpath)))
                ele.send_keys(password)
                self.driver.execute_script("arguments[0].click();", WebDriverWait(self.driver, 20).until(
                        EC.element_to_be_clickable((By.XPATH, self.Sign_button_click_xpath))))
                self.driver.implicitly_wait(10)

        def item_select(self, search_2, min, max):
                self.driver.find_element(By.XPATH, self.All_category_button_xpath).click()
                results = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_all_elements_located((By.XPATH, self.All_category_list_xpath))
                )

                for result in results:
                        if result.get_attribute('innerText') == "Electronics":
                                result.click() #It will search for Amazon word and then click on the Amazon word
                                break
                self.driver.implicitly_wait(10)
                ele = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, self.text_amazonsearch_bar_xpath)))
                ele.clear()
                ele.send_keys(search_2)
                action = ActionChains(self.driver)
                action.send_keys(Keys.ENTER).perform()
                ele = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, self.text_min_price))
                )
                ele.send_keys(min)
                time.sleep(1)
                ele = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, self.text_max_price)))
                ele.send_keys(max)
                time.sleep(2)
                action = ActionChains(self.driver)
                action.send_keys(Keys.ENTER).perform()
                self.driver.implicitly_wait(10)


        def price_select_add_to_cart(self):

                results = self.driver.find_elements(By.XPATH, self.item_price_xpath)
                #print the price of page 1
                for result in results:
                        number_str = result.get_attribute('innerText')
                        number_str = number_str.replace(",", "")  # Remove the comma
                        number_int = int(number_str)
                        if 30000 <= number_int <= 50000:  # Check if the price range is between 30k to 50k
                                print(number_int)


                        else:
                                print('Items price are not in the selected price range')
                                self.driver.save_screenshot(".\\Screenshots\\" + "Price_incorrect.png")

                five_star_products = self.driver.find_elements(By.XPATH, self.products_with_five_star_xpath)
                # print the the text of 5 star rating items in page 1
                for ele in five_star_products:
                        print('Five-star items are for 1st page:', ele.text)


                time.sleep(2)

                self.driver.find_element(By.XPATH, self.button_page_2_xpath).click()
                time.sleep(5)
                results = self.driver.find_elements(By.XPATH, self.item_price_xpath)
                # print the price of page 2
                for result in results:
                        number_str = result.get_attribute('innerText')
                        number_str = number_str.replace(",", "") # Remove the comma
                        number_int = int(number_str)
                        if 30000 <= number_int <= 50000:  # Check if the price range is between 30k to 50k
                                print(number_int)


                        else:
                                print('Items price are not in the selected price range in page 2')
                                self.driver.save_screenshot(".\\Screenshots\\" + "Price_incorrect.png")


                #print the the text of 5 star rating items in page 2
                five_star_products = self.driver.find_elements(By.XPATH, self.products_with_five_star_xpath)
                for ele in five_star_products:
                        print('Five-star items are for 2nd page:', ele.text)
                time.sleep(2)
                self.driver.find_element(By.XPATH, self.button_previous_xpath).click()
                time.sleep(5)


        def add_to_cart(self):

                list = []
                five_star_products = self.driver.find_elements(By.XPATH, self.products_with_five_star_xpath)
                for ele in five_star_products:
                        list.append(ele.text)
                print(list)
                #click on 1st 5 star rating element
                products = self.driver.find_elements(By.XPATH, self.product_name_with_5star_xpath)
                for prod in products:
                        prod.click()
                        break

                time.sleep(2)
                self.driver.switch_to.window(self.driver.window_handles[1])
                time.sleep(5)
                self.driver.find_element(By.XPATH, self.add_to_cart_xpath).click()
                time.sleep(5)
                # self.driver.find_element(By.XPATH, self.button_cart_xpath).click()
                # #click on cart
                # time.sleep(2)
                self.driver.execute_script("arguments[0].click();", WebDriverWait(self.driver, 20).until(
                        EC.element_to_be_clickable((By.XPATH, self.cart_button_xpath))))
                self.driver.implicitly_wait(10)


                ele = self.driver.find_element(By.XPATH, self.cart_item_text_xpath)
                print(ele.text)

                #Verifyif the correct item is added to the cart
                if list[0] == ele.text:
                        assert True
                else:
                        self.driver.save_screenshot(".\\Screenshots\\" + "item not added.png")
                        assert False



















