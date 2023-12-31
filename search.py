import selenium.webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from personal_info import *

if browsing_choice==["chrome"]:
    options=wd.ChromeOptions()
    options.add_argument('headless')
    browser=wd.Chrome(options)
elif browsing_choice==["msedge"]:
    options=wd.EdgeOptions()
    options.add_argument('headless')
    browser=wd.Edge(options)
elif browsing_choice==["firefox"]:
    options=wd.FirefoxOptions()
    options.add_argument('headless')
    browsing=wd.Firefox(options)
elif browsing_choice==["msie"]:
    options=wd.IeOptions()
    options.add_argument('headless')
    browsing=wd.Ie(options)
elif browsing_choice==["safari"]:
    options=wd.SafariOptions()
    options.add_argument('headless')
    browsing=wd.Safari(options)


def find(media_name):
    if browsing_choice=="":
        print("Browser not supported")
        return []
    browser.get("https://www.google.com")
    search_box = browser.find_element(By.ID, "APjFqb")
    search = media_name+" streaming sites"
    search_box.send_keys(search)
    search_box.submit()

    site_info=[]

    try:
        print("Waiting time 10 seconds...")
        streaming_sites = WebDriverWait(browser, 5).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="kp-wp-tab-TvmWatch"]/div[1]/div/div/div[2]/div[1]/div[2]/div/div/div/a/div/div[1]')))
        for i in streaming_sites:
            site_info.append(i.text.split("\n"))
    
        return site_info
    except:
        return []


