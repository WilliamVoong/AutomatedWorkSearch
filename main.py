from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time
keywords = {"kock", "server", "städ"}
def main(): 
    SET = set() 
    already_searched = set(line.strip() for line in open("searched-links.txt"))
    newly_searched_email= set()
    driver = webdriver.Firefox()
    req = driver.get("https://arbetsformedlingen.se/platsbanken/annonser?q=servit%C3%B6r%20kock%20st%C3%A4dare&l=3:z2cX_rjC_zFo;3:CSy8_41F_YvX;3:xQc2_SzA_rHK")
    adlinks = driver.find_elements(By.XPATH, "//a[@data-event-action='AS - Platsbanken - Annonslistsida - Annons - Link - Click']")
    for adlink in adlinks:
        #print("Value is: %s" % adlink.get_attribute("href"))
        SET.add(adlink.get_attribute("href"))
    for link in SET:
        if link not in already_searched:
            driver.get(link)
            time.sleep(1)
            try:
                mailAdress= driver.find_element(By.XPATH,"//a[@data-event-action='AS - Platsbanken - Annonssida - Maila din ansökan - Link - Click']")
                newly_searched_email.add(mailAdres.text)
                print(mailAdress.text)
            except: 
                print("email not found")
            time.sleep(1)
            driver.back()
main()
# TODO auto-send email
# TODO refactor code