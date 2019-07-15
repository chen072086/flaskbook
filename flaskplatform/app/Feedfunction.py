#!usr/bin/evn python

#encoding:utf-8

import feedparser

def test(url='http://blog.csdn.net/together_cz/article'):
    '''
    学习使用feedparser
    :param url:
    :return:
    '''
    one_page_dict = feedparser.parse(url)

    print(one_page_dict)

    print(one_page_dict['feed']['meta']['name'])


if __name__=='__main__':
    url_list = ['http://www.baidu.com', 'http://www.taobao.com']
    for one_url in url_list:
        test(one_url)