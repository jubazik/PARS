from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.chrome.service import Service as ChromeService, Service
from selenium.webdriver.chrome.options import Options
import time

from pathlib import Path
BASE_DIR = Path(__file__).parent
path_to_db = BASE_DIR / '../database.db'


options = Options()
service = Service()

soptions = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Iris OpenGL Engine",
        fix_hairline=True
        )
