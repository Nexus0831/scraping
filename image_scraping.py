import time
from urllib.request import urlretrieve
import subprocess
from selenium import webdriver


# 新たなSeleniumドライバを作る
driver = webdriver.PhantomJS(executable_path='/usr/local/Cellar/phantomjs/2.1.1/bin/phantomjs')
# うまくいかない時はFirefoxを使う


driver.get("http://www.amazon.com/War-Peace-Leo-Nikolayevich-Tolstoy/dp/1427030200")
time.sleep(2)

# 本のプレビューボタンをクリック
driver.find_element_by_id('sitbLogoImg').click()
image_list = set()

print("1")
time.sleep(5)

while "pointer" in driver.find_element_by_id("sitbReaderRightPageTurner").get_attribute('style'):
    print("2")
    driver.find_element_by_id("sitbReaderRightPageTurner").click()
    print("3")
    time.sleep(2)

    pages = driver.find_element_by_xpath("//div[@class='pageImage']/div/img")

    for page in pages:
        image = page.get_attribute("src")
        image_list.add(image)

driver.quit()

for image in sorted(image_list):
    urlretrieve(image, 'page.jpg')
    p = subprocess.Popen(["tesseract", "page.jpg", "page"],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    p.wait()
    f = open("page.txt", "r", encoding='UTF-8')
    print(f.read())