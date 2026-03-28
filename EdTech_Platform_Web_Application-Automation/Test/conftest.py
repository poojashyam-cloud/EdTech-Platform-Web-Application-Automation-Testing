import os
import pytest
import pytest_html
from selenium import webdriver
from utils.config import BASE_URL
import logging

def pytest_configure(config):
    logging.basicConfig(
        filename="test.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests: chrome, firefox, edge"
    )

@pytest.fixture(scope="function")
def driver(request):
    browser = request.config.getoption("--browser")

    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError(f"Unsupported browser: {browser}")
    driver.maximize_window()
    driver.get(BASE_URL)
    yield driver
    driver.quit()

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == "call":
        driver = item.funcargs.get("driver", None)
        if driver:
            if report.passed:
                folder = "screenshots/passed"
            elif report.failed:
                folder = "screenshots/failed"
            else:
                return

            ensure_dir(folder)
            screenshot_name = os.path.join(folder, f"{item.name}.png")
            driver.save_screenshot(screenshot_name)
            print(f"Screenshot saved: {screenshot_name}")

