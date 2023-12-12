from selenium import webdriver
import pytest
import conftest
from pages.home_page import HomePage
from pages.advertise_page import AdvertisePage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.test1
class TestCT01:
    def test_ct01_request_media_kit(self):
        driver = conftest.driver
        home_page = HomePage()
        advertise_page = AdvertisePage()
        home_page.nav_to_advertise()
        advertise_page.fill_media_form()
        advertise_page.assert_send()
