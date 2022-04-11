from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium import webdriver

def crawling_signature():
    options = webdriver.ChromeOptions()
    options.add_argument("headless")

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.implicitly_wait(1)

    a = list()
    b = list()
    c = list()

    MAXPAGE = 18
    MAXROW = 31
    s = "$"
    for pgNum in range(1, MAXPAGE+1):
        try:
            url = f"https://filesignatures.net/index.php?page=all&currentpage={pgNum}&order=EXT&alpha=All"

            driver.get(url)
            driver.implicitly_wait(1)

            print("[+] Current Page Number : ", pgNum)

            for i in range(2, MAXROW+1):
                a.append(driver.find_element_by_xpath(f"/html/body/div/div[4]/center/table/tbody/tr/td/center/table/tbody/tr[{i}]/td[2]/span/a").text)
                b.append(driver.find_element_by_xpath(f"/html/body/div/div[4]/center/table/tbody/tr/td/center/table/tbody/tr[{i}]/td[3]/span/a").text)
                c.append(driver.find_element_by_xpath(f"/html/body/div/div[4]/center/table/tbody/tr/td/center/table/tbody/tr[{i}]/td[4]").text)

        except Exception as e:
            print("[-] Crawling Error : ", e)
            driver.close()
            pass

    with open("./resource/signature_format.txt", "w") as f:
        for a1, b1, c1 in zip(a, b, c):
            data = a1 + "$" + b1.replace(" ", "") + "$" + c1 + "\n"
            print(f"[+] Insert Signature Data : {data}")
            f.write(data)

    print("[+] Complate Crawling !!!")
