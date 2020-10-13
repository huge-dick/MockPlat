# encoding=utf-8
# @Author : wangjie
# @Time : 2020/3/30 下午2:26
from bs4 import BeautifulSoup
import requests

import config


class Eureka(object):
    '''
        查找Eurkea上面的服务ip
        params:eureka 的IP地址
        return
    '''

    def __init__(self, erueka_address=config.eureka):
        self.erueka_address = erueka_address

    def tag_has_target(self, a):
        return a.has_attr('target')

    def get_service_ip(self, service=''):
        '''
        查找指定服务IP
        :param service: 服务名称
        :return:服务IP
        '''
        service = service.lower()
        res = requests.get(self.erueka_address)
        soup = BeautifulSoup(res.text, "lxml")
        # print(soup.a['class'])
        list_a = soup.find_all(self.tag_has_target)
        result = f'Not found service,please check service name:{service}'
        found = False
        for i in list_a:
            href = i['href'].split('/actu')[0]
            service_name = i.get_text().split(':')[1].lower()
            if service == service_name:
                # print(href,service_name)
                # result=f'{service_name}:{href}'
                result = href
                found = True
                break
        if not found:
            print(f'Not found service,please check service name:{service}')
        return result

    def query_all(self):
        '''
        查询所有服务
        :return:所有服务IP
        '''
        res = requests.get(self.erueka_address)
        soup = BeautifulSoup(res.text, "lxml")
        list_a = soup.find_all(self.tag_has_target)
        for i in list_a:
            href = i['href'].split('/actu')[0]
            service_name = i.get_text().split(':')[1].lower()
            print(service_name, href)


if __name__ == '__main__':
    print(Eureka().get_service_ip('ACCOUNT'))

