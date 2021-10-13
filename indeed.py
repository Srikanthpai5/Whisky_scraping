path = "D:\\PyCharm_Files\\selenium\\chromedriver_win32\\chromedriver.exe"

from selenium import webdriver
import pandas as pd
import time

search_query = 'https://www.indeed.com/q-data-scientist-jobs.html'
driver = webdriver.Chrome(executable_path=path)
job_details = []

driver.get(search_query)
time.sleep(5)


job_list = driver.find_elements_by_xpath("//div[@data-tn-component='organicJob']")


for job in job_list:
    title = job.find_elements_by_xpath('.//h2[@class="title"]/a')
    print(title)
    time.sleep(1)
    break

driver.close()

# scraping not complete -- cls&&exit

