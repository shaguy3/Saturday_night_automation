from selenium import webdriver
import openpyxl
import os
import bs4
import datetime

# TODO: Open a browser at the speed test url
speed_test_url = 'https://inteligence.speedtest.net/#login'
browser = webdriver.Firefox()
browser.get(speed_test_url)

# TODO: Login to the website and navigate to the mobile compare section
browser.find_element_by_class_name('auth0-lock-social-button-text').click()
browser.find_element_by_class_name('_3VhGO2').click()
browser.find_elements_by_class_name('_1d5bD6 _2XdgY-') # Sorts by name

# TODO: Take each of the operator's speed results, and put them in the excel workbook
excel_workbook_path = os.path.join('j:', 'DATA', 'CONTROLR', 'CELLS', 'speed test', 'speed test - 2019.xls')
wb = openpyxl.load_workbook(excel_workbook_path)
sheet = wb.get_active_sheet()
start_row = 1
stop = False
while not stop:
    if not sheet['C{}'.format(start_row)] == '':
        start_row += 1
    else:
        stop = True
for download_speed in browser.find_elements_by_class_name('GRkLy3'):
    pass
