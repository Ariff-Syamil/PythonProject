import os
# import json
from datetime import datetime, date, timedelta

import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

yesterday_price = None
day_before_price = None
# today = date.today()
today = datetime.strptime('2025-11-20',"%Y-%m-%d").date()
yesterday = today - timedelta(days=1)
day_before_yesterday = today - timedelta(days=2)

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
# ALPHA_URL = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={ALPHA_API}'
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHA_API = os.environ.get("ALPHA_K") # "0Z1QOGWFSTK5BEOC"
ALPHA_ENDPOINT = "https://www.alphavantage.co/query"
ALPHA_parameter = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK,
    "apikey" : ALPHA_API,
}
# stock_price_daily = requests.get(ALPHA_ENDPOINT, params=ALPHA_parameter, timeout=1200)
# stock_price_daily = stock_price_daily.json()
stock_price = {'Meta Data': {'1. Information': 'Daily Prices (open, high, low, close) and Volumes', '2. Symbol': 'TSLA', '3. Last Refreshed': '2025-11-19', '4. Output Size': 'Compact', '5. Time Zone': 'US/Eastern'}, 'Time Series (Daily)': {'2025-11-19': {'1. open': '385.111', '2. high': '411.7800', '3. low': '398.5000', '4. close': '403.9900', '5. volume': '69412223'}, '2025-11-18': {'1. open': '405.3800', '2. high': '408.9000', '3. low': '393.7100', '4. close': '401.2500', '5. volume': '80688637'}, '2025-11-17': {'1. open': '398.7400', '2. high': '423.9600', '3. low': '398.7400', '4. close': '408.9200', '5. volume': '102214259'}, '2025-11-14': {'1. open': '386.3000', '2. high': '412.1900', '3. low': '382.7800', '4. close': '404.3500', '5. volume': '105506682'}, '2025-11-13': {'1. open': '423.1300', '2. high': '424.5000', '3. low': '396.3400', '4. close': '401.9900', '5. volume': '118948032'}, '2025-11-12': {'1. open': '442.1500', '2. high': '442.3290', '3. low': '426.5600', '4. close': '430.6000', '5. volume': '58513520'}, '2025-11-11': {'1. open': '439.4000', '2. high': '442.4900', '3. low': '432.3600', '4. close': '439.6200', '5. volume': '60533237'}, '2025-11-10': {'1. open': '439.6000', '2. high': '449.6715', '3. low': '433.3600', '4. close': '445.2300', '5. volume': '76515907'}, '2025-11-07': {'1. open': '437.9200', '2. high': '439.3600', '3. low': '421.8800', '4. close': '429.5200', '5. volume': '103471495'}, '2025-11-06': {'1. open': '461.9600', '2. high': '467.4500', '3. low': '435.0900', '4. close': '445.9100', '5. volume': '109622907'}, '2025-11-05': {'1. open': '452.0500', '2. high': '466.3299', '3. low': '440.7100', '4. close': '462.0700', '5. volume': '84911911'}, '2025-11-04': {'1. open': '454.4600', '2. high': '460.2200', '3. low': '443.6000', '4. close': '444.2600', '5. volume': '87756644'}, '2025-11-03': {'1. open': '455.9900', '2. high': '474.0700', '3. low': '453.8000', '4. close': '468.3700', '5. volume': '84595244'}, '2025-10-31': {'1. open': '446.7500', '2. high': '458.0000', '3. low': '443.6855', '4. close': '456.5600', '5. volume': '83135787'}, '2025-10-30': {'1. open': '451.0500', '2. high': '455.0607', '3. low': '439.6100', '4. close': '440.1000', '5. volume': '72447938'}, '2025-10-29': {'1. open': '462.5000', '2. high': '465.7000', '3. low': '452.6500', '4. close': '461.5100', '5. volume': '67983544'}, '2025-10-28': {'1. open': '454.7750', '2. high': '467.0000', '3. low': '451.6000', '4. close': '460.5500', '5. volume': '80185667'}, '2025-10-27': {'1. open': '439.9800', '2. high': '460.1600', '3. low': '438.6900', '4. close': '452.4200', '5. volume': '105867547'}, '2025-10-24': {'1. open': '446.8300', '2. high': '451.6800', '3. low': '430.1700', '4. close': '433.7200', '5. volume': '94727774'}, '2025-10-23': {'1. open': '420.0000', '2. high': '449.3999', '3. low': '413.9000', '4. close': '448.9800', '5. volume': '126709833'}, '2025-10-22': {'1. open': '443.4500', '2. high': '445.5390', '3. low': '429.0000', '4. close': '438.9700', '5. volume': '84023458'}, '2025-10-21': {'1. open': '445.7550', '2. high': '449.3000', '3. low': '442.0500', '4. close': '442.6000', '5. volume': '54412169'}, '2025-10-20': {'1. open': '443.8650', '2. high': '449.8000', '3. low': '440.6100', '4. close': '447.4300', '5. volume': '63718971'}, '2025-10-17': {'1. open': '425.5000', '2. high': '441.4558', '3. low': '423.6000', '4. close': '439.3100', '5. volume': '89331578'}, '2025-10-16': {'1. open': '434.7300', '2. high': '439.3500', '3. low': '421.3101', '4. close': '428.7500', '5. volume': '77189889'}, '2025-10-15': {'1. open': '434.9000', '2. high': '440.5100', '3. low': '426.3301', '4. close': '435.1500', '5. volume': '71558185'}, '2025-10-14': {'1. open': '426.7900', '2. high': '434.2000', '3. low': '417.8600', '4. close': '429.2400', '5. volume': '72669438'}, '2025-10-13': {'1. open': '423.5300', '2. high': '436.8900', '3. low': '419.7000', '4. close': '435.9000', '5. volume': '79552785'}, '2025-10-10': {'1. open': '436.5400', '2. high': '443.1300', '3. low': '411.4500', '4. close': '413.4900', '5. volume': '112107870'}, '2025-10-09': {'1. open': '431.8100', '2. high': '436.3500', '3. low': '426.1800', '4. close': '435.5400', '5. volume': '69339928'}, '2025-10-08': {'1. open': '437.5700', '2. high': '441.3300', '3. low': '425.2300', '4. close': '438.6900', '5. volume': '71192128'}, '2025-10-07': {'1. open': '447.8200', '2. high': '452.6800', '3. low': '432.4501', '4. close': '433.0900', '5. volume': '102296082'}, '2025-10-06': {'1. open': '440.7500', '2. high': '453.5500', '3. low': '436.6900', '4. close': '453.2500', '5. volume': '85324878'}, '2025-10-03': {'1. open': '443.2850', '2. high': '446.7700', '3. low': '416.5750', '4. close': '429.8300', '5. volume': '133188180'}, '2025-10-02': {'1. open': '470.5400', '2. high': '470.7500', '3. low': '435.5700', '4. close': '436.0000', '5. volume': '137008950'}, '2025-10-01': {'1. open': '443.8000', '2. high': '462.2900', '3. low': '440.7500', '4. close': '459.4600', '5. volume': '98122285'}, '2025-09-30': {'1. open': '441.5200', '2. high': '445.0000', '3. low': '433.1200', '4. close': '444.7200', '5. volume': '74357960'}, '2025-09-29': {'1. open': '444.3500', '2. high': '450.9800', '3. low': '439.5000', '4. close': '443.2100', '5. volume': '79491510'}, '2025-09-26': {'1. open': '428.3000', '2. high': '440.4700', '3. low': '421.0200', '4. close': '440.4000', '5. volume': '101628160'}, '2025-09-25': {'1. open': '435.2400', '2. high': '435.3500', '3. low': '419.0800', '4. close': '423.3900', '5. volume': '96746426'}, '2025-09-24': {'1. open': '429.8300', '2. high': '444.2100', '3. low': '429.0301', '4. close': '442.7900', '5. volume': '93133570'}, '2025-09-23': {'1. open': '439.8800', '2. high': '440.9700', '3. low': '423.7200', '4. close': '425.8500', '5. volume': '83422691'}, '2025-09-22': {'1. open': '431.1100', '2. high': '444.9800', '3. low': '429.1300', '4. close': '434.2100', '5. volume': '97108777'}, '2025-09-19': {'1. open': '421.8200', '2. high': '429.4700', '3. low': '421.7200', '4. close': '426.0700', '5. volume': '93131034'}, '2025-09-18': {'1. open': '428.8650', '2. high': '432.2199', '3. low': '416.5600', '4. close': '416.8500', '5. volume': '90454509'}, '2025-09-17': {'1. open': '415.7500', '2. high': '428.3121', '3. low': '409.6700', '4. close': '425.8600', '5. volume': '106133532'}, '2025-09-16': {'1. open': '414.4950', '2. high': '423.2500', '3. low': '411.4300', '4. close': '421.6200', '5. volume': '104285721'}, '2025-09-15': {'1. open': '423.1300', '2. high': '425.7000', '3. low': '402.4300', '4. close': '410.0400', '5. volume': '163823667'}, '2025-09-12': {'1. open': '370.9400', '2. high': '396.6899', '3. low': '370.2400', '4. close': '395.9400', '5. volume': '168156391'}, '2025-09-11': {'1. open': '350.1700', '2. high': '368.9900', '3. low': '347.6000', '4. close': '368.8100', '5. volume': '103756010'}, '2025-09-10': {'1. open': '350.5500', '2. high': '356.3300', '3. low': '346.0700', '4. close': '347.7900', '5. volume': '72121679'}, '2025-09-09': {'1. open': '348.4400', '2. high': '350.7700', '3. low': '343.8200', '4. close': '346.9700', '5. volume': '53815991'}, '2025-09-08': {'1. open': '354.6400', '2. high': '358.4400', '3. low': '344.8400', '4. close': '346.4000', '5. volume': '75208290'}, '2025-09-05': {'1. open': '348.0000', '2. high': '355.8700', '3. low': '344.6801', '4. close': '350.8400', '5. volume': '108989785'}, '2025-09-04': {'1. open': '336.1500', '2. high': '338.8900', '3. low': '331.4800', '4. close': '338.5300', '5. volume': '60711033'}, '2025-09-03': {'1. open': '335.2000', '2. high': '343.3300', '3. low': '328.5100', '4. close': '334.0900', '5. volume': '88238894'}, '2025-09-02': {'1. open': '328.2300', '2. high': '333.3300', '3. low': '325.6000', '4. close': '329.3600', '5. volume': '58391952'}, '2025-08-29': {'1. open': '347.2300', '2. high': '348.7499', '3. low': '331.7000', '4. close': '333.8700', '5. volume': '81145660'}, '2025-08-28': {'1. open': '350.9100', '2. high': '353.5500', '3. low': '340.2600', '4. close': '345.9800', '5. volume': '67903224'}, '2025-08-27': {'1. open': '351.9400', '2. high': '355.3900', '3. low': '349.1560', '4. close': '349.6000', '5. volume': '65519012'}, '2025-08-26': {'1. open': '344.9300', '2. high': '351.9000', '3. low': '343.7200', '4. close': '351.6700', '5. volume': '76651550'}, '2025-08-25': {'1. open': '338.9000', '2. high': '349.5300', '3. low': '335.0300', '4. close': '346.6000', '5. volume': '86670037'}, '2025-08-22': {'1. open': '321.6600', '2. high': '340.2500', '3. low': '319.6900', '4. close': '340.0100', '5. volume': '94016347'}, '2025-08-21': {'1. open': '322.0800', '2. high': '324.9000', '3. low': '318.6800', '4. close': '320.1100', '5. volume': '55744445'}, '2025-08-20': {'1. open': '329.2200', '2. high': '331.3700', '3. low': '314.6000', '4. close': '323.9000', '5. volume': '77481768'}, '2025-08-19': {'1. open': '335.7900', '2. high': '340.5500', '3. low': '327.8500', '4. close': '329.3100', '5. volume': '75956002'}, '2025-08-18': {'1. open': '329.6200', '2. high': '336.2700', '3. low': '329.5900', '4. close': '335.1600', '5. volume': '56956552'}, '2025-08-15': {'1. open': '337.6550', '2. high': '339.3000', '3. low': '327.0200', '4. close': '330.5600', '5. volume': '74319792'}, '2025-08-14': {'1. open': '335.7600', '2. high': '340.4699', '3. low': '330.4000', '4. close': '335.5800', '5. volume': '75000662'}, '2025-08-13': {'1. open': '341.5000', '2. high': '348.9800', '3. low': '338.2000', '4. close': '339.3800', '5. volume': '67838892'}, '2025-08-12': {'1. open': '345.0000', '2. high': '345.2600', '3. low': '332.9400', '4. close': '340.8400', '5. volume': '80690111'}, '2025-08-11': {'1. open': '335.0000', '2. high': '346.6400', '3. low': '334.1500', '4. close': '339.0300', '5. volume': '105320174'}, '2025-08-08': {'1. open': '321.4300', '2. high': '335.1500', '3. low': '320.9800', '4. close': '329.6500', '5. volume': '91200319'}, '2025-08-07': {'1. open': '319.7900', '2. high': '322.4000', '3. low': '316.1600', '4. close': '322.2700', '5. volume': '66658672'}, '2025-08-06': {'1. open': '307.8900', '2. high': '320.4700', '3. low': '306.9345', '4. close': '319.9100', '5. volume': '78523579'}, '2025-08-05': {'1. open': '308.9500', '2. high': '312.4499', '3. low': '305.5000', '4. close': '308.7200', '5. volume': '57961278'}, '2025-08-04': {'1. open': '309.0800', '2. high': '312.1186', '3. low': '303.0001', '4. close': '309.2600', '5. volume': '78683905'}, '2025-08-01': {'1. open': '306.2050', '2. high': '309.3100', '3. low': '297.8200', '4. close': '302.6300', '5. volume': '89121446'}, '2025-07-31': {'1. open': '319.6050', '2. high': '321.3700', '3. low': '306.1000', '4. close': '308.2700', '5. volume': '85270919'}, '2025-07-30': {'1. open': '322.1800', '2. high': '324.4499', '3. low': '311.6164', '4. close': '319.0400', '5. volume': '83931942'}, '2025-07-29': {'1. open': '325.5500', '2. high': '326.2500', '3. low': '318.2500', '4. close': '321.2000', '5. volume': '87358861'}, '2025-07-28': {'1. open': '318.4500', '2. high': '330.4900', '3. low': '315.6900', '4. close': '325.5900', '5. volume': '112673755'}, '2025-07-25': {'1. open': '308.7400', '2. high': '323.6300', '3. low': '308.0100', '4. close': '316.0600', '5. volume': '148227027'}, '2025-07-24': {'1. open': '310.0000', '2. high': '310.1500', '3. low': '300.4100', '4. close': '305.3000', '5. volume': '156966023'}, '2025-07-23': {'1. open': '330.9000', '2. high': '336.2000', '3. low': '328.6700', '4. close': '332.5600', '5. volume': '92553756'}, '2025-07-22': {'1. open': '329.7400', '2. high': '335.4098', '3. low': '321.5500', '4. close': '332.1100', '5. volume': '77370371'}, '2025-07-21': {'1. open': '334.4000', '2. high': '338.0000', '3. low': '326.8800', '4. close': '328.4900', '5. volume': '75768797'}, '2025-07-18': {'1. open': '321.6600', '2. high': '330.9000', '3. low': '321.4200', '4. close': '329.6500', '5. volume': '94254993'}, '2025-07-17': {'1. open': '323.1500', '2. high': '324.3400', '3. low': '317.0601', '4. close': '319.4100', '5. volume': '73922870'}, '2025-07-16': {'1. open': '312.8000', '2. high': '323.5000', '3. low': '312.6200', '4. close': '321.6700', '5. volume': '97284786'}, '2025-07-15': {'1. open': '319.6750', '2. high': '321.2000', '3. low': '310.5000', '4. close': '310.7800', '5. volume': '77556346'}, '2025-07-14': {'1. open': '317.7300', '2. high': '322.5986', '3. low': '312.6700', '4. close': '316.9000', '5. volume': '78043430'}, '2025-07-11': {'1. open': '307.8900', '2. high': '314.0900', '3. low': '305.6500', '4. close': '313.5100', '5. volume': '79236442'}, '2025-07-10': {'1. open': '300.0500', '2. high': '310.4800', '3. low': '300.0000', '4. close': '309.8700', '5. volume': '104365271'}, '2025-07-09': {'1. open': '297.5500', '2. high': '300.1500', '3. low': '293.5500', '4. close': '295.8800', '5. volume': '75586771'}, '2025-07-08': {'1. open': '297.0000', '2. high': '304.0499', '3. low': '294.3500', '4. close': '297.8100', '5. volume': '103246742'}, '2025-07-07': {'1. open': '291.3700', '2. high': '296.1500', '3. low': '288.7701', '4. close': '293.9400', '5. volume': '131177949'}, '2025-07-03': {'1. open': '317.9900', '2. high': '318.4500', '3. low': '312.7600', '4. close': '315.3500', '5. volume': '58042302'}, '2025-07-02': {'1. open': '312.6300', '2. high': '316.8320', '3. low': '303.8200', '4. close': '315.6500', '5. volume': '119483730'}, '2025-07-01': {'1. open': '298.4600', '2. high': '305.8900', '3. low': '293.2100', '4. close': '300.7100', '5. volume': '145085665'}}}
# with open("alpha_stock.json", "r") as file:
#     stock_price = json.load(file)

