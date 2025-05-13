from langchain_core.tools import tool
import requests

class ProntoTools:
    @tool
    def get_item_prices(
        self,
        access_token: str,
        item_code_like: str = "",
        price_region_code_like: str = "",
        type_code_like: str = ""
    ) -> str:
        """Retrieves item pricing information with minimal data."""
        try:
            url = "https://xi.testing-dc4.prontocloud.com.au/pronto/rest/dem.ai_api/api/InvGetItemPrices_V2"
            headers = {
                "X-Pronto-Token": access_token,
                "Content-Type": "application/json"
            }
            payload = {
                "InvGetItemPricesRequest": {
                    "Parameters": {
                        "Limit": "25",
                        "Offset": "0"
                    },
                    "Filters": {
                        "ItemCode": {"Like": item_code_like},
                        "PriceRegionCode": {"Like": price_region_code_like},
                        "TypeCode": {"Like": type_code_like}
                    },
                    "RequestFields": {
                        "ItemPrices": {
                            "ItemPrice": {
                                "ItemCode": "",
                                "PriceRegionCode": "",
                                "WholesalePrice": "",
                                "TypeCode": ""
                            }
                        }
                    }
                }
            }
            response = requests.get(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.text[:1000]
        except Exception as e:
            return f"Error retrieving item prices: {str(e)}"

    @tool
    def get_item_attributes(
        self,
        access_token: str,
        item_code: str = "",
        attribute_id: str = "",
        type_code_like: str = ""
    ) -> str:
        """Retrieves product attribute information with minimal data."""
        try:
            url = "https://xi.testing-dc4.prontocloud.com.au/pronto/rest/dem.ai_api/api/InvGetItemAttributes_V2"
            headers = {
                "X-Pronto-Token": access_token,
                "Content-Type": "application/json"
            }
            payload = {
                "InvGetItemAttributes": {
                    "RecordLimit": "25",
                    "Parameters": {
                        "ItemCode": item_code,
                        "AttribteID": attribute_id,
                        "Sequence": "",
                        "Limit": "10",
                        "Offset": "0"
                    },
                    "Filters": {
                        "TypeCode": {"Like": type_code_like}
                    },
                    "RequestFields": {
                        "ItemAttributes": {
                            "ItemAttribute": {
                                "AttributeID": "",
                                "AttributeValue": "",
                                "ItemCode": "",
                                "Sequence": "",
                                "TypeCode": ""
                            }
                        }
                    }
                }
            }
            response = requests.get(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.text[:1000]
        except Exception as e:
            return f"Error retrieving item attributes: {str(e)}"

    @tool
    def get_all_item_prices(
        self,
        access_token: str,
        item_code_like: str = "",
        price_region_code_like: str = "",
        type_code_like: str = ""
    ) -> str:
        """Retrieves comprehensive pricing data with minimal filters."""
        try:
            url = "https://xi.testing-dc4.prontocloud.com.au/pronto/rest/dem.ai_api/api/InvGetItemPrices_V2"
            headers = {
                "X-Pronto-Token": access_token,
                "Content-Type": "application/json"
            }
            payload = {
                "InvGetItemPricesRequest": {
                    "Parameters": {
                        "Limit": "25",
                        "Offset": "0"
                    },
                    "Filters": {
                        "ItemCode": {"Like": item_code_like},
                        "PriceRegionCode": {"Like": price_region_code_like},
                        "TypeCode": {"Like": type_code_like}
                    },
                    "RequestFields": {
                        "ItemPrices": {
                            "ItemPrice": {
                                "ItemCode": "",
                                "PriceRegionCode": "",
                                "WholesalePrice": "",
                                "TypeCode": ""
                            }
                        }
                    }
                }
            }
            response = requests.get(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.text[:1000]
        except Exception as e:
            return f"Error retrieving all item prices: {str(e)}"

    @tool
    def get_item_warehouses(
        self,
        access_token: str,
        warehouse_code_like: str = ""
    ) -> str:
        """Retrieves inventory stock levels with minimal data."""
        try:
            url = "https://xi.testing-dc4.prontocloud.com.au/pronto/rest/dem.ai_api/api/InvGetItemWarehouses_V2"
            headers = {
                "X-Pronto-Token": access_token,
                "Content-Type": "application/json"
            }
            payload = {
                "InvGetItemWarehousesRequest": {
                    "RecordLimit": "10",
                    "Parameters": {
                        "ItemCode": {"Like": warehouse_code_like}
                    },
                    "RequestFields": {
                        "ItemWarehouses": {
                            "ItemWarehouse": {
                                "ItemCode": "",
                                "OnHandQty": "",
                                "BackOrdersQty": "",
                                "WarehouseCode": ""
                            }
                        }
                    }
                }
            }
            response = requests.get(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.text[:1000]
        except Exception as e:
            return f"Error retrieving item warehouses: {str(e)}"