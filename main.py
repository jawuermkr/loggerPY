from selenium import webdriver

usuario = "correo@usuario.com"
clave = "clave"

url = "url-a-conectar"

driver = webdriver.Chrome("/home/user/donde_esta_driver_con_extencion.exe")

driver.get(url)

driver.find_element_by_name("mail").send_keys(usuario)
driver.find_element_by_name("pass").send_keys(clave)
driver.find_element_by_name("btn").click()

print("Ingreso satisfactorio")
