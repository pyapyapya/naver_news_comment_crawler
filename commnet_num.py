from selenium import webdriver
from naver_news_comment_parsing import url_lst_to_url

# chromedriver path 개별 설정

chrome_driver_path = 'E:\chromedriver.exe'
driver = webdriver.Chrome(chrome_driver_path)
driver.implicitly_wait(3)

# url들이 담겨진 txt파일을 읽어들임


def count_num():
    comment_num = driver.find_element_by_css_selector('span[class=u_cbox_count]').text.replace(",", "", 1)
    # print(comment_num)
    return comment_num


def main():
    url_lst = url_lst_to_url()
    total_comment = 0
    url_count = 1
    for lst in url_lst:
        driver.get(lst)
        total_comment += int(count_num())
        f.write("url" + str(url_count) + " : " + str(count_num()) + '\n')
        url_count += 1

    f.write("total comments : " + str(total_comment))


if __name__ == '__main__':
    f = open("E:\crawl\comment_total.txt", 'w', encoding='utf-8')
    main()
    f.close()
