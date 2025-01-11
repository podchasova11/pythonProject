# from datetime import datetime
# from pages.Elements.ButtonStartTradingMainBanner import MainBannerStartTrading
# from pages.Elements.ButtonTradeOnWidgetMostTraded import ButtonTradeOnWidgetMostTraded
# from pages.Elements.ButtonTryDemoMainBanner import MainBannerTryDemo
# from pages.conditions import Conditions
# from src.src import CapitalComPageSrc
# from tests.build_dynamic_arg import build_dynamic_arg_v2
# from pages.Elements.AssertClass import AssertClass
#
# count = 1
#
#
# def pytest_generate_tests(metafunc):
#     """
#     Fixture generation test data
#     """
#     if "cur_item_link" in metafunc.fixturenames:
#         name_file = "tests/US_11_Education/US_11-03-08_Trading_Psychology_Guide/list_of_href.txt"
#
#         list_item_link = list()
#         try:
#             file = open(name_file, "r")
#         except FileNotFoundError:
#             print(f"{datetime.now()}   There is no file with name {name_file}!")
#         else:
#             for line in file:
#                 list_item_link.append(line[:-1])
#             file.close()
#
#         if len(list_item_link) == 0:
#             pytest.skip("Отсутствуют тестовые данные: отсутствует список ссылок на страницы")
#
#         metafunc.parametrize("cur_item_link", list_item_link, scope="class")
#
#
# @pytest.mark.us_11_03_08
# class TestTradingPsychologyGuideItem:
#     page_conditions = None
#
#     @allure.step("Start test_11.03.08_01 Click button [Start trading] on Main banner")
#     def test_01_main_banner_start_trading_button(
#             self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
#             prob_run_tc):
#         """
#         Check: Button [Start Trading] on Main banner
#         Language: All. License: All.
#         """
#         print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.03.08_01")
#         build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
#                              "11.03.08", "Education > Menu item [Trading Psychology Guide]",
#                              "01", "Testing button [Start Trading] on Main banner")
#
#         if cur_language not in [""]:
#             pytest.skip(f"Test-case not for '{cur_language}' language")
#
#         page_conditions = Conditions(d, "")
#         page_conditions.preconditions(
#             d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)
#
#         test_element = MainBannerStartTrading(d, cur_item_link)
#         test_element.arrange_(d, cur_item_link)
#
#         test_element.element_click()
#
#         test_element = AssertClass(d, cur_item_link)
#         match cur_role:
#             case "NoReg" | "Reg/NoAuth":
#                 test_element.assert_signup(d, cur_language, cur_item_link)
#             case "Auth":
#                 test_element.assert_trading_platform_v2(d, cur_item_link, True)
#
#     @allure.step("Start test_11.03.08_02 Click button [Try demo] on Main banner")
#     def test_02_main_banner_try_demo_button(
#             self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
#             prob_run_tc):
#         """
#         Check: Button [Try demo] on Main banner
#         Language: All. License: All.
#         """
#         print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.03.08_02")
#         build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
#                              "11.03.08", "Education > Menu item [Trading Psychology Guide]",
#                              "02", "Testing button [Try demo] on Main banner")
#
#         if cur_language not in [""]:
#             pytest.skip(f"Test-case not for '{cur_language}' language")
#
#         page_conditions = Conditions(d, "")
#         page_conditions.preconditions(
#             d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)
#
#         test_element = MainBannerTryDemo(d, cur_item_link)
#         test_element.arrange_(d, cur_item_link)
#
#         test_element.element_click()
#
#         test_element = AssertClass(d, cur_item_link)
#         match cur_role:
#             case "NoReg" | "Reg/NoAuth":
#                 test_element.assert_signup(d, cur_language, cur_item_link)
#             case "Auth":
#                 test_element.assert_trading_platform_v2(d, cur_item_link, True)
#
#     @allure.step("Start test_11.03.08_03 Click buttons [Trade] in Widget Most traded block")
#     def test_03_most_traded_trade_button(
#             self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
#             prob_run_tc):
#         """
#         Check: Button [Trade] in Most traded block
#         Language: All. License: All.
#         """
#         print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.03.08_03")
#         build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
#                              "11.03.08", "Education > Menu item [Trading Psychology Guide]",
#                              "03", "Testing button [Trade] in Most traded block")
#
#         if cur_country == "gb":
#             pytest.skip("This test-case not for FCA licence")
#
#         page_conditions = Conditions(d, "")
#         page_conditions.preconditions(
#             d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)
#
#         test_element = ButtonTradeOnWidgetMostTraded(d, cur_item_link)
#         test_elements_list = test_element.arrange_v2_()
#         for index, element in enumerate(test_elements_list):
#             print(f"\n{datetime.now()}   Testing element #{index + 1}")
#             if not test_element.element_click_v2(element):
#                 pytest.fail("Testing element is not clicked")
#             check_element = AssertClass(d, cur_item_link)
#             match cur_role:
#                 case "NoReg":
#                     check_element.assert_signup(d, cur_language, cur_item_link)
#                 case "Reg/NoAuth":
#                     check_element.assert_login(d, cur_language, cur_item_link)
#                 case "Auth":
#                     check_element.assert_trading_platform_v2(d, cur_item_link)
#
#     @allure.step("Start test_11.03.08_04 button [Create_verify_your_account] in block [Steps trading].")
#     def test_04_create_verify_your_account(
#             self, worker_id, d, cur_language, cur_country, cur_role,
#             cur_login, cur_password, cur_item_link, prob_run_tc, ):
#         """
#         Check: Button [Create_verify_your_account] in block [Steps trading]
#         Language: All. License: All.
#         """
#         print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.03.08_04:")
#         build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
#                              "11.03.08", "Education > Menu item [Trading Psychology Guide]",
#                              "04", "Testing button [Create_verify_your_account] in block [Steps trading]")
#
#         if cur_language != "":
#             pytest.skip("This test-case only for english language")
#
#         page_conditions = Conditions(d, "")
#         link = page_conditions.preconditions(
#             d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)
#
#         page_menu = MenuSection(d, link)
#         page_menu.menu_education_move_focus(d, cur_language)
#         link = page_menu.sub_menu_trading_psychology_guide_move_focus_click(d, cur_language)
#
#         test_element = BlockStepTrading(d, link)
#         test_element.arrange_(d, link)
#         test_element.element_click()
#
#         test_element = AssertClass(d, link)
#         match cur_role:
#             case "NoReg" | "Reg/NoAuth":
#                 test_element.assert_signup(d, cur_language, link)
#             case "Auth":
#                 test_element.assert_trading_platform_v2(d, link)

    # @allure.step("Start test of button [Practise for free] in content block")    НОВЫЙ ТЕСТ 11/09/23
    # def test_05(
    #         self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc):
    #     """
    #     Check: Button [Practise for free] in content block
    #     Language: All. License: All.
    #     """
    #     print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.03.08_05")
    #     build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
    #                          "11.03.08",
    #                          "Educations > Menu item [Trading Psychology Guide]",
    #                          "05",
    #                          "Testing button [Practise for free] in Content block")

    #     if cur_language not in [""]:
    #         pytest.skip(f"This test not for {cur_language} language")
    #     if cur_country == 'gb':
    #         pytest.skip("This test is not supported on UK location")

    #     menu_link = self.us_link.get_us_link(d, cur_language, cur_country, cur_role, cur_login, cur_password)

    #     test_element = ButtonPractiseForFreeInContentBlock(d, menu_link)
    #     test_element.arrange_(menu_link)

    #     if not test_element.element_click():
    #         pytest.fail("Testing element is not clicked")

    #     test_element = AssertClass(d, menu_link)
    #     match cur_role:
    #         case "NoReg":
    #             test_element.assert_signup(d, cur_language, menu_link)
    #         case "Reg/NoAuth":
    #             test_element.assert_login(d, cur_language, menu_link)
    #         case "Auth":
    #             test_element.assert_trading_platform_v2(d, menu_link)

