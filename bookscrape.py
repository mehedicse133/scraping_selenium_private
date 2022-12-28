
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path)

# driver.find_element(By.XPATH, '//button[text()="Some text"]')
# driver.find_elements(By.XPATH, '//button')




driver.get('https://www.adamchoi.co.uk/teamgoals/detailed')
all_matches_button = driver.find_element(By.XPATH, '//label[@analytics-event="All matches"]')
all_matches_button.click()
dopdown = driver.find_elements(By.ID, "country")
dopdown = driver.find_elements(By.TAG_NAME, value="Option")
for i in dopdown:
    print(i.text)
i = 0
while i < len(dopdown):
    if (dopdown[i].text == "Italy"):
        dopdown[i].click()
        break

    i += 1




# time.sleep(3)


date = []
home_teams = []
score = []
away_team = []


matches = driver.find_elements(By.TAG_NAME, "tr")
for match in matches:
    date.append(match.find_element(By.XPATH,'./td[1]').text)
    home_teams.append(match.find_element(By.XPATH,'./td[2]').text)
    score.append(match.find_element(By.XPATH,'./td[3]').text)
    away_team.append(match.find_element(By.XPATH,'./td[4]').text)

print(date)
# driver.quit()
# df = pd.DataFrame({'date':date,'home_teams':home_teams,'score':score,'away_team':away_team})
# df.to_csv('team.csv',index=False)
# print(df)


#   https://www.youtube.com/watch?v=H32uEDpCFLI
# https://www.youtube.com/watch?v=2cnXcOnmc5o&list=PLCCaxHeSItrMvZdUkgzJbXZZSzVL3xrt4


# https://www.toptal.com/python/web-scraping-with-python
# https://pypi.org/project/webdriver-manager/


# Loop through transactions and count
# links = driver.find_elements_by_tag_name('a')
# link_urls = [link.get_attribute('href') for link in links]
# thisCount = 0
# isFirst = 1
# for url in link_urls:
# if (url.find("GetXas.do?processId") >= 0):  # URL to link to transactions
#        	if isFirst == 1:  # already expanded +
#               	isFirst = 0
# else:
#        	driver.get(url)  # collapsed +, so expand


'''
add datetime row
https://www.youtube.com/watch?v=HiOtQMcI5wg

https://www.youtube.com/watch?v=wtSlg9G3onA

email
https://www.youtube.com/watch?v=H4f3PvDCkvc

https://www.youtube.com/watch?v=HBqYKthsB2E&list=PLgjw1dR712jqjwhvA2V6_DTVVKou_HHlW
'''
