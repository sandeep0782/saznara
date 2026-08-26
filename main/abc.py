import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

DEBUG_ADDRESS = "127.0.0.1:9222"
GROUP_NAME = "My Group"


def chrome_is_available():
    try:
        response = requests.get(
            f"http://{DEBUG_ADDRESS}/json/version",
            timeout=2,
        )
        return response.ok
    except requests.RequestException:
        return False


if not chrome_is_available():
    raise RuntimeError("Chrome is not running with remote debugging on port 9222.")


options = webdriver.ChromeOptions()
options.add_experimental_option(
    "debuggerAddress",
    DEBUG_ADDRESS,
)

driver = webdriver.Chrome(options=options)

print("Connected to existing Chrome")
print("URL:", driver.current_url)

wait = WebDriverWait(driver, 30)

# Wait until WhatsApp has loaded
wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

# Find the group
group = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            f'//span[@title="{GROUP_NAME}"]',
        )
    )
)

group.click()

print(f"Opened group: {GROUP_NAME}")

# Keep Chrome open
input("Press Enter to finish...")
