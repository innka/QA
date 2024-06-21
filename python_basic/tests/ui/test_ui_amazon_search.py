import pytest
import time
from modules.ui.page_objects.search_basket_amazone import Search_Amazone
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
#метод пошуку елементів за певними атрибутами
from selenium.webdriver.common.by import By
"""
@pytest.mark.idv_project6
def test_empty_search_page_object():
    search = Search_Amazone()

    search.go_to()

    search.try_empty_search()

    assert search.check_title("Amazon.fr : livres, DVD, jeux vidéo, musique, high-tech, informatique, jouets, vêtements, chaussures, sport, bricolage, maison, beauté, puériculture, épicerie et plus encore !")
    #time.sleep(3)
    search.close()

@pytest.mark.idv_project6
def test_search_with_param_page_object():
    search = Search_Amazone()

    search.go_to()

    search.try_search("dyson cool")

    assert search.check_title("Amazon.fr : dyson cool")
    #time.sleep(3)
    search.close()


@pytest.mark.idv_project6
def test_search_with_param_and_choose_smth_page_object():
    search = Search_Amazone()

    search.go_to()

    search.try_search("Lampe UV Ongles")
    search.choose_smth_from_search()
    search.add_to_basket()

    title = "Amazon.fr Panier"
    assert search.check_title(title)
    #time.sleep(5)
    search.close()

@pytest.mark.idv_project6
def test_check_basket_with_smth():
    search = Search_Amazone()

    search.go_to()

    search.try_search("Lampe UV Ongles")
    search.choose_smth_from_search()
    search.add_to_basket()
    search.go_to_basket()
    #time.sleep(3)
    title = "Amazon.fr Panier"
    assert search.check_title(title)
    search.close()
"""
@pytest.mark.idv_project6
def test_check_basket_with_smth():
    search = Search_Amazone()

    search.go_to()

    search.try_search("Lampe UV Ongles")
    search.choose_smth_from_search()
    search.add_to_basket()
    search.go_to_basket()
    search.finish_command()
    time.sleep(3)
    title = "Connexion Amazon"
    assert search.check_title(title)
    search.close()