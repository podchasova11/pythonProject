import pytest
import allure
from datetime import datetime

from tests.build_dynamic_arg import build_dynamic_arg_v2
from pages.conditions import Conditions
from pages.Menu.menu import MenuSection
from pages.Elements.AssertClass import AssertClass
from pages.Elements.HeaderButtonLogin import HeaderButtonLogin
from pages.Elements.HeaderButtonTrade import HeaderButtonTrade
from pages.Elements.ButtonStartTradingMainBanner import MainBannerStartTrading
# from pages.Elements.ButtonTryDemoMainBanner import MainBannerTryDemo
# from pages.Elements.testing_elements_locators import ButtonTradeOnWidgetMostTradedLocators
# from pages.Elements.ButtonTradeOnWidgetMostTraded import ButtonTradeOnWidgetMostTraded
# from pages.Elements.ButtonDownloadAppStore import ButtonDownloadAppStore
# from pages.Elements.ButtonGetItOnGooglePlay import ButtonGetItOnGooglePlay
# from pages.Elements.ButtonExploreWebPlatform import ButtonExploreWebPlatform
# from pages.Elements.BlockStepTrading import BlockStepTrading
from src.src import CapitalComPageSrc


@pytest.mark.us_11_03_03
class TestTrendTrading:
    page_conditions = None

    @allure.step("Start test of button [Log in] in the Header")
    def test_01_header_button_login(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            prob_run_tc):
        """
        Check: Button [Log In]
        Language: All. License: All.
        """
        print(f"\n\n{datetime.now()}   Работает obj {self} с именем TC_11.03.03_01")

        link = build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                                    "11.03.03", "Education > Menu item [Trend Trading]",
                                    "01", "Testing button [Log In] in the Header")

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        link = page_menu.sub_menu_trend_trading_move_focus_click(d, cur_language)

        test_element = HeaderButtonLogin(d, link)
        test_element.arrange_(d, cur_role, link)

        if not test_element.element_click():
            pytest.fail("Testing element is not clicked")

        test_element = AssertClass(d, link)
        test_element.assert_login(d, cur_language, link)

    @allure.step("Start test of button [Sign up] in the Header")
    def test_02_header_button_signup(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc):
        """
        Check: Button [Sign up]
        Language: All. License: All.
        """
        print(f"\n\n{datetime.now()}  Работает obj {self} с именем TC_11.03.03_02")

        link = build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                                    "11.03.03", "Education > Menu item [Trend Trading]",
                                    "02", "Testing button [Sign up] in the Header")

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        link = page_menu.sub_menu_trend_trading_move_focus_click(d, cur_language)

        test_element = HeaderButtonTrade(d, link)
        test_element.arrange_(d, cur_role, link)

        if not test_element.element_click():
            pytest.fail("Testing element is not clicked")

        test_element = AssertClass(d, link)
        test_element.assert_signup(d, cur_language, link)

    @allure.step("Start test of button [Start Trading] on the Main banner 'What is trend trading?'")
    def test_03_button_start_trading_main_banner(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc):
        """
        Check: Button [Start Trading]
        Language: All. License: All.
        """
        print(f"\n\n{datetime.now()}  Работает obj {self} с именем TC_11.03.03_03")

        link = build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                                    "11.03.03",
                                    "Education > Menu item [Trend Trading]",
                                    "02",
                                    "Testing button [Start Trading] in the Main banner 'What is trend trading?'")

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        link = page_menu.sub_menu_trend_trading_move_focus_click(d, cur_language)

        test_element = MainBannerStartTrading(d, link)
        test_element.arrange_(d, link)

        if not test_element.element_click():
            pytest.fail("Testing element is not clicked")

        test_element = AssertClass(d, link)
        match cur_role:
            case "NoReg":
                test_element.assert_signup(d, cur_language, link)
            case "Reg/NoAuth":
                test_element.assert_login(d, cur_language, link)
            case "Auth":
                test_element.assert_trading_platform_v2(d, link)
