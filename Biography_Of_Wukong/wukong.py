from urllib import request
from bs4 import BeautifulSoup

if __name__ == '__main__':
    wukong_file = open('悟空传.txt', 'w', encoding='utf-8')
    wukong_url = 'http://www.shushu8.com/jinhezai/wukongchuan/'
    heads = {}
    heads['User-Agent'] = 'Mozilla/5.0 (Linux; U; Android 2.2; en-gb; GT-P1000 Build/FROYO) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'
    wukong_req = request.Request(url=wukong_url, headers=heads)
    wukong_response = request.urlopen(wukong_req)
    wukong_html = wukong_response.read().decode('gbk')
    wukong_soup = BeautifulSoup(wukong_html, 'lxml')
    wukong_chapters = wukong_soup.find_all('div', class_="chapter9")
    wukong_chapters_soup = BeautifulSoup(str(wukong_chapters), 'lxml')
    for child in wukong_chapters_soup.div.children:
        if child != '\n':
            wukong_texts_url = 'http://www.shushu8.com'+child.a.get('href')
            wukong_text_req = request.Request(url=wukong_texts_url, headers=heads)
            wukong_text_response = request.urlopen(wukong_text_req)
            wukong_text_html = wukong_text_response.read().decode('gbk', 'ignore')
            wukong_text_soup = BeautifulSoup(wukong_text_html, 'lxml')
            wukong_text_txt = wukong_text_soup.find_all('pre', class_='note', id='content')
            wukong_text_soup2 = BeautifulSoup(str(wukong_text_txt), 'lxml')
            wukong_file.write(child.a.string)
            wukong_file.write('\n\n')
            wukong_file.write(wukong_text_soup2.pre.text)
            wukong_file.write('\n\n')

    wukong_file.close()

