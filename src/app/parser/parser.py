from .model import BaseParser, KworkOrder
from typing import Tuple
from bs4 import BeautifulSoup
import requests
from requests import Response
import re
from typing import Tuple

from database.models import Work

import json

from utils import to_file


class Parser(BaseParser):
    def __init__(self, category: int, start_page: int = 1) -> None:
        self._url = "https://kwork.ru/projects"
        self._headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
        }
        self._params = {}

        self._current_category = category
        self._current_page = start_page
        self._max_page = None

        self._current_page_data = {}

        # Init params
        self.add_param("page", start_page)
        self.add_param("fc", category)

    # Getters / Setters
    def set_current_page(self, value):
        self.update_param('page', value)
        self._current_page = value

    def get_current_page(self) -> int:
        return self._current_page

    # Properties
    current_page = property(
        fget=get_current_page,
        fset=set_current_page,
    )

    # Methods
    def add_param(self, key: str, value: str) -> None:
        self._params[key] = value

    def update_param(self, key: str, value: str) -> None:
        self._params[key] = value

    def save_data(self, data: object) -> None:
        self._current_page_data[self._current_page] = data

    def get_page(self) -> Tuple[Response, int]:
        response = requests.get(
            url=self._url,
            headers=self._headers,
            params=self._params,
        )
        return response, response.status_code
    
    def get_page_data(self, page_text: str) -> object:
        soup = BeautifulSoup(page_text, 'html.parser')
        script = soup.find_all('script')[11]
        data = re.sub(
            r'^.*?window\.stateData=',
            'window.stateData=',
            script.text, flags=re.DOTALL
        ).replace("window.stateData=", "")[:-1]
    
        return json.loads(data)["pagination"]
    

    # REWORK
    async def save(self, kwork):
        work = await Work.get_or_none(id=int(kwork["id"]))
        if work is None:
            await Work.create(
                category=int(kwork["category_id"]),
                status=kwork["status"],
                name=kwork["name"],
                description=kwork["description"],
                price=float(kwork["priceLimit"]),
                possible_price=float(kwork["possiblePriceLimit"]),
                kwork_count=kwork["kwork_count"],
                projects=0,
                hired_precent=kwork["user"]["data"]["wants_hired_percent"],
                max_days=kwork["max_days"],
                date_create=kwork["date_active"],
                date_expire=kwork["date_expire"],
                language=kwork["lang"],
                link=f"https://kwork.ru/projects/{kwork["id"]}/view"
            )

        

    async def parse_all(self):
        page, status_code = self.get_page()
        page_data = self.get_page_data(page.text)
        kworks = page_data["data"]

        # Set max_page if is None
        if self._max_page is None:
            self._max_page = page_data["last_page"]

        # Logs
        print(f"{'✅' if status_code == 200 else '❌'} [{status_code}] page {self._current_page}/{self._max_page}")

        self.current_page = self.current_page + 1

        if self.current_page == self._max_page:
            self.current_page = 1
            return
        
        for kwork in kworks:
            await self.save(kwork)

        await self.parse_all()
