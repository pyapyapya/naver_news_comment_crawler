import math
from selenium import webdriver
from time import sleep
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import ElementNotInteractableException

# 크롤링 작업을 위한 setting


def url_lst_to_url():
    url_file = open('E:\link.txt', 'r', encoding='utf-8')
    file = url_file.readlines()
    lst = []
    for i in file:
        lst.append(i.replace("\n", ""))
    url_file.close()
    return lst

# chromedriver path 개별 설정


chrome_driver_path = 'E:\chromedriver.exe'
driver = webdriver.Chrome(chrome_driver_path)
driver.implicitly_wait(3)

# 덧글 더보기를 클릭해주어 모든 덧글을 볼 수 있도록 함. (selenium은 load된 소스만 크롤링 할 수 있음)


def click_botten():
    comment_more_box = driver.find_element_by_css_selector('span[class=u_cbox_count]').text.replace(",", "", 1)
    comment_num = math.ceil(float(comment_more_box) / 20)
    print(comment_num)
    for i in range(0, comment_num):
        try:
            driver.find_element_by_css_selector(".u_cbox_btn_more").click()
            sleep(0.2)
            i += 1
        except ElementNotVisibleException:
            break
        except ElementNotInteractableException:
            break

# 덧글을 크롤링 함.


def write_txt(cBox, comment_txt):
    for i in cBox:
        # print(str(i.text))
        # print(type(str(i.text)))
        comment_txt.write(str(i.text) + '\n')
    comment_txt.close()

# main method


def main():
    url_lst = url_lst_to_url()
    a = 1
    for i in url_lst:
        comment_txt = open('E:\kk' + str(a) +'.txt', 'w', encoding="utf-8")
        driver.get(i)
        click_botten()
        cBox = driver.find_elements_by_css_selector('span[class=u_cbox_contents]')
        write_txt(cBox, comment_txt)
        a += 1


if __name__ == '__main__':
    main()
