# Add customer Page
from selenium import webdriver
class SearchCustomer:
    txtEmail_id = "SearchEmail"
    txtFirstName_id = "SearchFirstName"
    txtLastName_id = "SearchLastName"
    btnSearch_id = "search-customers"
    tblSearchResults_xpath = "//table[@role='grid']"
    table_xpath = "//table[@id='customers-grid']"
    tableRows_xpath = "//table[@id='customers-grid']//tbody/tr"
    tableColumns_xpath = "//table[@id='customers-grid']//tbody/tr/td"


    def __init__(self, driver):
        self.driver = driver

    def setemail(self,email):
        self.driver.find_element_by_id(self.txtEmail_id).clear()
        self.driver.find_element_by_id(self.txtEmail_id).send_keys(email)

    def setFirstName(self, FirstName):
        self.driver.find_element_by_id(self.txtFirstName_id).clear()
        self.driver.find_element_by_id(self.txtFirstName_id).send_keys(FirstName)

    def setLastName(self,LastName):
        self.driver.find_element_by_id(self.txtLastName_id).clear()
        self.driver.find_element_by_id(self.txtLastName_id).send_keys(LastName)

    def clickSearchBtn(self):
        self.driver.find_element_by_id(self.btnSearch_id).click()

    def getNosRows(self):
        return len(self.driver.find_elements_by_xpath(self.tableRows_xpath))

    def getNosColumn(self):
        return len(self.driver.find_elements_by_xpath(self.tableColumns_xpath))

    def getCustomerEmail(self,email):
        flag=False
        for r in range(1, self.getNosRows() + 1):
            table=self.driver.find_element_by_xpath(self.table_xpath)
            emailid=table.find_element_by_xpath("//*[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
            if emailid==email:
                flag=True
                break
        return flag

    def getCustomerName(self,Name):
        flag=False
        for r in range(1, self.getNosRows() + 1):
            table = self.driver.find_element_by_xpath(self.table_xpath)
            name=self.find_element_by_xpath("//*[@id='customers-grid']/tbody/tr["+str(r)+"]/td[3]").text
            if name==Name:
                flag=True
                break
                return flag