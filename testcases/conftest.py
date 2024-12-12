import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def pytest_addoption(parser):
    # Adds browser_name option to the pytest CLI to run tests on different browsers
    parser.addoption("--browser_name", action="store", default="chrome")


@pytest.fixture(scope="class")
def setUp(request):
    # Get the browser name from the command line arguments
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser_name == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser_name == "edge":
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    else:
        raise ValueError(f"Browser {browser_name} not supported")

    # Set implicit wait and maximize the window
    driver.implicitly_wait(10)
    driver.maximize_window()

    # Navigate to the desired URL
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # Use WebDriverWait for elements instead of time.sleep (recommended)
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@name='username']")))
    except TimeoutException:
        print("Timed out waiting for the page to load.")

    # If the request is a class-based test, assign the driver to the test class
    if request.cls is not None:
        request.cls.driver = driver

    yield driver  # Yield the driver to the test

    # Close the browser after the test completes
    driver.quit()
