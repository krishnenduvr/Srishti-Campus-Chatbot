from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://www.srishticampus.com/")
wait = WebDriverWait(driver, 20)
wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "a")))

soup = BeautifulSoup(driver.page_source, "html.parser")
courses = [a.get_text(strip=True) for a in soup.find_all("a") if "/course/" in a.get("href", "")]
print("Courses found:", courses)
driver.get("https://www.srishticampus.com/about-us.php")
wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "div")))

soup = BeautifulSoup(driver.page_source, "html.parser")
about_section = [p.get_text(strip=True) for p in soup.find_all("p") if p.get_text(strip=True)]
print("\n--- ABOUT ---")
print("\n".join(about_section[:10]))  # print first 10 lines for brevity
driver.get("https://www.srishticampus.com/internship.php")
wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "div")))

soup = BeautifulSoup(driver.page_source, "html.parser")
internship_section = [p.get_text(strip=True) for p in soup.find_all("p") if p.get_text(strip=True) and p.get_text(strip=True) != "LOADING..."]
print("\n--- INTERNSHIP ---")
print("\n".join(internship_section[:10]))

# --- Scrape Placements ---
driver.get("https://www.srishticampus.com/placements.php")
wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "div")))

soup = BeautifulSoup(driver.page_source, "html.parser")
placements_section = [p.get_text(strip=True) for p in soup.find_all("p") if p.get_text(strip=True) and p.get_text(strip=True) != "LOADING..."]
print("\n--- PLACEMENTS ---")
print("\n".join(placements_section[:10]))
# --- Scrape Contact ---
driver.get("https://www.srishticampus.com/contact-us.php")
wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "div")))

soup = BeautifulSoup(driver.page_source, "html.parser")

# Extract phone numbers
phones = [p.get_text(strip=True) for p in soup.find_all(string=True) if "+91" in p]
print("\n--- CONTACT NUMBERS ---")
print(phones)

# Extract email
emails = [e.get_text(strip=True) for e in soup.find_all(string=True) if "@" in e]
print("\n--- EMAIL ---")
print(emails)
driver.quit()
