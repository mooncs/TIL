import requests
from bs4 import  BeautifulSoup
from pprint import pprint

url = 'https://movie.naver.com/movie/sdb/rank/rmovie.naver'
response = requests.get(url).text
data = BeautifulSoup(response, 'html.parser')
movie = data.find_all('class', 'tit3')


'''
# # Task1 환율 정보 수집하기
# url = 'https://finance.naver.com/marketindex/'
# response = requests.get(url).text
# data = BeautifulSoup(response, 'html.parser')

# # data.select_one을 이용할 떄는 copy selector
# us_ex = data.select_one('#exchangeList > li.on > a.head.usd > div > span.value').text
# jpn_ex = data.select_one('#exchangeList > li:nth-child(2) > a.head.jpy > div > span.value').text

# print("현재 원달러 환율은 {}원 입니다.".format(us_ex))
# print("현재 원엔화 환율은 {}원 입니다.".format(jpn_ex))


# currencies = data.find_all('h3', class_='h_lst')
# ex_rates = data.find_all('span', class_='value')
# currency = [currency.text for currency in currencies]
# ex_rate = [rate.text for rate in ex_rates]
# for i in range(len(currency)-5):
#     print('{}의 환율은 {}원 입니다.'.format(currency[i], ex_rate[i]))

'''