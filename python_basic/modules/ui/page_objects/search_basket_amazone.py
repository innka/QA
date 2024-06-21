from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

class Search_Amazone(BasePage):
    URL = "https://www.amazon.fr/"

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(Search_Amazone.URL)

    def try_empty_search(self):
        search_elem = self.driver.find_element(By.NAME,"field-keywords")
        search_elem.send_keys("")
        btn_search = self.driver.find_element(By.ID, "nav-search-submit-button")
        btn_search.click()

    def try_search(self, param):
        search_elem = self.driver.find_element(By.NAME,"field-keywords")
        search_elem.send_keys(param)
        btn_search = self.driver.find_element(By.ID, "nav-search-submit-button")
        btn_search.click()

    def choose_smth_from_search(self):
        text = "MULEVIP Lampe UV Ongles Gel 180W Lampe UV Lampe LED Ongle,Lampe UV LED Machine UV Led pour Ongles 4 Minuteries 10s/30s/60s/99s, avec Mini Lampe UV Ongles Gel,Base Amovible, pour Toutes Les Gels"
        #text = "Dyson Cool AM07 Ventilateur avec télécommande 100 cm, minuterie 9 h, ventilateur tour silencieux blanc/argent, économie d'énergie, ventilateur sur pied, ventilateur sur pied"
        search_elem = self.driver.find_element(By.LINK_TEXT,text)
        search_elem.click()

    def add_to_basket(self):
        btn_add = self.driver.find_element(By.NAME, "submit.addToCart")
        btn_add.click()

    def go_to_basket(self):
        btn_basket = self.driver.find_element(By.LINK_TEXT, "Aller au panier")
        btn_basket.click()

    def finish_command(self):
        btn_finish_command = self.driver.find_element(By.NAME, "proceedToRetailCheckout")
        btn_finish_command.click()
    

    def check_title(self, expected_title):
        return self.driver.title == expected_title
    
