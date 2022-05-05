# https://admin-demo.nopcommerce.com/
import time
from selenium.webdriver.support.select import Select

class AddCustomerPage:
    lnkCustomers_Menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomers_Menuitem_xpath = "//body[1]/div[3]/aside[1]/div[1]/div[4]/div[1]/div[1]/nav[1]/ul[1]/li[4]/ul[1]/li[1]/a[1]/p[1]"
    btnAddnew_xpath = "//a[@class='btn btn-primary']"

    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    rdMaleGender_id = "Gender_Male"
    rdFemaleGender_id = "Gender_Female"
    txtDob_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_xpath = "//input[@id='Company']"

    txtcustomerRoles_xpath = "//*[@id='customer-info']/div[2]/div[10]/div[2]/div/div[1]/div/div"
    lstitemAdministrators_xpath = "//li[contains(text(),'Administrators')]"
    lstitemRegistered_xpath = "//li[contains(text(),'Registered')]"
    lstitemGuests_xpath = "//li[contains(text(),'Guests')]"
    lstitemVendors_xpath = "//li[contains(text(),'Vendors')]"
    drpmgrOfVendor_xpath = "//select[@id='VendorId']"


    txtAdminContent_xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath = "//button[@name='save']"


    def __init__(self, driver):
        self.driver = driver

    def clickonCustomerMenu(self):
        self.driver.find_element_by_xpath(self.lnkCustomers_Menu_xpath).click()

    def clickonCustomerMenuitem(self):
        self.driver.find_element_by_xpath(self.lnkCustomers_Menuitem_xpath).click()

    def clickOnAddnew(self):
            self.driver.find_element_by_xpath(self.btnAddnew_xpath).click()

    def setEmail(self, email):
            self.driver.find_element_by_xpath(self.txtEmail_xpath).send_keys(email)

    def setPassword(self, password):
            self.driver.find_element_by_xpath(self.txtPassword_xpath).send_keys(password)

    def setFirstName(self, FirstName):
            self.driver.find_element_by_xpath(self.txtFirstName_xpath).send_keys(FirstName)

    def setLastName(self, LastName):
            self.driver.find_element_by_xpath(self.txtLastName_xpath).send_keys(LastName)

    def setGender(self,gender):
                if gender == 'Male':
                    self.driver.find_element_by_id(self.rdMaleGender_id).click()
                elif gender == 'Female':
                    self.driver.find_element_by_id(self.rdFemaleGender_id).click()
                else:
                    self.driver.find_element_by_id(self.rdMaleGender_id).click()

    def setdob(self, dob):
                    self.driver.find_element_by_xpath(self.txtDob_xpath).send_keys(dob)

    def setCompanyName(self, ComapnyName):
                    self.driver.find_element_by_xpath(self.txtCompanyName_xpath).send_keys(ComapnyName)

    def setCustomerRole(self, role):
                    self.driver.find_element_by_xpath(self.txtcustomerRoles_xpath).click()
                    time.sleep(3)
                    if role == 'Registered':
                        self.listitem = self.driver.find_element_by_xpath(self.lstitemRegistered_xpath)
                    elif role == 'Administrators':
                        self.listitem = self.driver.find_element_by_xpath(self.lstitemAdministrators_xpath)
                    elif role == 'Guests':
                        # Here user can be Registered( or) Guest, only one
                        time.sleep(3)
                        self.driver.find_element_by_xpath(
                            "//*[@id ='customer-info']/div[2]/div[10]/div[2]/div/div[1]/div/div/span[1]").click()

                        self.listitem = self.driver.find_element_by_xpath(self.lstitemGuests_xpath)
                    elif role == 'Vendors':
                        self.listitem = self.driver.find_element_by_xpath(self.lstitemVendors_xpath)
                    else:
                        self.listitem = self.driver.find_element_by_xpath(self.lstitemGuests_xpath)

                    time.sleep(3)
                    self.driver.execute_script("arguments[0].click();", self.listitem)

    def setManageofVendor(self, value):
                drp = Select(self.driver.find_element_by_xpath(self.drpmgrOfVendor_xpath))
                drp.select_by_index(value)

    def setAdmincontent(self, content):
                self.driver.find_element_by_xpath(self.txtAdminContent_xpath).send_keys(content)

    def ClickSave(self):
                self.driver.find_element_by_xpath(self.btnSave_xpath).click()
