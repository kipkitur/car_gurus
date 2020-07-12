# import the required modules
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

# we will use Google Chrome in this test. Specify the location of your chromedriver.exe
webdriver_location = "\\Users\\kemei\\Downloads\\chromedriver_win32\\chromedriver.exe"

# the webpage we want to access for our test
car_model_information_page = "https://www.cargurus.com/Cars/forsale"


#USE FIXTURES TO DEFINE THE CODE TO RUN BEFORE AND AFTER THE TESTS
@pytest.fixture
def browser_setup():
    browser = webdriver.Chrome(webdriver_location)
    browser.maximize_window()
    browser.implicitly_wait(10)

    yield browser

    browser.quit()

# We include the fixture name as a parameter in a test function and rely on it to initialize the browser’s window before our function runs
# and to close it once our code completes – no matter how assert statements finish

def test_dropdown(browser_setup):
    # Test name: dropdown
    # Step # | name | target | value
    # 1 | open | /model-information |
    browser_setup.get(car_model_information_page)
    # 2 | maximize Window Size |
    browser_setup.maximize_window()
    # 3 | locate make element | name=selectedMakeId |
    make = browser_setup.find_element(By.NAME, "selectedMakeId")
    make.click()
    # 4 | locate make selected | click on Hyundai |
    make = browser_setup.find_element(By.XPATH, "//*[@id=\"Select Make\"]/optgroup[1]/option[15]")
    make.click()
    # 5 | locate model element | name=selectedModelId |
    model = browser_setup.find_element(By.NAME, "selectedModelId")
    model.click()
    # 6 | locate model selected | click on Sonata |
    model = browser_setup.find_element(By.XPATH, "//*[@id=\"Select Model\"]/optgroup[1]/option[21]")
    model.click()
    # 7 | locate min year dropdown | select 2015 as minimum year|
    min_year = browser_setup.find_element(By.NAME, "selectedStartYear")
    min_year.click()
    min_year = browser_setup.find_element(By.XPATH, "//*[@id=\"Select From Year\"]/option[7]")
    min_year.click()
    # 8 | locate max year dropdown | select 2017 as maximum year|
    max_year = browser_setup.find_element(By.NAME, "selectedEndYear")
    max_year.click()
    max_year = browser_setup.find_element(By.XPATH, "//*[@id=\"Select To Year\"]/option[5]")
    max_year.click()
    # 9 | locate min price input field| input value of $12000|
    min_price = browser_setup.find_element(By.ID, "minPrice")
    min_price.send_keys(12000)
    # 10 | locate max price input field| input value of $16000|
    max_price = browser_setup.find_element(By.ID, "maxPrice")
    max_price.send_keys(16000)
    # 11 | locate zip code input field| input zipcode for your area|
    zip_code = browser_setup.find_element(By.ID, "postal-code-input")
    zip_code.send_keys(22041)
    # 12 | locate dropdown to select radius option| click on radius of 25 miles|
    radius = browser_setup.find_element(By.ID, "radius")
    radius.click()
    radius = browser_setup.find_element(By.XPATH, "//*[@id=\"radius\"]/option[2]")
    radius.click()
    # 13 | locate the search button| click on the search button|
    search_used_cars_button = browser_setup.find_element(By.XPATH, "//*[@id=\"search-form\"]/form/button")
    search_used_cars_button.click()

    # set window size for your screenshot
    browser_setup.set_window_size(1800, 2200)
    # take a screenshot of the page
    # screenshots are important for visual testing
    browser_setup.save_screenshot("\\Users\\kemei\\Downloads\\used_hyundai_sonata_2015_2017.png")


    print("Program - End")