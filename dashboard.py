import streamlit as st
import requests
from datetime import date

BASE_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="AI Supply Chain Dashboard", layout="wide")
st.title("AI-Based Supply Chain Analytics Dashboard")

menu = st.sidebar.selectbox("Menu", ["Add Sales", "Add Inventory", "Forecast Demand"])

if menu == "Add Sales":
    st.header("Add Sales Data")
    with st.form("sales_form"):
        product_id = st.text_input("Product ID")
        sales_data = st.date_input("Date", value=date.today())
        units_sold = st.number_input("Units Sold", min_value=0)
        market_trend = st.slider("Market Trend Index", 0.0, 1.0, step=0.01)
        price = st.number_input("Price", min_value=0.0, step=0.01)
        submit = st.form_submit_button("Submit Sales")

        if submit:
            payload = {
                "product_id": product_id,
                "date": sales_data.strftime("%Y-%m-%d"),
                "units_sold": int(units_sold),
                "market_trend_index": float(market_trend),
                "price": float(price)
            }
            response = requests.post(f"{BASE_URL}/sales/", json=payload)
            st.success(response.json().get("msg", "Data submitted!"))

elif menu == "Add Inventory":
    st.header("Add Inventory Data")
    with st.form("inventory_form"):
        product_id = st.text_input("Product ID", key="inventory_product")
        current_stock = st.number_input("Current Stock", min_value=0)
        warehouse = st.text_input("Warehouse Location")
        submit = st.form_submit_button("Submit Inventory")

        if submit:
            payload = {
                "product_id": product_id,
                "current_stock": int(current_stock),
                "warehouse": warehouse
            }
            response = requests.post(f"{BASE_URL}/inventory/", json=payload)
            st.success(response.json().get("msg", "Inventory added!"))

elif menu == "Forecast Demand":
    st.header("Demand Forecast and Optimization")
    with st.form("forecast_form"):
        product_id = st.text_input("Product ID", key="forecast_product")
        forecast_date = st.date_input("Forecast Date", value=date.today())
        market_trend = st.slider("Market Trend Index", 0.0, 1.0, step=0.01, key="forecast_trend")
        price = st.number_input("Price", min_value=0.0, step=0.01, key="forecast_price")
        submit = st.form_submit_button("Get Forecast")

        if submit:
            params = {
                "product_id": product_id,
                "date": forecast_date.strftime("%Y-%m-%d"),
                "market_trend_index": market_trend,
                "price": price
            }
            response = requests.post(f"{BASE_URL}/forecast/", params=params)
            if response.status_code == 200:
                result = response.json()
                st.subheader("📊 Forecast Results")
                st.write(f"**Forecasted Demand:** {result['forecasted_demand']} units")
                st.write(f"**Optimized Inventory:** {result['optimized_inventory']} units")
            else:
                st.error("Forecast failed. Please check inputs or try again later.")
