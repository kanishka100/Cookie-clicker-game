import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# path = "C:\development\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get("https://orteil.dashnet.org/experiments/cookie/")
time_to_check = time.time() + 5
cookie = driver.find_element_by_id("cookie")
right_panel = driver.find_elements_by_css_selector(".grayed b")
ls = []
for a in right_panel[:8]:
    ls.append(a.text.split("-")[1].replace(",", ""))
print(ls)
game_over = time.time()
old_time = time.time()
while True:
    if time.time() - game_over < 5*60:
        cookie.click()
        if time.time() - old_time > 5:
            if int(driver.find_element_by_id("money").text.replace(",", "")) > int(' 123456789'):
                time_machine = driver.find_element_by_id("buyTime machine")
                time_machine.click()
            elif int(driver.find_element_by_id("money").text.replace(",", "")) > int(' 1000000'):
                portal = driver.find_element_by_id("buyPortal")
                portal.click()
            elif int(driver.find_element_by_id("money").text.replace(",", "")) > int(' 50000'):
                alchemy = driver.find_element_by_id("buyAlchemy lab")
                alchemy.click()
            elif int(driver.find_element_by_id("money").text.replace(",", "")) > int(' 7000'):
                shipment = driver.find_element_by_id("buyShipment")
                shipment.click()
            elif int(driver.find_element_by_id("money").text.replace(",", "")) > int(' 2000'):
                mine = driver.find_element_by_id("buyMine")
                mine.click()
            elif int(driver.find_element_by_id("money").text.replace(",", "")) > int(' 500'):
                factory = driver.find_element_by_id("buyFactory")
                factory.click()
            elif int(driver.find_element_by_id("money").text) > int(' 100'):
                grandma = driver.find_element_by_id("buyGrandma")
                grandma.click()
            elif int(driver.find_element_by_id("money").text) > int(' 15'):
                cursor = driver.find_element_by_id("buyCursor")
                cursor.click()
            old_time = time.time()
    else:
        res = driver.find_element_by_id("cps")
        print(res.text)
        break
driver.close()