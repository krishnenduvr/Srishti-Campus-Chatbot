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

driver.get("https://www.srishticampus.com/course/python")
wait.until(EC.presence_of_all_elements_located((By.TAG_NAME,"div")))
soup=BeautifulSoup(driver.page_source, "html.parser")
python=[p.get_text(strip=True) for p in soup.find_all("p") if p.get_text(strip=True)]
print("\n--- PYTHON COURSE ---")
print("\n".join(python[:20]))

driver.get("https://www.srishticampus.com/course/java")
wait.until(EC.presence_of_all_elements_located((By.TAG_NAME,"div")))
soup=BeautifulSoup(driver.page_source, "html.parser")
java=[p.get_text(strip=True) for p in soup.find_all("p") if p.get_text(strip=True)]
print("\n--- JAVA COURSE ---")
print("\n".join(java[:15]))

driver.get("https://www.srishticampus.com/course/software-testing")
wait.until(EC.presence_of_all_elements_located((By.TAG_NAME,"div")))
soup=BeautifulSoup(driver.page_source, "html.parser")
software_testing=[p.get_text(strip=True) for p in soup.find_all("p") if p.get_text(strip=True)]
print("\n ---SOFTWARE TESTING ---")
print("\n".join(software_testing[:10]))

driver.get("https://www.srishticampus.com/course/web-design")
wait.until(EC.presence_of_all_elements_located((By.TAG_NAME,"div")))
soup=BeautifulSoup(driver.page_source,"html.parser")
web_design=[p.get_text(strip=True) for p in soup.find_all("p") if p.get_text(strip=True)]
print("\n ---WEB DESIGNING ---")
print("\n".join(web_design[:10]))


driver.get("https://www.srishticampus.com/course/mean-stack-node")
wait.until(EC.presence_of_all_elements_located((By.TAG_NAME,"div")))
soup=BeautifulSoup(driver.page_source,"html.parser")
mean_stack=[p.get_text(strip=True) for p in soup.find_all("p") if p.get_text(strip=True)]
print("\n ---Mean Stack ---")
print("\n".join(mean_stack[:30]))

driver.get("https://www.srishticampus.com/course/mysql")
wait.until(EC.presence_of_all_elements_located((By.TAG_NAME,"div")))
soup=BeautifulSoup(driver.page_source,"html.parser")
mysql=[p.get_text(strip=True) for p in soup.find_all("p") if p.get_text(strip=True)]
print("\n --- MySQL ---")
print("\n".join(mysql[:10]))


driver.get("https://www.srishticampus.com/course/digitalmarketing")
wait.until(EC.presence_of_all_elements_located((By.TAG_NAME,"div")))
soup=BeautifulSoup(driver.page_source,"html.parser")
digital_marketing=[p.get_text(strip=True) for p in soup.find_all("p") if p.get_text(strip=True)]
print("\n --- Digital Marketing ---")
print("\n".join(digital_marketing))

driver.get("https://www.srishticampus.com/course/android-full-stack-course")
wait.until(EC.presence_of_all_elements_located((By.TAG_NAME,"div")))
soup=BeautifulSoup(driver.page_source,"html.parser")
antroid_full_stack_course=[p.get_text(strip=True) for p in soup.find_all("p") if p.get_text(strip=True)]
print("\n --- antroid_full_stack ---")
print("\n".join(antroid_full_stack_course))


driver.get("https://www.srishticampus.com/course/data-science-python")
wait.until(EC.presence_of_all_elements_located((By.TAG_NAME,"div")))
soup=BeautifulSoup(driver.page_source,"html.parser")
Datascience_using_python=[p.get_text(strip=True) for p in soup.find_all("p") if p.get_text(strip=True)]
print("\n --- Datascience_using_python ---")
print("\n".join(Datascience_using_python))


driver.get("https://www.srishticampus.com/online-training.php")
wait.until(EC.presence_of_all_elements_located((By.TAG_NAME,"div")))
soup=BeautifulSoup(driver.page_source,"html.parser")
online_training=[p.get_text(strip=True) for p in soup.find_all("p") if p.get_text(strip=True)]
print("\n --- Online Training ---")
print("\n".join(online_training))


driver.get("https://www.srishticampus.com/projects.php")
wait.until(EC.presence_of_all_elements_located((By.TAG_NAME,"div")))
soup=BeautifulSoup(driver.page_source,"html.parser")
projects=[p.get_text(strip=True) for p in soup.find_all("p") if p.get_text(strip=True)]
print("\n --- Academic projects ---")
print("\n".join(projects[:10]))



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