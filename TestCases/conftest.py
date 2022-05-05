import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture()
def setup(browser):

    if browser=='chrome':
     serv_obj = Service("F:\\Python\\copcommerce\\Driver\\chromedriver.exe")
     driver = webdriver.Chrome(service=serv_obj)
    elif browser=='firefox':
      serv_obj = Service("F:\\Python\\copcommerce\\Driver\\internetexplorer.exe")
      driver = webdriver.ie(service=serv_obj)
    else:
      serv_obj = Service("F:\\Python\\copcommerce\\Driver\\chromedriver.exe")
      driver = webdriver.Chrome(service=serv_obj)
      print("__Launching chrome browser__")

    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

############### pyTest html Report ###############
#it is Hook for adding environment info to html report

def pytest_configure(config):
    config._metadata['Project Name']= 'nop Commerce'
    config._metadata['Module Name'] = 'Customer'
    config._metadata['Tester'] = 'Dhananjay'

#it is Hook for removing environment info to html report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)