# import pytest
#
# from selenium import webdriver
#
#
# @pytest.fixture(scope="class")
# def init_driver(request):
#     request.cls.driver = webdriver.Chrome()
#
#     yield
#
#     request.cls.driver.quit()

import pytest
import logging as logger
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChOptions
from selenium.webdriver.firefox.options import Options as FFOptions


@pytest.fixture(scope="class")
def init_driver(request):
    supported_browsers = ['chrome', 'ch', 'headlesschrome', 'remote_chrome', 'firefox', 'ff', 'headlessfirefox',
                          'remote_firefox']

    browser = os.environ.get('BROWSER', None)
    if not browser:
        raise Exception("The environment variable 'BROWSER' must be set.")

    browser = browser.lower()

    if browser not in supported_browsers:
        raise Exception(f"Provided browser '{browser}' is not one of the supported."
                        f"Supported are: {supported_browsers}")

    if browser in ('chrome', 'ch'):
        driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
    elif browser in ('firefox', 'ff'):
        driver = webdriver.Firefox()
    elif browser in ('headlesschrome'):
        chrome_options = ChOptions()
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(options=chrome_options)
    elif browser == 'remote_chrome':
        chrome_remote_url = os.environ.get("REMOTE_WEBDRIVER")
        if not chrome_remote_url:
            raise Exception(f"If 'browser=remote_chrome' then 'REMOTE_WEBDRIVER' variable must be set.")
        chrome_options = ChOptions()
        chrome_options.add_argument('--ignore-ssl-errors=yes')
        chrome_options.add_argument('--ignore-certificate-errors')
        # driver = webdriver.Chrome()
        # http://selenium__standalone-chrome:4444/wd/hub
        driver = webdriver.Remote(
            command_executor=chrome_remote_url,
            options=chrome_options
        )
        # driver.get("http://demostore.supersqa.com")
        # logger.info(driver.title)
    elif browser == 'headlessfirefox':
        ff_options = FFOptions()
        ff_options.add_argument("--disable-gpu")
        ff_options.add_argument("--no-sandbox")
        ff_options.add_argument("--headless")
        driver = webdriver.Firefox(options=ff_options)

    logger.debug("############### BROWSER INFORMATION #####################")
    for k, v in driver.capabilities.items():
        logger.debug(f"{k}: {v}")
    logger.debug("#########################################################")

    request.cls.driver = driver

    yield
    driver.quit()

