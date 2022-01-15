from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


account = EMAIL_ADDRESS
password = PASSWORD

path = "/Users/webdriver browser/chromedriver"
s = Service(path)
driver = webdriver.Chrome(service = s)

url = "https://www.linkedin.com/jobs/search/?f_AL=true&f_TPR=a1641447354-&geoId=104769905&keywords=data%20scientist&location=Sydney%2C%20New%20South%20Wales%2C%20Australia"
driver.get(url)

sign_in = driver.find_element(By.CLASS_NAME, "nav__button-secondary")
sign_in.click()

email_item = driver.find_element(By.ID, "username")
email_item.send_keys(account)
pass_item = driver.find_element(By.ID, "password")
pass_item.send_keys(password)
sign = driver.find_element(By.CLASS_NAME, "login__form_action_container ")
sign.click()

job_list = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")
for job in job_list:
    job.click()
    try:
        first_apply = driver.find_element(By.CSS_SELECTOR, ".jobs-search-results__list-item")
        first_apply.click()
        submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")

        #check if it a multiple step applications
        if submit_button.get_attribute("arial-label") == "Continue to next step":
            close_button = driver.find_element(By.CSS_SELECTOR, ".artdeco-modal__dismiss")
            close_button.click()
            discard_button = driver.find_element(By.CSS_SELECTOR, ".primary ember")
            discard_button.click()
        else:
            submit_button.click()
    except NoSuchElementException:
        continue
driver.close()

