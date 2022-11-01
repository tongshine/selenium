from selenium.webdriver import Edge
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
web = Edge()
web.get("https://lagou.com/")

#找到某个元素点击
el = web.find_element(By.XPATH,'//*[@id="changeCityBox"]/p[1]/a')
el.click()#点击事件

#找到输入框，输入python，输入回车
web.find_element(By.XPATH,'//*[@id="search_input"]').send_keys("python",Keys.ENTER)

list = web.find_elements(By.XPATH,'//*[@id="jobList"]/div[1]/div')
for item in list: #/html/body/div/div[1]/div/div[2]/div[3]/div/div[1]/div[1]/div[1]

    name = item.find_element(By.XPATH,'./div[1]/div[1]/div[1]/a').text  #注意item不要写成 list
    price = item.find_element(By.XPATH,'./div[1]/div[1]/div[2]/span').text #少数了一个div
    print(name,price)