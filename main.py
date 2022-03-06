from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

TARGET_URL = "https://picklebet.com/sports/cricket/betting/?any=&page=1&tab=next"
delay = 10 
driver = Chrome(ChromeDriverManager().install())
try:
    driver.get(TARGET_URL)
    WebDriverWait(driver, delay).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="gatsby-focus-wrapper"]/div/div[1]/div/div/div[1]/div/div[2]/div[2]/div[3]'))
    )
    game_rows=driver.find_elements_by_class_name("MatchRow-module--match--fikdW")
    # iterate through list and get text
    print("-----------------------------------------------------------------------------------\n")
    print("   Sport  |  Tournament  |  Game  |  Selection  |  Value   ")
    print("-----------------------------------------------------------------------------------\n")
    sport = ''
    tournament = ''
    for i in game_rows:
        sport = i.find_elements_by_class_name("MatchRow-module--game--tZd2S")[0].text if i.find_elements_by_class_name("MatchRow-module--game--tZd2S") else sport
        tournament = i.find_elements_by_class_name("MatchRow-module--season--6cUSu")[0].text if i.find_elements_by_class_name("MatchRow-module--season--6cUSu") else tournament
        competitors = i.find_elements_by_class_name("Outcome-module--outcome---4ckI")

        selection1 = competitors[0].find_elements_by_class_name("Outcome-module--name--8JkNE")[0].text
        selection2 = competitors[1].find_elements_by_class_name("Outcome-module--name--8JkNE")[0].text

        value1 = competitors[0].find_elements_by_class_name("Outcome-module--odds--TojHm")[0].text
        value2 = competitors[1].find_elements_by_class_name("Outcome-module--odds--TojHm")[0].text

        print(f"   {sport} | {tournament} |  {selection1} vs {selection2}  |  {selection1} | {value1}   \n")
        print("-----------------------------------------------------------------------------------\n")
        print(f"   {sport} | {tournament} |  {selection1} vs {selection2}  |  {selection2} | {value2}   \n")
        print("-----------------------------------------------------------------------------------\n")
except Exception as e:
    print(e)
finally:
    driver.quit()
