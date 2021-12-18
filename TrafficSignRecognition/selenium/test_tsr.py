from selenium import webdriver
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager




class TestTSR():

    @pytest.fixture()
    def setup(self):
        #self.driver = webdriver.Chrome=webdriver.Chrome(ChromeDriverManager().install())
        self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        self.driver.maximize_window()
        yield
        self.driver.close()


    

    
    def test_homePageTitle(self,setup):
        self.driver.get("http://localhost:8000/")
        assert self.driver.title=="Traffic sign Detection"

    

        