import chromedriver_binary
import json
import requests
from selenium import webdriver
from time import sleep

HEADERS = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + 'xxxxxxxxx',
}


options = webdriver.ChromeOptions()

print('connectiong to remote browser...')
driver = webdriver.Chrome(options=options)

driver.get("xxxxxxxxxxx")
print(driver.current_url)


error_pop = driver.find_elements_by_class_name('error_pop')

if len(error_pop) > 0:
    print("新着物件はありません")
else:
    link = driver.find_element_by_xpath("//table/tbody/tr/td[9]/a").get_attribute("href")

    send_text = "新着物件がありました\n"+link
    print('新着物件があります')
sleep(5)


driver.quit()

POST = {
    'to': 'xxxxxxxxxxxxxx',
    'messages': [
        {
            'type': 'text',
            'text': send_text
        }
    ]
}

CH = 'https://api.line.me/v2/bot/message/push'
REQ = requests.post(CH, headers=HEADERS, data=json.dumps(POST))

# HTTPステータスが 200 だったら OK
print(REQ.status_code)
if REQ.status_code != 200:
    print(REQ.text)
