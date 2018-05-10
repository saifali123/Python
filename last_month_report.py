#!/bin/bash
from selenium import webdriver
import time 
import unittest
class TestStringMethods(unittest.TestCase):
	def test_last_month_report(self):
        
	
		print ("Opening Browser")
		driver=webdriver.Chrome()
		print ("Browsing Marketplace.kumolus.com")
		driver.get('https://marketplace.kumolus.com/login')
		time.sleep(5)
        
	
		print ("Passing Credentials")
		user=driver.find_element_by_id('session_username')
		user.send_keys('###')
		password=driver.find_element_by_id('session_password')
		password.send_keys('###')
		login=driver.find_element_by_xpath('//*[@id="new_session"]/div[3]/div[5]/input[2]')
		login.click()
		print ("Login Successfully Done!")
	

		print ("On Report Page")
		driver.get('https://marketplace.kumolus.com/reports/cost_report')
		driver.maximize_window()
	

		print ("Selecting last month cost")
        	time.sleep(3)
		custom=driver.find_element_by_xpath('/html/body/div[6]/div[3]/div/div/div/div[1]/div/div/button[2]')
		custom.click()
		calender=driver.find_element_by_xpath('//*[@id="reportrange"]')
        	calender.click()	
		last_month=driver.find_element_by_xpath('/html/body/div[9]/div[1]/ul/li[2]')
        	last_month.click()
		time.sleep(5)
	
	
		print ("Clicking Apply")
		apply_button=driver.find_element_by_xpath('//*[@id="custom"]/ng-include/div/div[1]/div/div[2]/form/div[5]/div/input[2]')
		apply_button.click()
		time.sleep(10)
	
		#Total Cost of Last Month
		total_cost=driver.find_element_by_xpath('//*[@id="custom"]/ng-include/div/div[2]/div[1]/div[2]/div/div[1]/div[1]/span').text
        	print total_cost
	
	
	#def test_tearDown(self):
    	#	self.driver.quit()
           

#last_month_report()
	
if __name__ == '__main__':
    unittest.main() 