#
# # @pytest.hookimpl(hookwrapper=True)
# # def pytest_runtest_makereport(item, call):
# #     pytest_html = item.config.pluginmanager.getplugin("html")
# #     outcome = yield
# #     report = outcome.get_result()
# #     if report.when == "call":
# #         # always add url to report
# #         xfail = hasattr(report, "wasxfail")
# #         # check if test failed
# #         if (report.skipped and xfail) or (report.failed and not xfail):
# #             is_frontend_test = True if 'init_driver' in item.fixturenames else False
# #             if is_frontend_test:
# #                 results_dir = os.environ.get("RESULTS_DIR")
# #                 if not results_dir:
# #                     raise Exception("Environment variable 'RESULTS_DIR' must be set.")
# #
# #                 screen_shot_path = os.path.join(results_dir, item.name + '.png')
# #                 driver_fixture = item.funcargs['request']
# #                 allure.attach(driver_fixture.cls.driver.get_screenshot_as_png(),
# #                               name='screenshot',
# #                               attachment_type=allure.attachment_type.PNG)
#
#
# ## FOR: generating only pytest-html report
# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     pytest_html = item.config.pluginmanager.getplugin("html")
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, "extra", [])
#     if report.when == "call":
#         # always add url to report
#         xfail = hasattr(report, "wasxfail")
#         # check if test failed
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             is_frontend_test = True if 'init_driver' in item.fixturenames else False
#             if is_frontend_test:
#                 results_dir = os.environ.get("RESULTS_DIR")
#                 if not results_dir:
#                     raise Exception("Environment variable 'RESULTS_DIR' must be set.")
#
#                 screen_shot_path = os.path.join(results_dir, item.name + '.png')
#                 driver_fixture = item.funcargs['request']
#                 driver_fixture.cls.driver.save_screenshot(screen_shot_path)
#                 # only add additional html on failure
#                 # extra.append(pytest_html.extras.html('<div style="background:orange;">Additional HTML</div>'))
#                 extra.append(pytest_html.extras.image(screen_shot_path))
#
#         report.extra = extra
#
# # #========
# # @pytest.hookimpl(hookwrapper=True)
# # def pytest_runtest_makereport(item, call):
# #     pytest_html = item.config.pluginmanager.getplugin("html")
# #     outcome = yield
# #     report = outcome.get_result()
# #     extra = getattr(report, "extra", [])
# #     if report.when == "call":
# #         # always add url to report
# #         extra.append(pytest_html.extras.url("http://www.example.com/"))
# #         xfail = hasattr(report, "wasxfail")
# #         # check if test failed
# #         if (report.skipped and xfail) or (report.failed and not xfail):
# #             is_frontend_test = True if 'init_driver' in item.fixturenames else False
# #             if is_frontend_test:
# #                 results_dir = os.environ.get("RESULTS_DIR")
# #                 if not results_dir:
# #                     raise Exception("Environment variables 'RESULTS_DIR' must be set")
# #                 screenshot_path = os.path.join(results_dir, item.name + '.png')
# #                 driver_fixture = item.funcargs['request']
# #                 driver = driver_fixture.cls.driver.save_screenshot(screenshot_path)
# #             # only add additional html on failure
# #             # extra.append(pytest_html.extras.html("<div>Additional HTML</div>"))
# #             # extra.append(pytest_html.extras.image("/Users/mneelaka/PycharmProjects/python_selenium_course/ssqatest/image.jpeg"))
# #             extra.append(pytest_html.extras.image("screenshot_path"))
# #
# #         report.extra = extra
#
#
# # @pytest.fixture(autouse=True)
# # def basedriver(request):
# #     node = request.node
# #     print('Marker:', node.get_closest_marker('set1'))
# #     print("111111")
# #     logger.info("111111")
# #     logger.debug("2222222222")
# #     all_tags = []
# #     for i in node.iter_markers():
# #         print(i.name)
# #         all_tags.append(i.name)
# #         if i.name.startswith('tcid'):
# #             with open('/Users/admas/live.csv', 'a') as f:
# #                 f.write(i.name + ',\n')
# #
# #     for j in all_tags:
# #         if j.startswith('tcid'):
# #             break
# #     else:
# #         print(333333)
# #         # pdb.set_trace()
# #         print(333333)
# #     print("111111")
# #     print("111111")
# #     # import pdb; pdb.set_trace()
#
# #
# #
# # @pytest.mark.optionalhook
# # def pytest_html_results_table_header(cells):
# #     #<th class="sortable result initial-sort asc inactive" col="result"><div class="sort-icon">vvv</div>Result</th>
# #     cells.insert(1, html.th('Description'))
# #     cells.insert(2, html.th('Priority', class_="sortable", col="priority"))
# #     cells.insert(3, html.th('Owner', class_="sortable", col="owner"))
# #     cells.pop()
# #
# # @pytest.mark.optionalhook
# # def pytest_html_results_table_row(report, cells):
# #     cells.insert(1, html.td(report.description))
# #     cells.insert(2, html.td(report.priority))
# #     cells.insert(3, html.td(report.owner))
# #     cells.pop()
# #
# # @pytest.mark.hookwrapper
# # def pytest_runtest_makereport(item, call):
# #     outcome = yield
# #     report = outcome.get_result()
# #     report.description = str(item.function.__doc__)
# #
# # marker_priority = item.get_closest_marker("priority")
# # if marker_priority:
# #     report.priority = marker_priority.kwargs['value']
# #     #print(marker_priority)
# #
# # marker_owner = item.get_closest_marker("owner")
# # if marker_owner:
# #     report.owner = marker_owner.kwargs['name']