daily_sp = stock_price["Time Series (Daily)"]
for day, values in daily_sp.items():
    # print(f"On {day}, tesla stock open with {values["1. open"]} dollar per share")
    the_day = datetime.strptime(day,"%Y-%m-%d").date()
    if the_day == yesterday:
        yesterday_price = float(values["1. open"])
    elif the_day == day_before_yesterday:
        day_before_price = float(values["1. open"])

change = (yesterday_price - day_before_price) / day_before_price
if abs(change) > 0.05:
    day_before_price = yesterday_price
    # print(f"{yesterday} price changes 5%")
    # print("Get News")
percentage_change = change * 100
percentage_change = round(percentage_change, 2)
emoji = ""
if percentage_change < 0 :
    emoji = "🔻"
    percentage_change *= -1
elif percentage_change > 0:
    emoji = "🔺"

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
NEWS_K = "e881e72f7de64c579d8865686c9ec0a7"
# NEWS_K = os.environ.get("NEWS_K")
# NEWS_API = f"https://newsapi.org/v2/everything?q={COMPANY_NAME}&from={yesterday}&to={day_before_yesterday}&language=en&sortBy=popularity&pageSize=3&apiKey={NEWS_K}"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_PARAMETER = {
    "q": COMPANY_NAME,
    "from": yesterday,
    "to":day_before_yesterday,
    "language": "en",
    "sortBy": "popularity",
    "pageSize": 3,
    "apiKey": NEWS_K,
}
news = requests.get(NEWS_ENDPOINT, params=NEWS_PARAMETER, timeout=1200)
# news = news.json()
news = {'status': 'ok', 'totalResults': 376, 'articles': [{'source': {'id': None, 'name': 'Gizmodo.com'}, 'author': 'Mike Pearl', 'title': 'Tesla Is in Trouble with Travis County, Texas', 'description': 'It might lose precious tax rebates.', 'url': 'https://gizmodo.com/tesla-is-in-trouble-with-travis-county-texas-2000686485', 'urlToImage': 'https://gizmodo.com/app/uploads/2025/11/giga-factory-1-1200x675.jpg', 'publishedAt': '2025-11-18T11:00:22Z', 'content': 'In 2020, Travis County, Texas, promised Tesla a wonderful treat: 20 years of tax rebates for the companys massive Texas Gigafactory, which was yet to be built there at the time. Presently, that rebat… [+3682 chars]'}, {'source': {'id': None, 'name': 'Gizmodo.com'}, 'author': 'Matt Novak', 'title': 'Elon Musk Claims Money Won’t Exist in the Future (and Jensen Huang Would Like a Heads Up)', 'description': '"My prediction is that work will be optional," Musk said about the future.', 'url': 'https://gizmodo.com/elon-musk-claims-money-wont-exist-in-the-future-and-jensen-huang-would-like-a-heads-up-2000688307', 'urlToImage': 'https://gizmodo.com/app/uploads/2025/11/GettyImages-2247481493-1200x675.jpg', 'publishedAt': '2025-11-19T20:05:14Z', 'content': 'Elon Musk made some wild claims at the US-Saudi Investment Forum at the Kennedy Center in Washington, D.C. on Wednesday, insisting that his Optimus robot would fix poverty, people wouldn’t have to wo… [+6150 chars]'}, {'source': {'id': 'business-insider', 'name': 'Business Insider'}, 'author': 'Lloyd Lee', 'title': 'Tesla gets approved to launch ride-hailing service in Arizona', 'description': 'Tesla got a permit to operate a ride-hailing service in Arizona as the company continues to expand Robotaxi access to more users.', 'url': 'https://www.businessinsider.com/tesla-robotaxi-expanded-access-arizona-permit-2025-11', 'urlToImage': 'https://i.insider.com/691cf9a9e1a9cbb014de7972?width=1024&format=jpeg', 'publishedAt': '2025-11-18T23:38:45Z', 'content': 'Tesla CEO Elon Musk said on X that the company plans to expand its robotaxi service area in Austin, Texas.Eric Gay/AP\r\n<ul><li>Tesla received a permit to operate a ride-hailing service in Arizona on … [+2316 chars]'}]}

top_articles = f"{STOCK}: {emoji} {percentage_change} %"
for article in news["articles"]:
    top_articles += f"\n\nHeadline: {article["title"]}\nBrief: {article["description"]}"

print(top_articles)
## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.
TWILLIO_API = "682268fad369e4af8092e0c4070c8490"
TWILLIO_SID = "ACbac2fed1a3ca61e53f20e4249c76d097"
TWILLIO_TOKEN = "27313fc398e3f5c15c913aa1805da6fd"
client = Client(TWILLIO_SID, TWILLIO_TOKEN)
message = client.messages.create(
    from_='whatsapp:+14155238886',
    body=top_articles,
    to='whatsapp:+60194442559',
)

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

