from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from time import sleep
link = "https://open.spotify.com/playlist/2b6uvPJzAnMtFyzNItGHyu?si=62025d3ec1c74706&nd=1"
options = Options()
driver = webdriver.Firefox(options=options, executable_path=r'./geckodriver.exe')
cnt = 0

while cnt<58:
    driver.get("https://spotifydown.com/tr")
    sleep(0.2)
    searchInput = driver.find_elements(By.XPATH,"//*[contains(@class, 'searchInput')]")[0]
    searchInput.send_keys(link)
    sleep(0.05)
    indirButon = driver.find_elements(By.XPATH,"//button[text()='İndir']") [0]
    indirButon.click()
    sleep(0.05)
    print("burda")
    sleep(1)
    artir=500
    while 1:
        try:
            allIndirButtons = driver.find_elements(By.XPATH,"//button[text()='İndir']")
            driver.execute_script(f"window.scrollTo(0, {artir})")
            allIndirButtons[cnt].click()
            break
        except:
            artir+=100
            continue

    artir=0
    while 1:
        try:
            indirButon2 = driver.find_elements(By.XPATH,"//a[contains(text(), 'İndir')]")[0]
            driver.execute_script(f"window.scrollTo(0, {artir})")
            indirButon2.click()
            break
        except:
            artir+=100
            continue
    cnt += 1