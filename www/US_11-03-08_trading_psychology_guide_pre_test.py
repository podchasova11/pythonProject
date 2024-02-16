"""
-*- coding: utf-8 -*-
@Time    : 2023/09/06 18:10
@Author  : Mila Podchasova
"""
import allure
import pytest
import random  # for new method
from datetime import datetime

import conf
from pages.Education.Trading_psychology_guide_locators import TradingPsychologyContentList
from pages.Menu.menu import MenuSection
from tests.build_dynamic_arg import build_dynamic_arg_v2
from pages.conditions import Conditions
from src.src import CapitalComPageSrc

count = 1


class TestTradingPsychologyGuidePretest:
    page_conditions = None

    @allure.step("Start test_11.03.08_00 pretest")
    def test_trading_psychology_guide_pretest(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc):
        global count

        print(f"\n\n{datetime.now()}   Работает obj {self} с именем TC_11.03.08_00")

        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.03.08", "Education > Menu item [Trading Psychology Guide]",
                             "00", "Pretest")

        if count == 0:
            pytest.skip("Так надо")

        if cur_language not in [""]:
            pytest.skip(f"Test-case not for '{cur_language}' language")

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        page_menu.sub_menu_trading_psychology_guide_move_focus_click(d, cur_language)
        del page_menu

        # Записываем ссылки в файл
        name_file = "tests/US_11_Education/US_11-03-08_Trading_Psychology_Guide/list_of_href.txt"
        list_items = d.find_elements(*TradingPsychologyContentList.LISTS)
        count_in = len(list_items)
        print(f"{datetime.now()}   Trading Psychology Guide page include {count_in} lists item(s)")  # for new method
        file = None

        try:
            file = open(name_file, "w")
            count_out = 0
            if count_in > 0:
                for i in range(conf.QTY_LINKS):
                    if i < count_in:
                        k = random.randint(1, count_in)
                        item = list_items[k - 1]
                        file.write(item.get_property("href") + "\n")
                        count_out += 1

            file.write(d.current_url + "\n")  # для добавления головной страницы
            count_in += 1  # для добавления головной страницы
            count_out += 1  # для добавления головной страницы
            print(f"{datetime.now()}   Plus 1 main page Trading Psychology Guide. Total: {count_in} for testing")

        finally:
            file.close()
            del file

        print(f"{datetime.now()}   Test data include {count_out} item(s)")
        if count_in != 0:
            print(f"{datetime.now()}   The test coverage = {count_out/count_in*100} %")
        else:
            print(f"{datetime.now()}   The test coverage = 0 %")

        count -= 1










import allure
import pytest
from datetime import datetime

from pages.Elements.ButtonBuyInContentBlock import BuyButtonContentBlock
from pages.Elements.ButtonDownloadAppStore import ButtonDownloadAppStore
from pages.Elements.ButtonExploreWebPlatform import ButtonExploreWebPlatform
from pages.Elements.ButtonGetItOnGooglePlay import ButtonGetItOnGooglePlay
from pages.Elements.ButtonSellInContentBlock import SellButtonContentBlock
from pages.Elements.ButtonStartTradingMainBanner import MainBannerStartTrading
from pages.Elements.ButtonTradeOnWidgetMostTraded import ButtonTradeOnWidgetMostTraded
from pages.Elements.ButtonTryDemoMainBanner import MainBannerTryDemo
from pages.common import Common
from tests.build_dynamic_arg import build_dynamic_arg_v2
from pages.Menu.menu import MenuSection
from pages.conditions import Conditions
from pages.Elements.BlockStepTrading import BlockStepTrading
from pages.Elements.AssertClass import AssertClass
from src.src import CapitalComPageSrc


@pytest.fixture()
def cur_time():
    return str(datetime.now())


count = 1


def pytest_generate_tests(metafunc):
    """
    Fixture generation test data
    """
    if "cur_item_link" in metafunc.fixturenames:
        name_file = "tests/US_11_Education/US_11-03-01_trading_strategies_guide/list_of_href.txt"

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


