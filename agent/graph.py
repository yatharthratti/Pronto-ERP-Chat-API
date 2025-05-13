from langchain_groq import ChatGroq
from langchain_core.tools import tool
import requests
import xml.etree.ElementTree as ET
from langgraph.prebuilt import create_react_agent
from agent.tools import ProntoTools


model = ChatGroq(
    model="qwen-qwq-32b",
    temperature=0,
    max_tokens=2000,
    timeout=None,
    max_retries=2,
    api_key="x"
)


@tool
def get_access_token() -> str:
    """Retrieves an authentication access token for Pronto ERP API access."""
    try:
        url = "https://xi.testing-dc4.prontocloud.com.au/pronto/rest/dem.ai_api/login"
        headers = {
            "X-Pronto-username": "aigen_user",
            "X-Pronto-Password": "fb785+0ee9D7DF0C457be",
            "X-Pronto-Content": "application/json",
        }
        form_data = {
            "user name": "aigen_user",
            "password": "fb785+0ee9D7DF0C457be",
        }
        response = requests.post(url, headers=headers, data=form_data)
        response.raise_for_status()
        root = ET.fromstring(response.text)
        token_element = root.find("token")
        return token_element.text.strip() if token_element is not None else ""
    except Exception as e:
        return f"Error retrieving access token: {str(e)}"

@tool
def get_sales_orders(
    access_token: str,
    territory_code: str = ""
) -> str:
    """Retrieves active sales orders with minimal data."""
    try:
        url = "https://xi.testing-dc4.prontocloud.com.au/pronto/rest/dem.ai_api/api/SalesOrderGetSalesOrders_V2"
        headers = {
            "X-Pronto-Token": access_token,
            "Content-Type": "application/json"
        }
        payload = {
            "SalesOrderGetSalesOrdersRequest": {
                "Parameters": {
                    "Limit": "25" 
                },
                "Filters": {
                    "TerritoryCode": {"Like": territory_code}
                },
                "RequestFields": {
                    "SalesOrders": {
                        "SalesOrder": {
                            "Count": "",
                            "SOOrderNo": "",
                            "StatusCode": "",
                            "TerritoryCode": "",
                            "OperatorCode": "",
                            "SourceCode": ""
                        }
                    }
                }
            }
        }
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.text
    except Exception as e:
        return f"Error retrieving sales orders: {str(e)}"


pronto_tools = ProntoTools()


inventory_tools = [
    get_access_token,
    pronto_tools.get_item_prices,
    pronto_tools.get_item_attributes,
    pronto_tools.get_all_item_prices,
    pronto_tools.get_item_warehouses,
    get_sales_orders
]

# Define the ProntoAgent class
class ProntoAgent:
    def __init__(self):
        self.graph = create_react_agent(model, tools=inventory_tools)

    def get_graph(self):
        return self.graph


pronto_agent = ProntoAgent()