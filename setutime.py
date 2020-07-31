from requests import get as rget
from lxml import etree
import random
import os
from urllib.parse import quote, urljoin, urlsplit

user_agent = [
"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko",
"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
"Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
"Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
"Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
"Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
"Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
"Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
"MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
"Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10",
"Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
"Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+",
"Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0",
"Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124",
"Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)",
"UCWEB7.0.2.37/28/999",
"NOKIA5700/ UCWEB7.0.2.37/28/999",
"Openwave/ UCWEB7.0.2.37/28/999",
"Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999",
]

def get(url, headers=None):
    if not headers:
        headers = get_header()
    try:
        return rget(url, timeout=10, headers=headers)
    except TimeoutError:
        print(f'timeout!')


def get_header():
    header = {'User-Agent': random.choice(user_agent),
              'cookies': 'ASPSESSIONIDCQCRAQRB=BJIIDJKBLKJLJFDPENMNIEIA; UM_distinctid=173a3db9182a-026412db3dc4c08-7b631e35-100200-173a3db9183b2; CNZZDATA1254428444=530434908-1596179079-https%253A%252F%252Fqqkj52.com%252F%7C1596179079; Hm_lvt_731a53a94394c1764ce2ab6cc1a76d2d=1596181943; Hm_lpvt_731a53a94394c1764ce2ab6cc1a76d2d=1596181943'}
    #print(f'header: {header}')
    return header

start_url = 'https://so.azs2019.com/serch.php?keyword={}'


def get_imgs(url):
    next_page = url
    imgs = []
    root = url[:url.rfind('/') + 1]

    while next_page:
        print(f'next_page: {next_page}')
        header = get_header()
        response = get(next_page, headers=header)
        response.encoding = 'gbk'
        print(f'response len: {len(response.text)}')
        html = etree.HTML(response.text)

        try:
            next_page = urljoin(root, html.xpath("//li[@class='next-page']//a")[0].attrib['href'])
        except:
            next_page = False

        imgs += (html.xpath("//article[@class='article-content']//img//@src"))
    return imgs



class SearchResult:
    def __init__(self, result, next_page):
        self.next_page = next_page
        self.result = result

    def get_next_page(self):
        url = self.next_page
        main_url = url
        response = get(url)
        response.encoding = 'gbk'
        print(f'response len: {len(response.text)}')
        html = etree.HTML(response.text)
        li = html.xpath("//article")
        #print(f'li : {li}')
        result = []
        for each in li:
            header = each[0]
            a = header[-1][0]
            discription = a.attrib['title']
            url = a.attrib['href']
            result.append((discription, url))
        return SearchResult(result, next_page=main_url[:main_url.rfind('=') + 1] + str(int(main_url[main_url.rfind('=') + 1:]) + 1))

    def crawl(self, index):
        print('开始爬')
        img_urls = get_imgs(self.result[index - 1][1])
        print('开始下图片')
        dowm_imgs(img_urls, self.result[index - 1][0])
        print('下完了')

    def __repr__(self):
        s = ''
        i = 1
        for discription, url in self.result:
            s += str(i) + ': ' + discription + '\n'
            i += 1
        return s


def search(keyword='萝莉'):
    header = get_header()
    main_url = start_url.format(quote(keyword, encoding='gbk')) + '&page=1'
    response = get(main_url)
    response.encoding = 'gbk'
    print(f'response len: {len(response.text)}')
    html = etree.HTML(response.text)
    li = html.xpath("//article")
    #print(f'li : {li}')
    result = []
    for each in li:
        header = each[0]
        a = header[-1][0]
        discription = a.attrib['title']
        url = a.attrib['href']
        result.append((discription, url))
    return SearchResult(result, next_page=main_url[:main_url.rfind('=') + 1] + str(int(main_url[main_url.rfind('=') + 1:]) + 1))


root = 'imgs/'
if not os.path.exists(root):
    os.mkdir(root)

def dowm_imgs(urls, dir='default'):
    if not os.path.exists(root + dir):
        os.mkdir(root + dir)

    fnames = []
    for img_url in urls:
        fname = root + dir + '/' + img_url[img_url.rfind('/') + 1:]
        fnames.append(fname)
        with open(fname, 'wb') as f:
            response = get(img_url)
            while not len(response.content) == int(response.headers['Content-Length']):
                response = get(img_url)
                print(f'at dowmloading_img: 错误')
            f.write(response.content)
            print(f'downloading img from: {img_url}')
    return fnames


if __name__ == '__main__':
    r = search()
    while True:
        print(eval(input('最好别用这个功能>')))



