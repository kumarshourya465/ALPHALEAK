from network import get_fund_data
from analytics import process_nav_data

if __name__=="__main__":
    fund_code=["125497","119551","BOGUS_CODE_999999","120503"]

    for val in fund_code:
        try :
            fund_data=get_fund_data(val)
            process_nav_data(fund_data["data"])
        except Exception as e:
            print("WARNING!!!")
            print(f"FUND CODE({val}) HAS FAILED TO PROCESS!!")
            print(e)
            continue
    print("------PROCESS COMPLETE------")

    