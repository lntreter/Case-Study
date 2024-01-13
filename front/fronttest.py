import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CasenStudy(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://flights-app.pages.dev/")

    # Test 1
    def testInputBoxes(self):

        opt1 = None # İlk kutucukta seçilen şehir
        opt2 = None # İkinci kutucukta seçilen şehir
        wait = WebDriverWait(self.driver, 10) # Sayfa yüklenene kadar bekler.
        combobox_button = wait.until(EC.element_to_be_clickable((By.ID, "headlessui-combobox-button-:R1a9lla:"))) # İlk kutucuğun id'si
        combobox_button.click() # İlk kutucuğa tıklar.

        options_visible = EC.visibility_of_any_elements_located((By.XPATH, "//ul[@role='listbox']/li")) # Seçeneklerin görünür olmasını bekler.
        options = wait.until(options_visible) # Seçenekler görünür olana kadar bekler.

        for option in options: # Seçeneklerin içinde dolaşır.

            if "Paris" in option.text: # Eğer Paris seçeneği varsa

                option.click() # Paris seçeneğine tıklar.
                opt1 = True # opt1 True olur.
                break

        combobox_button2 = wait.until(EC.element_to_be_clickable((By.ID, "headlessui-combobox-button-:R1ahlla:"))) # İkinci kutucuğun id'si
        combobox_button2.click() # İkinci kutucuğa tıklar.

        options_visible2 = EC.visibility_of_any_elements_located((By.XPATH, "//ul[@role='listbox']/li")) # Seçeneklerin görünür olmasını bekler.
        options2 = wait.until(options_visible2) # Seçenekler görünür olana kadar bekler.

        for option in options2: # Seçeneklerin içinde dolaşır.

            if "Paris" in option.text: # Eğer Paris seçeneği varsa

                option.click() # Paris seçeneğine tıklar.
                opt2 = True # opt2 True olur.
                break


        self.assertFalse(opt1 == opt2, "Test 1 başarısız.") # Eğer iki kutucuğa da aynı şehir seçilebiliyorsa (yani hem opt1 hem opt2 true ise) test başarısız olur.

    # Test 2
    def testNumberofFlights(self):

        # İlk kutucukta seçilen şehir

        wait = WebDriverWait(self.driver, 10)
        combobox_button = wait.until(EC.element_to_be_clickable((By.ID, "headlessui-combobox-button-:R1a9lla:")))
        combobox_button.click()    

        options_visible = EC.visibility_of_any_elements_located((By.XPATH, "//ul[@role='listbox']/li"))
        options = wait.until(options_visible)

        Flights = [] # Kontrol için liste oluşturulur.

        options_visible2 = EC.visibility_of_any_elements_located((By.XPATH, "//ul[@role='listbox']/li")) # Seçeneklerin görünür olmasını bekler.

        # Tüm seçenekleri teker teker kontrol etmesi için for döngüsü oluşturulur.

        for index in range(len(options)): 

            options = wait.until(options_visible) 
            options[index].click() # Seçeneklere tek tek tıklar.
            wait.until(EC.element_to_be_clickable((By.ID, "headlessui-combobox-button-:R1ahlla:"))).click() # İkinci kutucuğa tıklar.
            selections = wait.until(options_visible2) # İkinci kutucuktaki seçenekler görünür olana kadar bekler.

            for index in range(len(selections)):

                selections = wait.until(options_visible2) # Sayfa yenilendiğinde seçeneklerin görünür olmasını bekler.
                selections[index].click() # Seçeneklere tek tek tıklar.
                findList = EC.visibility_of_any_elements_located((By.XPATH, "//ul[@role='list']/li")) # Uçuşların görünür olmasını bekler. 
                s1 = wait.until(EC.visibility_of_any_elements_located((By.XPATH, "/html/body/main/div[2]"))) # Uçuş olmadığında çıkan yazıyı bulur.

                if s1[0].get_attribute("innerHTML") != "Bu iki şehir arasında uçuş bulunmuyor. Başka iki şehir seçmeyi deneyebilirsiniz.": # Eğer uçuş yoksa

                    # Uçuş sayısını bulur.

                    p = wait.until(EC.visibility_of_any_elements_located((By.XPATH, 
                        "//div[@class='mt-24 max-w-5xl w-full justify-center items-center text-sm lg:flex']/div/p[@class='mb-10']")))
                    print(len(p), p[0].get_attribute('innerHTML')) # Kotnrol için yazdırır.

                    # Uçuş sayısı ile uçuşların sayısı eşitse True, değilse False ekler.

                    try:

                        availableFlights = wait.until(findList)
                    
                    except:
                    
                        availableFlights = []
                    
                    if str(len(availableFlights)) in p[0].get_attribute('innerHTML'):
                    
                        Flights.append(True)
                    
                    else:
                    
                        Flights.append(False)
                
                else:
                    
                    Flights.append(True) # Uçuş yoksa True ekler.
                
                wait.until(EC.element_to_be_clickable((By.ID, "headlessui-combobox-button-:R1ahlla:"))).click() # Döngünün sonunda ikinci kutucuğa tıklar.

            wait.until(EC.element_to_be_clickable((By.ID, "headlessui-combobox-button-:R1a9lla:"))).click()  # İlk döngünün sonunda ilk kutucuğa tıklar.
                
        print(Flights)
        self.assertTrue(all(Flights), "Test 2 Başarısız.") # Eğer tüm uçuşlar için True döndüyse test başarılı olur.
    

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()