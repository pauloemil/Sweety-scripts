from selenium import webdriver
from time import  sleep
from random import randint
from selenium.common.exceptions import NoSuchElementException
email = "yourAccountHere"
password = "password"
driver = webdriver.Chrome("W:\courses\python selenium\chromedriver")
driver.get("https://learn.sha.edu.eg/auth/oidc/")
sleep(2)
driver.find_element_by_name("loginfmt").send_keys(email)
sleep(2)
driver.find_element_by_id("idSIButton9").click()
sleep(2)
driver.find_element_by_name("passwd").send_keys(password)
sleep(2)
driver.find_element_by_id("idSIButton9").click()
sleep(2)
driver.find_element_by_id("idSIButton9").click()
sleep(2)
driver.get("https://learn.sha.edu.eg/mod/quiz/attempt.php?attempt=16943&cmid=2098")
sleep(2)
x = 0
print("section: ", end="")
section = int(input())
print("gomla tet7t for el as2ela el mkalya: ", end="")
gomla = input()
x = 0
for i in range(5):
    for j in range(44):
        x += 1
        y = randint(0, 2)
        print("question:", x)
        try:
            #lw fe aktr mn 3 choices yeb2a so2al el section fa hay5tar el section bta3k
            driver.find_element_by_id("q17773:" + str(x) + "_answer3")
            driver.find_element_by_id("q17773:" + str(x) + "_answer"+str(section-1)).click()

        except NoSuchElementException:
            try:
                #lw so2al 3ade mwafek, mo7ayed, 8er mwafek hya5od wa7ed 34wa2e
                driver.find_element_by_id("q17773:" + str(x) + "_answer"+str(y)).click()
            except NoSuchElementException:
                #lw so2al mkale hay7ot el gomla bta3tk
                driver.find_element_by_id("q17773:" + str(x) + "_answer_ideditable").send_keys(gomla)
        finally:
            sleep(0.1)


    driver.find_element_by_name("next").click()
    sleep(2)

