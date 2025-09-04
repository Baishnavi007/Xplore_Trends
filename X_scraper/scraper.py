import os
import time
import socket
import django
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv

# -----------------------------
#  Django + Env Setup
# -----------------------------
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "X_scraper.settings")
django.setup()

from trends_scraper.models import TrendRun  # Import after django.setup()

load_dotenv()
X_EMAIL = os.getenv("X_EMAIL")
X_USERNAME = os.getenv("X_USERNAME")
X_PASSWORD = os.getenv("X_PASSWORD")


# -----------------------------
#  Selenium Login Function
# -----------------------------
def login_to_x():
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1400,900")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://x.com/login")
    time.sleep(3)

    # Enter email
    email_field = driver.find_element(By.NAME, "text")
    email_field.send_keys(X_EMAIL)
    email_field.send_keys(Keys.RETURN)
    time.sleep(3)

    # Enter username only if asked
    try:
        username_field = driver.find_element(By.NAME, "text")
        username_field.send_keys(X_USERNAME)
        username_field.send_keys(Keys.RETURN)
        time.sleep(3)
    except:
        print("⚠ Username step skipped")

    # Enter password
    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys(X_PASSWORD)
    password_field.send_keys(Keys.RETURN)
    time.sleep(5)

    return driver


# -----------------------------
#  Scrape Top Trends
# -----------------------------
def fetch_top_trends(driver):
    driver.get("https://x.com/explore")
    time.sleep(5)

    opened_div = driver.find_element(
        By.XPATH,
        '//div[@aria-label="Timeline: Explore"]//div[@data-testid="cellInnerDiv"][6]'
    )

    next_five_divs = opened_div.find_elements(
        By.XPATH, 'following-sibling::div[@data-testid="cellInnerDiv"][position() <= 5]'
    )

    texts = [div.text for div in next_five_divs if div.text.strip()]
    trend_names = [t.split("\n")[1] if "\n" in t else t for t in texts]

    return trend_names[:5]


# -----------------------------
#  Save to PostgreSQL via ORM
# -----------------------------
def save_to_db(trends):
    ip_address = socket.gethostbyname(socket.gethostname())

    while len(trends) < 5:
        trends.append("")

    TrendRun.objects.create(
        trend1=trends[0],
        trend2=trends[1],
        trend3=trends[2],
        trend4=trends[3],
        trend5=trends[4],
        ip_address=ip_address
    )
    print("✅ Data inserted into DB!")


# -----------------------------
#  Main Runner
# -----------------------------
def main():
    driver = login_to_x()
    print("✅ Logged in successfully!")

    trends = fetch_top_trends(driver)
    print("🔥 Top 5 Trends:", trends)

    save_to_db(trends)
    driver.quit()
    return trends