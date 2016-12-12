from selenium import webdriver
 
#Paso 1
driver = webdriver.Firefox()
 
#Paso 2
driver.get("http://www.mercadolibre.com.ar")
 
#Paso 3
textbox = driver.find_element_by_id("query")
 
#Paso 4
textbox.send_keys("Buscounproductoquenoexisteparanada")
 
#Paso 5
button = driver.find_element_by_name("mlSearchBtn")
 
#Paso 6
button.click()
 
#Paso 7: En este caso es transparente
 
#Paso 8
textelement = driver.find_element_by_class_name("typo")
 
if textelement.text == 'No hay publicaciones que coincidan con tu busqueda.':
    print("El test paso correctamente")
else:
    print("El test no paso")
