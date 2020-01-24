from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
url = "http://www.so365.in/Goodbits_ESS"


def smartoffice_login():
	driver.get(url)
	driver.find_element_by_id("txtUserName").send_keys("akhil")
	driver.find_element_by_id("txtPassword").send_keys("akhil123")
	driver.find_element_by_xpath('//*[@id="tableposition"]/tbody/tr[3]/td[2]/input[1]').click()
	driver.implicitly_wait(4)
	driver.find_element_by_xpath('//*[@id="bs-example-navbar-collapse-1"]/ul[1]/li[3]/a').click()
	driver.find_element_by_xpath('//*[@id="bs-example-navbar-collapse-1"]/ul[1]/li[3]/ul/li[3]/a').click()
	driver.implicitly_wait(10)

	mytable = driver.find_element_by_xpath('//*[@id="dg_EmployeeSwipeDetails"]/div[2]/table')
	for row in mytable.find_elements_by_css_selector('tr'):
		print(row.text)
smartoffice_login()