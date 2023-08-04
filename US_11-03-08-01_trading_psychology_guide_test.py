import pytest
import allure
from datetime import datetime

from pages.Elements.ButtonStartTradingMainBanner import MainBannerStartTrading
from pages.Elements.ButtonTradeOnWidgetMostTraded import ButtonTradeOnWidgetMostTraded
from pages.Elements.ButtonTryDemoMainBanner import MainBannerTryDemo
from pages.conditions import Conditions
from src.src import CapitalComPageSrc
from tests.build_dynamic_arg import build_dynamic_arg_v2
from pages.Elements.AssertClass import AssertClass

count = 1


def pytest_generate_tests(metafunc):
    """
    Fixture generation test data
    """
    if "cur_item_link" in metafunc.fixturenames:
        name_file = "tests/US_11_Education/US_11-03-08_Trading_Psychology_Guide/list_of_href.txt"

        list_item_link = list()
        try:
            file = open(name_file, "r")
        except FileNotFoundError:
            print(f"{datetime.now()}   There is no file with name {name_file}!")
        else:
            for line in file:
                list_item_link.append(line[:-1])
            file.close()

        if len(list_item_link) == 0:
            pytest.skip("Отсутствуют тестовые данные: отсутствует список ссылок на страницы")

        metafunc.parametrize("cur_item_link", list_item_link, scope="class")


@pytest.fixture()
def cur_time():
    """Fixture"""
    return str(datetime.now())


class TestTradingPsychologyGuideItem:
    page_conditions = None

    @allure.step("Start test_11.03.08_01 Click button [Start trading] on Main banner")
    def test_01_main_banner_start_trading_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc):
        """
        Check: Button [Start Trading] on Main banner
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.03.08_01")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.03.08", "Educations > Menu item [Trading Psychology Guide]",
                             "01", "Testing button [Start Trading] on Main banner")

        if cur_language not in [""]:
            pytest.skip(f"Test-case not for '{cur_language}' language")

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = MainBannerStartTrading(d, cur_item_link)
        test_element.arrange_(d, cur_item_link)

        test_element.element_click()

        test_element = AssertClass(d, cur_item_link)
        match cur_role:
            case "NoReg" | "Reg/NoAuth":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v2(d, cur_item_link, True)

    @allure.step("Start test_11.03.08_02 Click button [Try demo] on Main banner")
    def test_02_main_banner_try_demo_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc):
        """
        Check: Button [Try demo] on Main banner
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.03.08_02")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.03.08", "Educations > Menu item [Trading Psychology Guide]",
                             "02", "Testing button [Try demo] on Main banner")

        if cur_language not in [""]:
            pytest.skip(f"Test-case not for '{cur_language}' language")

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = MainBannerTryDemo(d, cur_item_link)
        test_element.arrange_(d, cur_item_link)

        test_element.element_click()

        test_element = AssertClass(d, cur_item_link)
        match cur_role:
            case "NoReg" | "Reg/NoAuth":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v2(d, cur_item_link, True)

    @allure.step("Start test_11.03.08_03 Click buttons [Trade] in Widget Most traded block")
    def test_03_most_traded_trade_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc):
        """
        Check: Button [Trade] in Most traded block
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.03.08_03")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.03.08", "Educations > Menu item [Trading Psychology Guide]",
                             "03", "Testing button [Trade] in Most traded block")

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        if cur_country == "gb":
            pytest.skip("This test-case not for FCA licence")

        test_element = ButtonTradeOnWidgetMostTraded(d, cur_item_link)
        test_elements_list = test_element.arrange_v2_()
        for index, element in enumerate(test_elements_list):
            print(f"\n{datetime.now()}   Testing element #{index + 1}")
            if not test_element.element_click_v2(element):
                pytest.fail("Testing element is not clicked")
            check_element = AssertClass(d, cur_item_link)
            match cur_role:
                case "NoReg":
                    check_element.assert_signup(d, cur_language, cur_item_link)
                case "Reg/NoAuth":
                    check_element.assert_login(d, cur_language, cur_item_link)
                case "Auth":
                    check_element.assert_trading_platform_v2(d, cur_item_link)
