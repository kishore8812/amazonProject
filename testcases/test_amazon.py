import pytest
from selenium import webdriver
import time

from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
from pageObject.amazon import Amazon



class Test_001_Amazon(LogGen):

    path = './/TestData/Data.xlsx'
    logger = LogGen.loggen()

    # @pytest.mark.sanity
    # @pytest.mark.regression
    def test_001(self):
        self.search = XLUtils.readData(self.path, 'Amazon', 1, 2)
        self.amazon = Amazon(self.driver)
        self.amazon.searchbar(self.search)
        self.logger.info("*******amazon name is searched***********")
        self.logger.info("*******results are printed***********")
        self.logger.info("*******Clicked on amazon text***********")
        self.logger.info("*******printed all results of the search results***********")
        time.sleep(2)

    def test_002(self):
        self.search_1 = XLUtils.readData(self.path, 'Amazon', 2, 2)
        self.email = XLUtils.readData(self.path, 'Amazon', 3, 2)
        self.password = XLUtils.readData(self.path, 'Amazon', 4, 2)
        self.amazon = Amazon(self.driver)
        self.amazon.amazon_login(self.search_1, self.email, self.password)
        self.logger.info("*******Amazon login is searched***********")
        self.logger.info("*******User entered its email and password***********")
        self.logger.info("*******User is able to login***********")
        time.sleep(2)

    def test_003(self):
        self.search_2 = XLUtils.readData(self.path, 'Amazon', 5, 2)
        self.min = XLUtils.readData(self.path, 'Amazon', 6, 2)
        self.max = XLUtils.readData(self.path, 'Amazon', 7, 2)
        self.amazon = Amazon(self.driver)
        self.amazon.item_select(self.search_2, self.min, self.max)
        self.logger.info("*******User clicked on the All button in the search bar***********")
        self.logger.info("*******User search for the electronics section and then clicked on the electronics text***********")
        self.logger.info("*******User searched for dell computer***********")

    def test_004(self):
        self.amazon = Amazon(self.driver)
        self.amazon.price_select_add_to_cart()
        self.logger.info("*******Searched for all the 5 star rating items in 1st and 2nd pager***********")
        self.logger.info("*******Verified if the price is in the range of 30k to 50k***********")
        self.logger.info(
            "*******Printed the 5 star rating items from page 1 and page 2***********")




    def test_005(self):
        self.amazon = Amazon(self.driver)
        self.amazon.add_to_cart()
        self.logger.info(
            "*******added the 1st 5 star rating item from page 1***********")
        self.logger.info("*******Click on Add to cart***********")
        self.logger.info("*******Verified if the item is added to the cart and the item is matching***********")



