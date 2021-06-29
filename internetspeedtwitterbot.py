from selenium import webdriver
import time

class InternetSpeedTwitterBot:
    def __init__(self):
        self.path = "/Users/edwinzwanenburg/Code/chromedriver"
        self.driver = webdriver.Chrome(executable_path=self.path)
        self.down = None
        self.up = None

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        go_btn = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        go_btn.click()

        time.sleep(50)

        down = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        up = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span')
        self.down = float(down.text)
        self.up = float(up.text)

    def tweet_at_provider(self):
        print("sending tweet")