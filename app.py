import streamlit as st
from network import get_fund_data
from analytics import process_nav_data
from analytics import get_summary_data

#setting the page layout, and name
st.set_page_config(page_title="ALPHALEAK: Quant Analytics Engine",layout="wide")

#to create the title
st.title("ALPHALEAK : Quant Analytics Engine")
st.caption("Automated Mutual Fund Performance & Risk Analytics Engine")

#to create the input box
fund_code=st.text_input("Enter The Mutual Fund Code:",placeholder="e.g. 125497")

#creating the button to click and run the things
if st.button("Run Analytics"):
    try:

        fund_data=get_fund_data(fund_code)
        processed_data=process_nav_data(fund_data["data"])
        summary=get_summary_data(processed_data)

        #printing success
        st.success("Analytics Generated Successfully!")
        st.divider()

        #ROW 1 PERFORMANCE METRICS(3 COLUMNS)
        st.subheader("KEY PERFORMANCE INDICATORS")
        col1,col2,col3=st.columns(3)

        with col1:
            st.metric(label="Total_Returns",value=f"{summary["total_return"]*100:.2f}%")
            st.metric(label="Max_Drawdown",value=f"{summary["max_drawdown"]*100:.2f}%")

        with col2:
            st.metric(label="Volatility (Daily)",value=f"{summary["volatility"]*100:.2f}%")
            st.metric(label="Win_Rate",value=f"{summary["win_rate"]*100:.2f}%")

        with col3:
            st.metric(label="Best Single Day",
                      value=f"{summary["best_day"]*100:.2f}%",
                      delta=summary['best_day_date'])
            st.metric(
                label="Worst Single Day", 
                value=f"{summary['worst_day'] * 100:.2f}%", 
                delta=summary['worst_day_date'],
                delta_color="inverse"
            )

        #ROW 2 HISTORICAL NAV CHART
        st.subheader("Historical NAV Movement")
        st.line_chart(processed_data["nav"])

    except Exception as e:
        st.error(f"Failed to process the analytics for the func code{fund_code}.\nPlease check the code and try again!")

