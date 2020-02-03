from datetime import date, datetime

today = date.today()
# today_date = int(today.strftime("%d"))
today_date = 3
punch_list = []

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
# chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('/home/akhil/Documents/company_time_logger/chromedriver', chrome_options=chrome_options)

url = "http://www.so365.in/Goodbits_ESS"


class IntimeCalc:

    def smartoffice_login(self):
        driver.get(url)
        driver.find_element_by_id("txtUserName").send_keys("akhil")
        driver.find_element_by_id("txtPassword").send_keys("akhil123")
        driver.find_element_by_xpath('//*[@id="tableposition"]/tbody/tr[3]/td[2]/input[1]').click()
        driver.implicitly_wait(4)
        driver.find_element_by_xpath('//*[@id="bs-example-navbar-collapse-1"]/ul[1]/li[3]/a').click()
        driver.find_element_by_xpath('//*[@id="bs-example-navbar-collapse-1"]/ul[1]/li[3]/ul/li[3]/a').click()
        driver.implicitly_wait(5)

        iframe = driver.find_elements_by_tag_name('iframe')[0]
        driver.switch_to.frame(iframe)
        driver.implicitly_wait(50)
        table = driver.find_elements_by_tag_name('table')[3]
        # tr_list = table.find_elements_by_css_selector(
        #     '#dg_EmployeeSwipeDetails > div.k-grid-content.k-auto-scrollable > table > tbody > tr:nth-child(3) > td:nth-child(1)')
        for i in range(20):
            print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>   ',i )
            selector = '#dg_EmployeeSwipeDetails > div.k-grid-content.k-auto-scrollable > table > tbody > tr:nth-child('+ str(
                i + 1) + ') > td:nth-child(1)'
            # dg_EmployeeSwipeDetails > div.k-grid-content.k-auto-scrollable > table > tbody > tr:nth-child(2)
            td = table.find_element_by_css_selector(selector)
            # print(td.text)

            date_string = td.text
            print(9999, date_string)
            try:
                date = int(date_string.split('-')[0])
            except:
                date = -9999
            if date == today_date:
                date_string_modified = date_string.split()
                date_obj = datetime.strptime(date_string_modified[0] + ' ' + date_string_modified[1],
                                             '%d-%b-%Y %H:%M:%S')
                punch_list.append(date_obj)

        return punch_list

    def calculate_intime(self, todays_punch_list):
        total_intime , total_outitme = 0, 0
        date_objects = list(reversed(todays_punch_list))
        print(000000, date_objects)
        len_dates = len(date_objects)
        for index, x in enumerate(date_objects):
            if index + 1 < len_dates:
                diff = date_objects[index + 1] - x
                if index % 2 == 0:
                    print(date_objects[index + 1] ,'   ===  ',x)
                    print('In times>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>',diff.total_seconds()/60)
                    total_intime += diff.total_seconds()
                else:
                    total_outitme += diff.total_seconds()
        return total_intime/360, total_outitme/360

time_cal_obj = IntimeCalc()
todays_punch_list = time_cal_obj.smartoffice_login()
total_intime, total_outitme = time_cal_obj.calculate_intime(todays_punch_list)
print('====total_intime======', total_intime)
print('=====total_outitme=====', total_outitme)
