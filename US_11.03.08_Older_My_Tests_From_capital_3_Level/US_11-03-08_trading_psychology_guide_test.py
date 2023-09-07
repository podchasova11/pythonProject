from datetime import datetime
import allure
import pytest

from pages.Elements.BlockStepTrading import BlockStepTrading
from pages.Elements.ButtonStartTradingMainBanner import MainBannerStartTrading
from pages.Elements.ButtonTradeOnWidgetMostTraded import ButtonTradeOnWidgetMostTraded
from pages.Elements.ButtonTryDemoMainBanner import MainBannerTryDemo
from pages.Menu.menu import MenuSection
from pages.Elements.AssertClass import AssertClass
from tests.build_dynamic_arg import build_dynamic_arg_v2
from pages.conditions import Conditions
from src.src import CapitalComPageSrc


@pytest.fixture()
def cur_time():
    """Fixture"""
    return str(datetime.now())


@pytest.mark.us_11_03_08
class TestTradingPsychologyGuide:
    page_conditions = None

    @allure.step("Start test_11.03.08_01 button [Start Trading] on Main banner")
    def test_11_03_08_01_main_banner_start_trading_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            prob_run_tc, cur_time):
        """
        Check: Button [Start Trading]
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.03.08_01:")
        print(f"\n{datetime.now()}   {self.__dict__}")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.03.08", "Education > Menu item [Trading Psychology Guide]",
                             "01", "Testing button [Start Trading] on Main banner")

        if cur_language != "":
            pytest.skip("This test-case only for english language")

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        link = page_menu.sub_menu_trading_psychology_guide_move_focus_click(d, cur_language)

        test_element = MainBannerStartTrading(d, link)
        test_element.arrange_(d, link)

        test_element.element_click()

        test_element = AssertClass(d, link)
        match cur_role:
            case "NoReg" | "Reg/NoAuth":
                test_element.assert_signup(d, cur_language, link)
            case "Auth":
                test_element.assert_trading_platform_v2(d, link)

    @allure.step("Start test_11.03.08_02 Click button [Try demo] on Main banner")
    def test_11_03_08_02_main_banner_try_demo_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            prob_run_tc, cur_time):
        """
        Check: Button [Try demo]
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.03.08_02:")
        print(f"\n{datetime.now()}   {self.__dict__}")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.03.08", "Education > Menu item [Trading Psychology Guide]",
                             "02", "Testing button [Try demo] on Main banner")

        if cur_language != "":
            pytest.skip("This test-case only for english language")

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        link = page_menu.sub_menu_trading_psychology_guide_move_focus_click(d, cur_language)

        test_element = MainBannerTryDemo(d, link)
        test_element.arrange_(d, link)

        test_element.element_click()

        test_element = AssertClass(d, link)
        match cur_role:
            case "NoReg" | "Reg/NoAuth":
                test_element.assert_signup(d, cur_language, link)
            case "Auth":
                test_element.assert_trading_platform_v2(d, link)

    @allure.step("Start test_11.03.08_03 Click buttons [Trade] in Widget Most traded block")
    def test_11_03_08_03_most_traded_trade_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            prob_run_tc, cur_time):
        """
        Check: Button [Trade] in Most traded block
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.03.08_03:")
        print(f"\n{datetime.now()}   {self.__dict__}")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.03.08", "Education > Menu item [Trading Psychology Guide]",
                             "03", "Testing button [Trade] in Most traded block")

        if cur_language != "":
            pytest.skip("This test-case only for english language")

        if cur_country == 'gb':
            pytest.skip("This test is not supported on UK location")

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        link = page_menu.sub_menu_trading_psychology_guide_move_focus_click(d, cur_language)

        test_element = ButtonTradeOnWidgetMostTraded(d, link)
        test_elements_list = test_element.arrange_v2_()
        for index, element in enumerate(test_elements_list):
            print(f"\n{datetime.now()}   Testing element #{index + 1}")
            if not test_element.element_click_v2(element):
                pytest.fail("Testing element is not clicked")
            check_element = AssertClass(d, link)
            match cur_role:
                case "NoReg":
                    check_element.assert_signup(d, cur_language, link)
                case "Reg/NoAuth":
                    check_element.assert_login(d, link)
                case "Auth":
                    check_element.assert_trading_platform_v2(d, link)

    @allure.step("Start test_11.03.08_04 button [Create_verify_your_account] in block [Steps trading].")
    def test_11_03_08_04_create_verify_your_account(
            self, worker_id, d, cur_language, cur_country, cur_role,
            cur_login, cur_password, prob_run_tc, cur_time):
        """
        Check: Button [Create_verify_your_account] in block [Steps trading]
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.03.08_04:")
        print(f"\n{datetime.now()}   {self.__dict__}")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.03.08", "Education > Menu item [Trading Psychology Guide]",
                             "04", "Testing button [Create_verify_your_account] in block [Steps trading]")

        if cur_language != "":
            pytest.skip("This test-case only for english language")

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        link = page_menu.sub_menu_trading_psychology_guide_move_focus_click(d, cur_language)

        test_element = BlockStepTrading(d, link)
        test_element.arrange_(d, link)
        test_element.element_click()

        test_element = AssertClass(d, link)
        match cur_role:
            case "NoReg" | "Reg/NoAuth":
                test_element.assert_signup(d, cur_language, link)
            case "Auth":
                test_element.assert_trading_platform_v2(d, link)