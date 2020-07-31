# setutime
色图time爬虫/接口

[爬行网站点击进入](https://qqkj52.com/zhainanshe/)

------

### 用法：

使用python shell加载



```
python
from setutime import *
r = search('萝莉') 
r #展示当前页面
Out[6]: 
1: 极品萝莉网红草莓味的奈奈兔JK无圣光套图[36P]
2: 极品萝莉网红萌兰酱牛仔裤无圣光套图[82P]
3: 极品萝莉网红一只云烧绯红女仆无圣光套图[46P]
4: 极品萝莉网红九尾狐狸m6月新作无圣光套图[35P]
5: 极品萝莉网红柚木E罩杯天然美少女无圣光套图[57P]
6: 极品萝莉网红咬一口小奈樱COS女仆丝袜无圣光套图[41P]
7: 极品萝莉网红柚木丰满肉感的巨乳娘无圣光套图[40P]
8: 极品萝莉网红日奈森果浴室里的小天使无圣光套图[68P]
r.crawl(1) #爬取第一个
next_page: https://qqhk16.com/luyilu/2020/0712/9102.html
response len: 25379
next_page: https://qqhk16.com/luyilu/2020/0712/9102_2.html
response len: 24992
next_page: https://qqhk16.com/luyilu/2020/0712/9102_3.html
response len: 24999
next_page: https://qqhk16.com/luyilu/2020/0712/9102_4.html
response len: 25000
next_page: https://qqhk16.com/luyilu/2020/0712/9102_5.html
response len: 24874
next_page: https://qqhk16.com/luyilu/2020/0712/9102_6.html
response len: 24877
next_page: https://qqhk16.com/luyilu/2020/0712/9102_7.html
response len: 24877
next_page: https://qqhk16.com/luyilu/2020/0712/9102_8.html
response len: 24819
downloading img from: https://www.images.zhaofulipic.com:8819/allimg/200712/16111353c-0.jpg
downloading img from: https://www.images.zhaofulipic.com:8819/allimg/200712/1611135a3-1.jpg
downloading img from: https://www.images.zhaofulipic.com:8819/allimg/200712/1611132Z4-2.jpg
downloading img from: https://www.images.zhaofulipic.com:8819/allimg/200712/16111343M-3.jpg
downloading img from: https://www.images.zhaofulipic.com:8819/allimg/200712/1611135054-4.jpg
downloading img from: https://www.images.zhaofulipic.com:8819/allimg/200712/161113N23-5.jpg
downloading img from: https://www.images.zhaofulipic.com:8819/allimg/200712/1611135500-6.jpg
downloading img from: https://www.images.zhaofulipic.com:8819/allimg/200712/161113AU-7.jpg
downloading img from: https://www.images.zhaofulipic.com:8819/allimg/200712/1611133544-8.jpg
downloading img from: https://www.images.zhaofulipic.com:8819/allimg/200712/1611135396-9.jpg
downloading img from: https://www.images.zhaofulipic.com:8819/allimg/200712/1611134S3-10.jpg
downloading img from: https://www.images.zhaofulipic.com:8819/allimg/200712/161113C25-11.jpg
downloading img from: https://www.images.zhaofulipic.com:8819/allimg/200712/1611134530-12.jpg
downloading img from: https://www.images.zhaofulipic.com:8819/allimg/200712/16111331N-13.jpg
downloading img from: https://www.images.zhaofulipic.com:8819/allimg/200712/1611135132-14.jpg
downloading img from: https://www.images.zhaofulipic.com:8819/allimg/200712/1611134429-15.jpg
downloading img from: https://www.images.zhaofulipic.com:8819/allimg/200712/161113D34-16.jpg
downloading img from: https://www.images.zhaofulipic.com:8819/allimg/200712/16111321S-17.jpg
downloading img from: https://www.images.zhaofulipic.com:8819/allimg/200712/1611132496-18.jpg
downloading img from: https://www.images.zhaofulipic.com:8819/allimg/200712/1611132209-19.jpg
downloading img from: https://www.images.zhaofulipic.com:8819/allimg/200712/161113O14-20.jpg
downloading img from: https://www.images.zhaofulipic.com:8819/allimg/200712/16111341O-21.jpg
downloading img from: https://www.images.zhaofulipic.com:8819/allimg/200712/1611133245-22.jpg
downloading img from: https://www.images.zhaofulipic.com:8819/allimg/200712/161113CB-23.jpg
downloading img from: https://www.images.zhaofulipic.com:8819/allimg/200712/1611132439-24.jpg
downloading img from: https://www.images.zhaofulipic.com:8819/allimg/200712/1611132423-25.jpg
downloading img from: https://www.images.zhaofulipic.com:8819/allimg/200712/1611132W8-26.jpg
downloading img from: https://www.images.zhaofulipic.com:8819/allimg/200712/1611133636-27.jpg
downloading img from: https://www.images.zhaofulipic.com:8819/allimg/200712/1611135Q8-28.jpg
downloading img from: https://www.images.zhaofulipic.com:8819/allimg/200712/1611134960-29.jpg
downloading img from: https://www.images.zhaofulipic.com:8819/allimg/200712/1611133036-30.jpg
downloading img from: https://www.images.zhaofulipic.com:8819/allimg/200712/1611133036-31.jpg
downloading img from: https://www.images.zhaofulipic.com:8819/allimg/200712/1611136032-32.jpg
downloading img from: https://www.images.zhaofulipic.com:8819/allimg/200712/1611134M3-33.jpg
downloading img from: https://www.images.zhaofulipic.com:8819/allimg/200712/1611131241-34.jpg
downloading img from: https://www.images.zhaofulipic.com:8819/allimg/200712/161113IB-35.jpg
```

------

### api:

自己看源代码