#
# СТАРЫЕ ТЕСТЫ ОТ 13/09/2023
#
# import allure
# import pytest
# from datetime import datetime
#
# from pages.Elements.ButtonStartTradingMainBanner import MainBannerStartTrading
# from pages.Elements.ButtonTradeOnWidgetMostTraded import ButtonTradeOnWidgetMostTraded
# from pages.Elements.ButtonTryDemoMainBanner import MainBannerTryDemo
# from tests.build_dynamic_arg import build_dynamic_arg_v2
# from pages.Menu.menu import MenuSection
# from pages.conditions import Conditions
# from pages.Elements.HeaderButtonLogin import HeaderButtonLogin
# from pages.Elements.HeaderButtonTrade import HeaderButtonTrade
# from pages.Elements.BlockStepTrading import BlockStepTrading
# from pages.Elements.AssertClass import AssertClass
# from src.src import CapitalComPageSrc

#
# @pytest.fixture()
# def cur_time():
#     return str(datetime.now())
#
#
# @pytest.mark.us_11_03_01
# class TestTradingStrategiesGuides:
#
#     page_conditions = None
#
#     @allure.step("Start test_11.03.01_01 of button [Log in] on Header")
#     def test_11_03_01_01_header_button_login(
#             self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
#             prob_run_tc, cur_time):
#         """
#         Check: Button [Log In]
#         Language: All. License: All.
#         """
#         print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.03.01_01")
#
#         link = build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
#                                     "11.03.01", "Education > Menu Item [Trading Strategies Guides]",
#                                     "01", "Testing button [Log In] on Header")
#
#         page_conditions = Conditions(d, "")
#         page_conditions.preconditions(
#             d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)
#
#         page_menu = MenuSection(d, link)
#         page_menu.menu_education_move_focus(d, cur_language)
#         link = page_menu.sub_menu_trading_strategies_guide_move_focus_click(d, cur_language)
#
#         test_element = HeaderButtonLogin(d, link)
#         test_element.arrange_(d, cur_role, link)
#         test_element.element_click()
#         test_element = AssertClass(d, link)
#         test_element.assert_login(d, cur_language, link)
#
#     @allure.step("Start test_11.03.01_02 of button [Sign up] on Header")
#     def test_11_03_01_02_header_button_signup(
#             self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
#             prob_run_tc, cur_time):
#         """
#         Check: Button [Sign up]
#         Language: All. License: All.
#         """
#         print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.03.01_02")
#
#         link = build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
#                                     "11.03.01", "Education > Menu Item [Trading Strategies Guides]",
#                                     "02", "Testing button [Sign up] on Header")
#
#         page_conditions = Conditions(d, "")
#         page_conditions.preconditions(
#             d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)
#
#         page_menu = MenuSection(d, link)
#         page_menu.menu_education_move_focus(d, cur_language)
#         link = page_menu.sub_menu_trading_strategies_guide_move_focus_click(d, cur_language)
#
#         test_element = HeaderButtonTrade(d, link)
#         test_element.arrange_(d, cur_role, link)
#         test_element.element_click()
#
#         test_element = AssertClass(d, link)
#         test_element.assert_signup(d, cur_language, link)
#
#     @allure.step("Start test_11.03.01_03 of button [Start Trading] on Main banner")
#     def test_11_03_01_03_main_banner_start_trading_button(
#             self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
#             prob_run_tc, cur_time):
#         """
#         Check: Button [Start Trading]
#         Language: All. License: All.
#         """
#         print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.03.01_03")
#
#         link = build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
#                                     "11.03.01", "Education > Menu Item [Trading Strategies Guides]",
#                                     "03", "Testing button [Start Trading] on Main banner")
#
#         page_conditions = Conditions(d, "")
#         page_conditions.preconditions(
#             d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)
#
#         page_menu = MenuSection(d, link)
#         page_menu.menu_education_move_focus(d, cur_language)
#         link = page_menu.sub_menu_trading_strategies_guide_move_focus_click(d, cur_language)
#
#         test_element = MainBannerStartTrading(d, link)
#         test_element.arrange_(d, link)
#         test_element.element_click()
#
#         test_element = AssertClass(d, link)
#
#         match cur_role:
#             case "NoReg":
#                 test_element.assert_signup(d, cur_language, link)
#             case "Reg/NoAuth":
#                 test_element.assert_login(d, cur_language, link)
#             case "Auth":
#                 test_element.assert_trading_platform_v2(d, link)
#
#     @allure.step("Start test_11.03.01_04 of button [Try demo] on Main banner")
#     def test_11_03_01_04_main_banner_try_demo_button(
#             self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc):
#         """
#         Check: Button [Try demo] on Main banner
#         Language: All. License: All.
#         """
#         print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.03.01_04")
#
#         link = build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
#                                     "11.03.01", "Education > Menu Item [Trading Strategies Guides]",
#                                     "04", "Testing button [Try demo] on Main banner")
#
#         page_conditions = Conditions(d, "")
#         page_conditions.preconditions(
#             d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)
#
#         page_menu = MenuSection(d, link)
#         page_menu.menu_education_move_focus(d, cur_language)
#         link = page_menu.sub_menu_trading_strategies_guide_move_focus_click(d, cur_language)
#
#         test_element = MainBannerTryDemo(d, link)
#         test_element.arrange_(d, link)
#         test_element.element_click()
#
#         test_element = AssertClass(d, link)
#         match cur_role:
#             case "NoReg":
#                 test_element.assert_signup(d, cur_language, link)
#             case "Reg/NoAuth":
#                 test_element.assert_login(d, cur_language, link)
#             case "Auth":
#                 test_element.assert_trading_platform_v2(d, link)
#
#     @allure.step("Start test of buttons [Trade] in Most traded block")
#     def test_11_03_01_05_most_traded_trade_button(
#             self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc):
#         """
#         Check: Button [Trade] in Most traded block
#         Language: All. License: All.
#         """
#         print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.03.01_05")
#         build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
#                              "11.03.01", "Education > Menu Item [Trading Strategies Guides]",
#                              "05", "Testing button [Trade] in Most traded block")
#
#         page_conditions = Conditions(d, "")
#         link = page_conditions.preconditions(
#             d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)
#
#         page_menu = MenuSection(d, link)
#         page_menu.menu_education_move_focus(d, cur_language)
#         link = page_menu.sub_menu_trading_strategies_guide_move_focus_click(d, cur_language)
#
#         test_element = ButtonTradeOnWidgetMostTraded(d, link)
#         test_elements_list = test_element.arrange_v2_()
#         for index, element in enumerate(test_elements_list):
#             print(f"\n{datetime.now()}   Testing element #{index + 1}")
#             if not test_element.element_click_v2(element):
#                 pytest.fail("Testing element is not clicked")
#             check_element = AssertClass(d, link)
#             match cur_role:
#                 case "NoReg":
#                     check_element.assert_signup(d, cur_language, link)
#                 case "Reg/NoAuth":
#                     check_element.assert_login(d, cur_language, link)
#                 case "Auth":
#                     check_element.assert_trading_platform_v2(d, link)
#
#     @allure.step("Start test_11.03.01_06 button 'Create_verify_your_account' on the page.")
#     def test_11_03_01_06_create_verify_your_account(
#             self, worker_id, d, cur_language, cur_country, cur_role,
#             cur_login, cur_password, prob_run_tc, cur_time):
#         """
#         Check: Header -> button [Log In]
#         Language: En. License: FCA.
#         """
#         print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.03.01_06")
#         print(f"\n{datetime.now()}   {self.__dict__}")
#         link = build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
#                                     "11.03.01", "Education > Menu Item [Trading Strategies Guides]",
#                                     "06", "Testing button [1. Create your account] in block [Steps trading]")
#
#         page_conditions = Conditions(d, "")
#         page_conditions.preconditions(
#             d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)
#
#         page_menu = MenuSection(d, link)
#         page_menu.menu_education_move_focus(d, cur_language)
#         link = page_menu.sub_menu_trading_strategies_guide_move_focus_click(d, cur_language)
#
#         test_element = BlockStepTrading(d, link)
#         test_element.arrange_(d, link)
#         test_element.element_click()
#
#         test_element = AssertClass(d, link)
#         match cur_role:
#             case "NoReg" | "Reg/NoAuth":
#                 test_element.assert_signup(d, cur_language, link)
#             case "Auth":
#                 test_element.assert_trading_platform_v2(d, link)
#
#
