from selenium import webdriver
 
#Paso 1
driver = webdriver.Firefox()
 
#Paso 2
driver.get("http://www.mercadolibre.com.ar")
 
#Paso 3
textbox = driver.find_element_by_id("query")
 
#Paso 4
textbox.send_keys("Disco SSD")
 
#Paso 5
button = driver.find_element_by_name("mlSearchBtn")
 
#Paso 6
button.click()
 
#Paso 7: En este caso es transparente
 
#Paso 8
try:
    driver.find_element_by_id("searchResults")
    print("Se encontro el elemento, por lo que el test paso.")
except:
    print("No se encontro el elemento, por lo que el test no paso")
