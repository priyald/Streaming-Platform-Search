import selenium.webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import operator as op

def common_member(a, b):
    result = [i for i in a if op.countOf(b,i)>0 ]
    return result

def find(media_name):
    browser=wd.Chrome()
    browser.get("https://www.google.com")
    search_box = browser.find_element(By.ID, "APjFqb")
    search = media_name+" streaming sites"
    search_box.send_keys(search)
    search_box.submit()

    site_info=[]

    try:
        streaming_sites = WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="kp-wp-tab-TvmWatch"]/div[1]/div/div/div[2]/div[1]/div[2]/div/div/div/a/div/div[1]')))
        for i in streaming_sites:
            site_info.append(i.text.split("\n"))
    
        return site_info
    except: 
        return []

media_name = input("Enter name of movie or show: ")
if media_name!="":
    sites=find(media_name)


existing_subscriptions=[["Netflix", "Subscription"],
                        ["Amazon Prime Video", "Premium subscription"],
                        ["Hulu", "Premium subscription"]]


if sites==[]:
    print("No such movie/show found. Check the spelling once more")
else:
    print("\nThe subscriptions available to watch are:")

    j = common_member(sites,existing_subscriptions)
    k = sites
    if len(j)>0:
        for i in j:
            print("\t",i[0])
            k.remove(i)
    else:
        print("No such subscription")

    if k!=[]:
        print("\nRemaining sites are:")
        for i in k:
            print("\t",i[0],"\t\t\t",i[1])