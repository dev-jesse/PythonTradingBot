import logging
import typing

import requests

logger = logging.getLogger()


class BitmexConnector:
    def __init__(self, private_key: str, public_key: str):
        self.base_url = "https://www.bitmex.com/api/v1"
        self.wss_url = "wss://ws.bitmex.com/realtime"

        self.public_key = public_key
        self.private_key = private_key

    def _make_requests(self, method: str, endpoint: str, data: typing.Dict):
        if method == "GET":
            try:
                response = requests.get(self.base_url + endpoint, params=data)
            except Exception as e:
                logger.error(
                    "Connection error while making %s request to %s: %s",
                    method, endpoint, e)
                return None
        elif method == "POST":
            try:
                response = requests.post(self.base_url + endpoint, params=data)
            except Exception as e:
                logger.error(
                    "Connection error while making %s request to %s: %s",
                    method, endpoint, e)
                return None
        elif method == "DELETE":
            try:
                response = requests.delete(self.base_url + endpoint,
                                           params=data)
            except Exception as e:
                logger.error(
                    "Connection error while making %s request to %s: %s",
                    method, endpoint, e)
                return None
        else:
            raise ValueError()

        if response.status_code == "200":
            return response.json()
        else:
            logger.error(
                "Error while making %s request to %s: %s (error code %s)",
                method, endpoint, response.json(), response.status_code)
            return None

    def get_contracts(self):
        exchange_info = self._make_requests("GET", "/instrument", {})
        contracts = []
        if exchange_info is not None:
            for contract in exchange_info:
                contracts.append(contract["symbol"])

        return contracts
