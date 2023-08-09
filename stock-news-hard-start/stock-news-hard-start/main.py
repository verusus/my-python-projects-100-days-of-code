import os
import requests
import datetime
from twilio.rest import Client

# twilio recovery code: DC5j0-DNCkemrXfsWDn2Q_fWP0wilEO8wvsbsG8G    # this has nothing with this code

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": "AMR4QKE1YRTEB8KI",
}

response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
response.raise_for_status()
yesterday = datetime.date.today() - datetime.timedelta(days=1)
before_yesterday = datetime.date.today() - datetime.timedelta(days=2)
yesterday_close_val = float(response.json()["Time Series (Daily)"][f"{yesterday}"]["4. close"])
before_yesterday_close_val = float(response.json()["Time Series (Daily)"][f"{before_yesterday}"]["4. close"])
difference_val = abs(yesterday_close_val - before_yesterday_close_val)
difference_percent = difference_val/yesterday_close_val*100

print(difference_percent)
if difference_percent > 0.4:
    news_parameters = {
        "q": COMPANY_NAME,
        "apiKey": "31bb4d1eaa7e426b8048cb3e964bebd0",
    }
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
    news_response.raise_for_status()
    articles = news_response.json()["articles"][:3]

    # setting environment variables for security
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    increasing_icon = "🔺"
    decreasing_icon = "🔻"
    icon_to_send = ""
    sms_list = []
    for article in articles:
        if yesterday_close_val >= before_yesterday_close_val:
            icon_to_send = increasing_icon
        else:
            icon_to_send = decreasing_icon

        sms_text = f"""{COMPANY_NAME}: {icon_to_send}{round(difference_percent)}% Headline: {article['title']}.\nBrief: {article['description']}"""
        sms_list.append(sms_text)

    for sms in sms_list:
        message = client.messages.create(
            body=sms,
            from_='+14143103612',
            to='+212618732987'
        )

        print(message.status)

# Optional: Format the SMS message like this:
"""TSLA: 🔺2% Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. Brief: We at Insider Monkey have 
gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings 
show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash. 
or "TSLA: 🔻5% Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. Brief: We at Insider Monkey 
have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F 
filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus 
market crash. """
