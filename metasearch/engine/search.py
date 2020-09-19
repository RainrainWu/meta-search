import json

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


def search_meta(keyword):

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    
    result = {}
    result["yahoo"] = search_yahoo(browser, keyword)
    result["google"] = search_google(browser, keyword)
    result["baidu"] = search_baidu(browser, keyword)
    browser.close()
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return result


def search_yahoo(browser, keyword):
    yahoo_url = "https://search.yahoo.com/search;_ylt=Awr9Ds9LtWVfNscAFnNDDWVH;_ylc=X1MDMTE5NzgwNDg2NwRfcgMyBGZyAwRncHJpZANjbFVVbjFlS1FaV3VFR2RsQUduLnVBBG5fcnNsdAMwBG5fc3VnZwMxMARvcmlnaW4Dc2VhcmNoLnlhaG9vLmNvbQRwb3MDMARwcXN0cgMEcHFzdHJsAwRxc3RybAMzBHF1ZXJ5A2ZvbwR0X3N0bXADMTYwMDUwMTA3NA--?fr2=sb-top-search&p={KEYWORD}&fr=sfp&iscqry="
    yahoo_xpath = "/html/body/div[1]/div[3]/div/div/div[1]/div/div/div/div/ol/li[{ORDER}]/div/div[1]/h3/a"
    browser.get(yahoo_url.format(KEYWORD="foo"))
    buffer = {}

    for i in range(1, 4):
        key = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, yahoo_xpath.format(ORDER=i)))
        ).text
        val = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, yahoo_xpath.format(ORDER=i)))
        ).get_attribute("href")
        buffer[key] = val
    return buffer


def search_google(browser, keyword):
    google_url = "https://www.google.com/search?q={KEYWORD}"
    google_xpath_text = "/html/body/div[7]/div[2]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[{ORDER}]/div/div[1]/a/h3"
    google_xpath_url = "/html/body/div[7]/div[2]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[{ORDER}]/div/div[1]/a"
    browser.get(google_url.format(KEYWORD="foo"))
    buffer = {}

    for i in range(3, 6):
        key = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, google_xpath_text.format(ORDER=i)))
        ).text
        val = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, google_xpath_url.format(ORDER=i)))
        ).get_attribute("href")
        buffer[key] = val
    return buffer

def search_baidu(browser, keyword):
    baidu_url = "http://www.baidu.com/s?ie=utf-8&wd={KEYWORD}"
    baidu_xpath = "/html/body/div[1]/div[3]/div[1]/div[3]/div[{ORDER}]/h3/a"
    browser.get(baidu_url.format(KEYWORD="foo"))
    buffer = {}

    for i in range(1, 4):
        key = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, baidu_xpath.format(ORDER=i)))
        ).text
        val = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, baidu_xpath.format(ORDER=i)))
        ).get_attribute("href")
        buffer[key] = val
    return buffer