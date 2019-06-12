from framework.base.Selenium_driver import SeleniumDriver
from selenium.webdriver.common.action_chains import ActionChains


class HomePage(SeleniumDriver):

    # locators
    _signInMenu = "//div[@id='nav-tools']/a/span[2]"
    _signInBTN = "//div[@id='nav-flyout-yourAccount']//span[.='Sign in']"
    _shopByCaIid = "nav-link-shopall"
    _submenuWomen = "//div[@id='nav-flyout-shopAll']/div[2]//span[.=\"Women's Fashion\"]"
    _subCatLinkWomen = "//div[@id='nav-flyout-shopAll']/div[3]//span[.='Western Wear']"
    _submenuAlexa = "//div[@id='nav-flyout-shopAll']/div[2]//span[.='Echo & Alexa']"
    _subCatLinkAlexa = "//div[@id='nav-flyout-shopAll']/div[3]//span[.='Amazon Echo']"
    _submenuMobiles = "//div[@id='nav-flyout-shopAll']/div[2]//span[.='Mobiles, Computers']"
    _subCatLinkMobiles = "//div[@id='nav-flyout-shopAll']/div[3]//span[.='All Mobile Phones']"
    _cartId = "nav-cart-count"
    _signOutLink = "nav-item-signout"
    _searchInput = "twotabsearchtextbox"
    _searchBTN = "//input[@type='submit' and @value='Go']"

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver



    """Method for login to the website"""
    def goToLogin(self):
        self.mouseHover(self._signInMenu, "xpath")
        self.driver.implicitly_wait(5)
        self.elementClick(self._signInBTN,"xpath")
        self.driver.implicitly_wait(5)
        return True

    """Method for verify user is logged in or not"""
    def verifyLoggedinUser(self):
        signOutLink = self.getElement(self._signOutLink,"id")
        self.mouseHover(self._signInMenu, "xpath")
        assert signOutLink.is_displayed(),"Login is not successfull"
        print("User is loggedin")

    """Method for search the product"""
    def searchProduct(self,searchKey):
        self.sendKeys(searchKey,self._searchInput,"id")
        self.driver.implicitly_wait(5)
        self.elementClick(self._searchBTN,"xpath")
        self.driver.implicitly_wait(5)

    """Method for go to the cart page by click on the cart link"""
    def goToCart(self):
        self.elementClick(self._cartId,"id")
        self.driver.implicitly_wait(10)
        return True

    """Method for go to the Western Wear Listing"""
    def goToWesternWear(self):
        self.mouseHover(self._shopByCaIid,"id")
        self.driver.implicitly_wait(5)
        self.mouseHover(self._submenuWomen, "xpath")
        self.driver.implicitly_wait(5)
        self.elementClick(self._subCatLinkWomen, "xpath")
        self.driver.implicitly_wait(5)
        return True

    """Method for go to the Amazon Echo listing"""
    def goToAmazonEcho(self):
        self.mouseHover(self._shopByCaIid, "id")
        self.driver.implicitly_wait(5)
        self.mouseHover(self._submenuAlexa,"xpath")
        self.driver.implicitly_wait(5)
        self.elementClick(self._subCatLinkAlexa, "xpath")
        self.driver.implicitly_wait(5)
        return True

    """Method for go to the Mobile Phones Listing"""
    def goToMobilePhones(self):
        self.mouseHover(self._shopByCaIid, "id")
        self.driver.implicitly_wait(5)
        self.mouseHover(self._submenuMobiles, "xpath")
        self.driver.implicitly_wait(5)
        self.elementClick(self._subCatLinkMobiles, "xpath")
        self.driver.implicitly_wait(5)
        return True

    """Method for Logout"""
    def logout(self):
        self.mouseHover(self._signInMenu, "xpath")
        self.driver.implicitly_wait(5)
        self.elementClick(self._signOutLink,"id")

