# Gerekli modullerin import edilmesi : 
    
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Chrome Driver Path :

driver = webdriver.Chrome(executable_path=r"C:\\Chrome Driver\\chromedriver.exe")

# Access to Website :

driver.get('https://postakodu.ptt.gov.tr/adres/')

driver.maximize_window()

# Bekleme Suresi tanimlama : 


# Il Liste Uzunlugunun Bulunmasi :

WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH , '//*[@id="MainContent_ComboBox1_ComboBox1_Button"]'))).click()    

html_list = driver.find_element_by_id("MainContent_ComboBox1_ComboBox1_OptionList")
items_sehir = html_list.find_elements_by_tag_name("li")
len(items_sehir)

il_drop = driver.find_element_by_xpath('//*[@id="MainContent_ComboBox1_ComboBox1_Button"]')
il_drop.click()


for sehir_index in range(1,len(items_sehir)+1):
    
    # Il Dropbox'unun Acilmasi :
    
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH , '//*[@id="MainContent_ComboBox1_ComboBox1_Button"]'))).click()    
    
     
    # Il Degerinin Secilmesi :
    
    xpath_il = '//*[@id="MainContent_ComboBox1_ComboBox1_OptionList"]/li['
    xpath_il += str(sehir_index)
    xpath_il += "]"
    
    driver.find_element_by_xpath(xpath_il).click()
        
    # Ilce Liste Uzunlugunun Bulunmasi :
    
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH , '//*[@id="MainContent_ComboBox2_ComboBox2_Button"]'))).click()        
    
           
    html_list = driver.find_element_by_id("MainContent_ComboBox2_ComboBox2_OptionList")
    items_ilce = html_list.find_elements_by_tag_name("li")
    len(items_ilce)
    
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH , '//*[@id="MainContent_ComboBox2_ComboBox2_Button"]'))).click() 
    
       
    
    for ilce_index in range(1,len(items_ilce)+1) :
        
        # Ilce Dropbox'unun Acilmasi :
            
        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH , '//*[@id="MainContent_ComboBox2_ComboBox2_Button"]'))).click()        
        
               
        # Ilce Degerinin Bulunmasi :
        
        xpath_ilce = '//*[@id="MainContent_ComboBox2_ComboBox2_OptionList"]/li['
        xpath_ilce += str(ilce_index)
        xpath_ilce += "]"
        
        driver.find_element_by_xpath(xpath_ilce).click()
        
        
        # Semt Liste Uzunlugunun Bulunmasi :
        
        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH , '//*[@id="MainContent_ComboBox3_ComboBox3_Button"]'))).click()    
                       
        
        html_list = driver.find_element_by_id("MainContent_ComboBox3_ComboBox3_OptionList")
        items_semt = html_list.find_elements_by_tag_name("li")
        len(items_semt)
        
        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH , '//*[@id="MainContent_ComboBox3_ComboBox3_Button"]'))).click()
        
                
        
        for Semt_index in range(1,len(items_semt)+1):
            
            # Semt Dropbox'unun acilmasi :
                
            WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH , '//*[@id="MainContent_ComboBox3_ComboBox3_Button"]'))).click()            
            
                        
            # Semt Degerinin Secilmesi :
            
            xpath_Semt = '//*[@id="MainContent_ComboBox3_ComboBox3_OptionList"]/li['
            xpath_Semt += str(Semt_index)
            xpath_Semt += "]"
            
            driver.find_element_by_xpath(xpath_Semt).click()
            
            
            # Mahalle Liste Uzunlugunun Bulunmasi :
            
            WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH , '//*[@id="MainContent_ComboBox4_ComboBox4_Button"]'))).click()
            
            
            html_list = driver.find_element_by_id("MainContent_ComboBox4_ComboBox4_OptionList")
            items_mahalle = html_list.find_elements_by_tag_name("li")
            len(items_mahalle)
            
            WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH , '//*[@id="MainContent_ComboBox4_ComboBox4_Button"]'))).click()
            
                        
            
            for Mahalle_index in range(1,len(items_mahalle)+1):
                
                # Mahalle Dropbox'unun acilmasi :
                
                WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH , '//*[@id="MainContent_ComboBox4_ComboBox4_Button"]'))).click()            
                
                                
                # Mahalle Degerinin secilmesi :
                
                xpath_Mahalle = '//*[@id="MainContent_ComboBox4_ComboBox4_OptionList"]/li['
                xpath_Mahalle += str(Mahalle_index)
                xpath_Mahalle += "]"
                
                driver.find_element_by_xpath(xpath_Mahalle).click()
                                
                # Sokak Liste Uzunlugunun Bulunmasi :
                
                WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH , '//*[@id="MainContent_ComboBox5_ComboBox5_Button"]'))).click()                
                
                               
                
                html_list = driver.find_element_by_id("MainContent_ComboBox5_ComboBox5_OptionList")
                items_sokak = html_list.find_elements_by_tag_name("li")
                len(items_sokak)
                
                WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH , '//*[@id="MainContent_ComboBox5_ComboBox5_Button"]'))).click()            
                
                                
                
                for Sokak_index in range(1,len(items_sokak)+1):
                    
                    # Sokak Dropbox'unun acilmasi :
                        
                    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH , '//*[@id="MainContent_ComboBox5_ComboBox5_Button"]'))).click()            
                    
                                       
                    # Sokak degerinin Secilmesi :
                    
                    xpath_Sokak = '//*[@id="MainContent_ComboBox5_ComboBox5_OptionList"]/li['
                    xpath_Sokak += str(Sokak_index)
                    xpath_Sokak += "]"
                    
                    driver.find_element_by_xpath(xpath_Sokak).click()
                    
                    
                    # Bina_no Liste Uzunlugunun Bulunmasi :
                    
                    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH , '//*[@id="MainContent_ComboBox6_ComboBox6_Button"]'))).click()            
                    
                                       
                    
                    html_list = driver.find_element_by_id("MainContent_ComboBox6_ComboBox6_OptionList")
                    items_bina_no = html_list.find_elements_by_tag_name("li")
                    len(items_mahalle)
                    
                    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH , '//*[@id="MainContent_ComboBox6_ComboBox6_Button"]'))).click()        
                    
                   
                    
                    
                    for Bina_no_index in range(1,len(items_bina_no)+1):
                        
                        # Bina_no Dropbox'unun acilmasi :
                            
                        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH , '//*[@id="MainContent_ComboBox6_ComboBox6_Button"]'))).click()        
                            
                                            
                        # Bina_no'nun Secilmesi :
                            
                        xpath_Bina_no = '//*[@id="MainContent_ComboBox6_ComboBox6_OptionList"]/li['
                        xpath_Bina_no += str(Bina_no_index)
                        xpath_Bina_no += "]"
                        
                        driver.find_element_by_xpath(xpath_Bina_no).click()
                        
                        
                        
                        ## !!Degerlerin Alinmasi!! :
                        
                        il = driver.find_element_by_xpath('//*[@id="MainContent_ComboBox1_ComboBox1_TextBox"]').get_property('value')
                        
                        ilce = driver.find_element_by_xpath('//*[@id="MainContent_ComboBox2_ComboBox2_TextBox"]').get_property('value')
                        
                        semt = driver.find_element_by_xpath('//*[@id="MainContent_ComboBox3_ComboBox3_TextBox"]').get_property('value')
                        
                        mahalle = driver.find_element_by_xpath('//*[@id="MainContent_ComboBox4_ComboBox4_TextBox"]').get_property('value')
                        
                        sokak = driver.find_element_by_xpath('//*[@id="MainContent_ComboBox5_ComboBox5_TextBox"]').get_property('value')
                        
                        bina_no = driver.find_element_by_xpath('//*[@id="MainContent_ComboBox6_ComboBox6_TextBox"]').get_property('value')
                        
                        adres = il + ',' + ilce + ',' + semt + ',' + mahalle + ","  + sokak + ',' + bina_no + '\n'
                        
                        # Write to Text File :
                        
                        tf = 'APS_veritabani.txt'
                        
                        f2 = open(tf, 'a+')                        
                        
                        f2.writelines(adres)    
                    # Sayfanin koruma protokolunden kurtulma yolu :
                    
                    driver.refresh()