import requests
import json
import pandas as pd
from url_of_api import UrlOfApi
from data_checker import DataChecker
from data_processor import DataProcessor

# API URL 선택
url = UrlOfApi.YEONGDEUNGPO_GU.value

checker = DataChecker(url)

checker.check_data()

# 원하는 필드만 확인
keys = ["동명", "주소"]
filtered_data = checker.check_data(keys_to_check=keys)

print(filtered_data)

# 4. DataProcessor 클래스 인스턴스 생성
processor = DataProcessor(filtered_data)

# 5. 데이터 가공 (필드 이름 변경 예: '설치장소(상호명)' -> '상세주소')
keys_to_rename = {
    "설치주소": "도로명주소",
    "위  치": "상세주소"
}

# 6. 가공된 데이터 얻기
processed_df = processor.process_data(keys_to_rename=keys_to_rename)

print(processed_df)

# 7. 가공된 데이터를 엑셀 파일로 저장
#processor.save_to_excel(processed_df, "road_and_detail_address.xlsx")