import requests #importing this module to get the data from the API

def get_fund_data(code):
    url=f"https://api.mfapi.in/mf/{code}" # api link with the exact code of the scheme i am trying to target

    response=requests.get(url)# using this function to actually ask the server to send me the data and store in "response"

    print(f"server response for code({code}):",response.status_code)  #200: access granted, 404: server not found

    data=response.json()# java script object notation to actually convert raw uninary bytes, into string , basically then converting to dictionary for structured way of use
    # print(data["meta"]["scheme_name"])

    # to get the history of pricing data , which is stored in the form of list, with each index as a dictionary itself:

    prices=data["data"]
    print(f"total no.of records for code({code}):",len(prices))
    print("LATEST ENTRY:",prices[0])

    return data

