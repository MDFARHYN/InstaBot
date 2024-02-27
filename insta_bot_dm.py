from selenium import webdriver
from selenium_stealth import stealth
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import json

with open('account.json', 'r') as file:
    account_info = json.load(file)
    for account in account_info:
        username = account["username"]
        password = account["password"]
       
 
        is_follow_input = input("Do you want to send DM to your followers? Type YES or NO:  ")    
        message_text = input("type your message: ")
        is_follow = False
        is_following =  True

        is_follow_input = is_follow_input.lower().strip()

        if is_follow_input == "yes":
               is_follow = True
               is_following = False
        else:
            is_follow = False
            is_following = True
            print("Sending message to people those your are following")
            



        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")

        # options.add_argument("--headless")

        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        driver = webdriver.Chrome(options=options)

        stealth(driver,
                languages=["en-US", "en"],
                vendor="Google Inc.",
                platform="Win32",
                webgl_vendor="Intel Inc.",
                renderer="Intel Iris OpenGL Engine",
                fix_hairline=True,
                )

        url = "https://www.instagram.com/accounts/login/"
        driver.get(url)

        button_locator = (By.XPATH, '//div[text()="Log in"]')
        login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(button_locator))
               
        user_name = driver.find_element(By.CSS_SELECTOR, 'input[aria-label="Phone number, username, or email"]')
        user_name.send_keys(username)
        password_fields = driver.find_element(By.CSS_SELECTOR, 'input[aria-label="Password"]')
        password_fields.send_keys(password)
        time.sleep(5)
        login_button.click()

        input("press Enter after solve challanges :")

        # Wait for the "Not Now" button to be present in the DOM
        not_now_button_locator = (By.XPATH, '//button[text()="Not Now"]')
        not_now_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located(not_now_button_locator))

        # Wait for the "Not Now" button to be clickable
        not_now_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(not_now_button_locator))

        # Now you can interact with the "Not Now" button
        not_now_button.click()


        #wait for profile
        profile_button_locator = (By.CSS_SELECTOR, 'div:nth-child(8) .x9jhf4c')
        profile_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(profile_button_locator))
        profile_button.click()

        if is_following:
            #wait following_button
            following_button =(By.CSS_SELECTOR, '.x2pgyrj~ .x2pgyrj+ .x2pgyrj ._a6hd')
            wait_following_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located(following_button))

            #click following_button
            following_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(following_button))
            following_button.click()

        else:
            #wait_followers
            followers =  (By.CSS_SELECTOR,'.x2pgyrj:nth-child(2) ._a6hd')
            followers_wait =  WebDriverWait(driver, 20).until(EC.presence_of_element_located(followers))

            #click followers_button
            followers_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located(followers))
            followers_button.click()

      
        time.sleep(2)   
        pop_up_window = WebDriverWait( 
            driver, 10).until(EC.presence_of_element_located( 
                (By.XPATH, '//div[@class="_aano"]')))

        profile_list = []
        for i in range (1,7):
               
              driver.execute_script( 
                'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',  
              pop_up_window)
              
              time.sleep(2)

        profile = driver.find_elements(By.CSS_SELECTOR,'._aad7')
        for i in profile[:5]:
                    profile_url = f'https://www.instagram.com/{i.text}/'
                    print(profile_url)
                    profile_list.append(profile_url)

         
        for i in profile_list:
                    time.sleep(5) 
                    print(f"Waiting 10 seconds for sending another message",  )
                    driver.get(i)
                    profile_url = i
                    message_buuton =  (By.CSS_SELECTOR, '.x5n08af.xsz8vos')  
                    #wait_for_message_button
                    wait_message_buuton = WebDriverWait(driver, 20).until(EC.presence_of_element_located(message_buuton))
                    #click_message_button
                    click_message_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(message_buuton))
                    click_message_button.click()
                               
                    #wait_text_input
                    text_input =  (By.CLASS_NAME, 'xzsf02u')             
                    wait_text_input = WebDriverWait(driver, 20).until(EC.presence_of_element_located(text_input))
                    text_box = driver.find_element(By.CLASS_NAME, 'xzsf02u')
                    text_box.send_keys(message_text)
                    time.sleep(5) 
                    text_box.send_keys(Keys.ENTER)
                    print(f"Message_TEXT: {message_text} sent sucessfully to this profile {profile_url} ")
                    
                  
                   
                     
                    

        driver.quit()
        print("\nsucessfully send all messages")
       
   
 
