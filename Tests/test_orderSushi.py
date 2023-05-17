import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest

class TestOrderingSushi:

    @pytest.mark.sushiOrder
    def test_order_sushi(self, driver):

        #--------------------------------------------------------------------------------------------------------------------go to webpage
        driver.get("https://www.mikansushi.es/")

        #--------------------------------------------------------------------------------------------------------------------shows hidden login block
        icon_lock = driver.find_element(By.XPATH, "//*[@id='header']/div/div[1]/div[3]/div/div[2]/div/a/span/i")
        driver.execute_script("arguments[0].click();", icon_lock)
        time.sleep(1)

        #--------------------------------------------------------------------------------------------------------------------username and password insertion
        user_name_insert = driver.find_element(By.XPATH, "//*[@id='user_login']")
        user_name_insert.send_keys("")                           # insert login user name

        password_insert = driver.find_element(By.XPATH, "//*[@id='user_pass']")
        password_insert.send_keys("")                            # insert login user password

        #--------------------------------------------------------------------------------------------------------------------Click on loggin button
        driver.find_element(By.XPATH, "//*[@id='loginform']/div[3]/button").click()
        time.sleep(6)

        #--------------------------------------------------------------------------------------------------------------------Click on Pedido Online
        pedido_online_loc = driver.find_element(By.XPATH, "//*[@id='nav-menu-item-6045']/a")
        pedido_online_loc.click()
        time.sleep(2)

        #--------------------------------------------------------------------------------------------------------------------Select items
        sashimi = driver.find_element(By.XPATH, "//*[@id='wppizza-article-1-90-7890-0-0']")
        sashimi.click()
        time.sleep(3)

        maki_salmao = driver.find_element(By.XPATH, "//*[@id='wppizza-article-1-87-7931-0-0']")
        maki_salmao.click()
        time.sleep(3)
        
        maki_gambas = driver.find_element(By.XPATH, "//*[@id='wppizza-article-1-87-7943-0-0']")
        maki_gambas.click()
        time.sleep(3)
        
        maki_dragon = driver.find_element(By.XPATH, "//*[@id='wppizza-article-1-95-7951-0-0']")
        maki_dragon.click()
        time.sleep(3)
        
        #--------------------------------------------------------------------------------------------------------------------Click on REALICE SU PEDIDO button
        realice_su_pedido = driver.find_element(By.XPATH, "//*[@id='wppizza-minicart']/span[4]/input")
        realice_su_pedido.click()
        time.sleep(5)

        #--------------------------------------------------------------------------------------------------------------------add 1 more maki salmon
        one_more_button = driver.find_element(By.XPATH, "//*[@id='wppizza-order-item-1.87.7931.0.0']/td[1]/span/a[1]")
        one_more_button.click()
        one_more_button.send_keys(Keys.ENTER)
        time.sleep(3)
        
        #--------------------------------------------------------------------------------------------------------------------Delivery data insert
        nombre = driver.find_element(By.XPATH, "//*[@id='cname']")                         # name 
        nombre.send_keys("")

        direccion = driver.find_element(By.XPATH, "//*[@id='caddress']")                   # address
        direccion.send_keys("")

        telefono = driver.find_element(By.XPATH, "//*[@id='ctel']")                        # phone number
        telefono.send_keys("")

        comentarios = driver.find_element(By.XPATH, "//*[@id='ccomments']")                # comment
        comentarios.send_keys("El Maki Dragon SIN salsa y SIN crema porfa. Muchas gracias. =)")

        #--------------------------------------------------------------------------------------------------------------------Select card payment method
        tarjeta_payment = driver.find_element(By.XPATH, "//*[@id='wppizza-gateway-ccod']")
        tarjeta_payment.click()
        time.sleep(2)

        #--------------------------------------------------------------------------------------------------------------------Click Enviar Pedido button
        enviar_pedido = driver.find_element(By.XPATH, "//*[@id='wppizza-ordernow']")
        enviar_pedido.click()
        time.sleep(5)

        #--------------------------------------------------------------------------------------------------------------------Assertion
        # confirmation_message = driver.find_element(By.XPATH, "").text
        # assert confirmation_message == "", "The order wasn't completed, try again."