@pytest.mark.us_11_03_01
class TestTradingStrategiesGuides:

    page_conditions = None

    @allure.step("Start test_11.03.01_01 of button [Start Trading] on Main banner")
    def test_01_main_banner_start_trading_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc):
        """
        Check: Button [Start Trading]
        Language: "", "de", "es", "it". License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.03.01_01")

        link = build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                                    "11.03.01",
                                    "Education > Menu item [Trading Strategies Guides]",
                                    "01",
                                    "Testing button [Start Trading] on Main banner")

        if cur_language not in ["", "de", "es", "it"]:
            Common().skip_test_for_language(cur_language)

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        link = page_menu.sub_menu_trading_strategies_guide_move_focus_click(d, cur_language)

        test_element = MainBannerStartTrading(d, cur_item_link)
        test_element.arrange_(d, cur_item_link)
        test_element.element_click()

        test_element = AssertClass(d, cur_item_link)

        match cur_role:
            case "NoReg":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "Reg/NoAuth":
                test_element.assert_login(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v2(d, cur_item_link)

    @allure.step("Start test_11.03.01_02 of button [Try demo] on Main banner")
    def test_02_main_banner_try_demo_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc):
        """
        Check: Button [Try demo] on Main banner
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.03.01_02")

        link = build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                                    "11.03.01",
                                    "Education > Menu item [Trading Strategies Guides]",
                                    "02",
                                    "Testing button [Try demo] on Main banner")

        if cur_language not in ["", "de", "es", "it"]:
            Common().skip_test_for_language(cur_language)

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        link = page_menu.sub_menu_trading_strategies_guide_move_focus_click(d, cur_language)

        test_element = MainBannerTryDemo(d, cur_item_link)
        test_element.arrange_(d, cur_item_link)
        test_element.element_click()

        test_element = AssertClass(d, cur_item_link)
        match cur_role:
            case "NoReg":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "Reg/NoAuth":
                test_element.assert_login(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v2(d, cur_item_link, True)

    @allure.step("Start test of buttons [Trade] in Most traded block")
    def test_03_most_traded_trade_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc):
        """
        Check: Button [Trade] in Most traded block
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.03.01_03")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.03.01",
                             "Education > Menu item [Trading Strategies Guides]",
                             "03",
                             "Testing button [Trade] in Most traded block")

        if cur_country == 'gb':
            pytest.skip("This test is not supported on UK location")

        if cur_language not in ["", "de", "es", "it"]:
            Common().skip_test_for_language(cur_language)

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        link = page_menu.sub_menu_trading_strategies_guide_move_focus_click(d, cur_language)

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

    @allure.step("Start test of button [Download on the App Store] in Block 'Sign up and trade smart today!'")
    def test_06_button_download_on_the_app_store(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc):
        """
        Check: Button [Download on the App Store] in Block "Sign up and trade smart today!"
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.03.01_06")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.03.01", "Education > Menu item [Trading Strategies Guides]",
                             "06",
                             "Test button [Download on the App Store] in Block \"Sign up and trade smart today!\"")

        if cur_language not in ["", "de", "es", "it"]:
            Common().skip_test_for_language(cur_language)

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        link = page_menu.sub_menu_trading_strategies_guide_move_focus_click(d, cur_language)

        test_element = ButtonDownloadAppStore(d, cur_item_link)
        test_element.arrange_(cur_item_link)
        if not test_element.element_click():
            pytest.fail("Testing element is not clicked")
        test_element = AssertClass(d, cur_item_link)
        test_element.assert_app_store(d, cur_item_link)

    @allure.step("Start test of button [Get it on Google Play] in Block 'Sign up and trade smart today!'")
    def test_07_button_get_it_on_google_play(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc):
        """
        Check: Button [Get it on Google Play] in Block "Sign up and trade smart today!"
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.03.01_07")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.03.01",
                             "Education > Menu item [Trading Strategies Guides]",
                             "07",
                             "Test button [Get it on Google Play] in Block \"Sign up and trade smart today!\"")

        if cur_language not in ["", "de", "es", "it"]:
            Common().skip_test_for_language(cur_language)

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        # page_menu = MenuSection(d, link)
        # page_menu.menu_education_move_focus(d, cur_language)
        # link = page_menu.sub_menu_trading_strategies_guide_move_focus_click(d, cur_language)

        test_element = ButtonGetItOnGooglePlay(d, cur_item_link)
        test_element.arrange_(cur_item_link)
        if not test_element.element_click():
            pytest.fail("Testing element is not clicked")

        test_element = AssertClass(d, cur_item_link)
        test_element.assert_google_play(d, cur_item_link)

    @allure.step("Start test of button [Explore Web Platform] in Block 'Sign up and trade smart today!'")
    def test_08_button_explore_web_platform(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc):
        """
        Check: Button [Explore Web Platform] in Block "Sign up and trade smart today!"
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.03.01_08")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.03.01",
                             "Education > Menu item [Trading Strategies Guides]",
                             "08",
                             "Testing button [Explore Web Platform] in Block \"Sign up and trade smart today!\"")

        if cur_language not in ["", "de", "es", "it"]:
            Common().skip_test_for_language(cur_language)

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        # page_menu = MenuSection(d, link)
        # page_menu.menu_education_move_focus(d, cur_language)
        # link = page_menu.sub_menu_trading_strategies_guide_move_focus_click(d, cur_language)

        test_element = ButtonExploreWebPlatform(d, cur_item_link)
        test_element.arrange_(cur_item_link)
        if not test_element.element_click():
            pytest.fail("Testing element is not clicked")

        test_element = AssertClass(d, cur_item_link)
        match cur_role:
            case "NoReg":
                test_element.assert_signup_form_on_the_trading_platform(d)
            case "Reg/NoAuth":
                test_element.assert_login_form_on_the_trading_platform(d)
            case "Auth":
                test_element.assert_trading_platform_v2(d, cur_item_link)

    @allure.step("Start test_11.03.01_09 button 'Create_verify_your_account' on the page.")
    def test_11_03_01_09_create_verify_your_account(
            self, worker_id, d, cur_language, cur_country, cur_role,
            cur_login, cur_password, cur_item_link, prob_run_tc, cur_time):
        """
        Check: Header -> button [Log In]
        Language: En. License: FCA.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.03.01_09")
        print(f"\n{datetime.now()}   {self.__dict__}")
        link = build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                                    "11.03.01",
                                    "Education > Menu item [Trading Strategies Guides]",
                                    "09",
                                    "Testing button [1. Create your account] in block [Steps trading]")

        if cur_language not in ["", "de", "es", "it", "cn"]:
            Common().skip_test_for_language(cur_language)

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        # page_menu = MenuSection(d, link)
        # page_menu.menu_education_move_focus(d, cur_language)
        # link = page_menu.sub_menu_trading_strategies_guide_move_focus_click(d, cur_language)

        test_element = BlockStepTrading(d, cur_item_link)
        test_element.arrange_(d, cur_item_link)
        test_element.element_click()

        test_element = AssertClass(d, cur_item_link)
        match cur_role:
            case "NoReg" | "Reg/NoAuth":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v2(d, cur_item_link)

    @allure.step("Start test of button [Sell] in Banner [Trading Instrument]")
    def test_11_03_01_10_button_sell(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            cur_item_link, prob_run_tc):
        """
        Check: Button [Sell] in Banner "Trading Instrument"
        Language: En. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.03.01_10")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.03.01", "Education > Menu item [Trading Strategies Guides]",
                             "10", "Testing button [Sell] in Banner [Trading Instrument]")

        if cur_country == 'gb':
            pytest.skip("This test is not supported on UK location")

        if cur_language not in [""]:
            Common().skip_test_for_language(cur_language)

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = SellButtonContentBlock(d, cur_item_link)
        test_element.arrange_(d, cur_item_link)

        test_element.element_click(cur_role)

        test_element = AssertClass(d, cur_item_link)
        match cur_role:
            case "NoReg":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "Reg/NoAuth":
                test_element.assert_login(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v2(d, cur_item_link)

    @allure.step("Start test of button [Buy] in Banner [Trading Instrument]")
    def test_11_03_01_11_button_buy(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            cur_item_link, prob_run_tc):
        """
        Check: Button [Buy] in Banner [Trading Instrument]
        Language: En. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.03.01_11")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.03.01", "Education > Menu item [Trading Strategies Guides]",
                             "11", "Testing button [Buy] in Banner [Trading Instrument]")

        if cur_country == 'gb':
            pytest.skip("This test is not supported on UK location")

        if cur_language not in [""]:
            Common().skip_test_for_language(cur_language)

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = BuyButtonContentBlock(d, cur_item_link)
        test_element.arrange_(d, cur_item_link)

        test_element.element_click(cur_role)

        test_element = AssertClass(d, cur_item_link)
        match cur_role:
            case "NoReg":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "Reg/NoAuth":
                test_element.assert_login(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v2(d, cur_item_link)
