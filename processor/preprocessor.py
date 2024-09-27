import re
import os
from processor.data_checker import DataChecker
from processor.data_processor import DataProcessor


class TrashDataProcessor:
    """하나의 클래스에서 모든 데이터 처리 및 저장 작업을 수행하는 클래스"""

    def __init__(self, url, road_address, detail_address, category, result_filename):
        self.url = url
        self.road_address = road_address
        self.detail_address = detail_address
        self.category = category
        self.result_filename = result_filename

    def check_and_process_data(self):
        """API에서 데이터를 가져와 필요한 필드를 처리"""
        checker = DataChecker(self.url)

        # 필요한 필드만 검증
        keys = ["주소"]
        filtered_data = checker.check_data(keys_to_check=keys)

        # 필드 이름 변경
        processor = DataProcessor(filtered_data)
        keys_to_rename = {"주소": self.road_address}
        processed_df = processor.process_data(keys_to_rename=keys_to_rename)

        return processed_df

    def extract_detail_address(self, row):
        """주소에서 도로명 주소와 상세주소를 분리"""
        match = re.match(r'(.+?길 \d+[-\d]*)(.*)', row[self.road_address])
        if match:
            road_address = match.group(1).strip()  # 도로명 주소
            detail_address = match.group(2).strip() if match.group(2) else ''  # 상세주소
            return road_address, detail_address

        return row[self.road_address], ''  # 기본 주소가 없을 경우

    def process_addresses(self, dataframe):
        """데이터프레임에서 도로명 주소와 상세주소 컬럼을 분리 및 추가"""
        dataframe[self.road_address], dataframe[self.detail_address] = zip(
            *dataframe.apply(self.extract_detail_address, axis=1)
        )
        return dataframe

    def add_trash_category(self, dataframe):
        """쓰레기 카테고리 컬럼을 추가"""
        dataframe[self.category] = self.category
        return dataframe

    def save_to_excel(self, dataframe):
        """가공된 데이터를 엑셀 파일로 저장"""
        output_dir = '../resultFile'
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        output_file = os.path.join(output_dir, self.result_filename)
        dataframe.to_excel(output_file, index=False)
        print(f"File saved at {output_file}")

    def run(self):
        """전체 프로세스를 실행하는 메서드"""
        # 1. 데이터 체크 및 처리
        processed_df = self.check_and_process_data()

        # 2. 도로명 주소와 상세주소 분리
        processed_df = self.process_addresses(processed_df)

        # 3. 쓰레기 카테고리 추가
        processed_df = self.add_trash_category(processed_df)

        # 4. 엑셀 파일로 저장
        self.save_to_excel(processed_df)

