import json
import os

import requests
from url_of_api import UrlOfApi

from dotenv import load_dotenv

load_dotenv('./.env')
MAP_API_KEY = os.environ.get("KAKAO_API_KEY")

def addr_lat_lon(address):
    url = UrlOfApi.KAKAO_MAP_API + address
    headers = {"Authorization": "KakaoAK " + MAP_API_KEY}

    response = requests.get(url, headers=headers)
    json_response = response.json()

    # 주소 정보가 존재하는지 확인
    if json_response['documents']:
        address_xy = json_response['documents'][0]['address']
        # address_xy가 None인지 체크
        if address_xy is not None:
            return float(address_xy['y']), float(address_xy['x']) # 위도, 경도 반환
        else:
            return None, None
    else:
        print(f"주소 '{address}'에 대한 결과가 없습니다.")

    return None, None  # 주소가 없거나 유효하지 않을 경우





