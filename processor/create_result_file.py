import os
import pandas as pd
from processor.create_coordinates import addr_lat_lon

class CoordinateProcessor:
    """엑셀 파일에서 주소로 위도와 경도를 추가하고 결과를 저장하는 클래스"""

    def __init__(self, input_file, output_dir, output_file):
        self.input_file = input_file
        self.output_dir = output_dir
        self.output_file = output_file
        self.df = pd.read_excel(input_file)

    def get_coordinates(self, row):
        """각 행에서 주소를 가져와 위도와 경도를 반환"""
        address = row['road_name_address']
        if pd.isna(address):  # 주소가 NaN인 경우 처리
            return None, None
        lat, lon = addr_lat_lon(address)
        return lat, lon

    def process_coordinates(self):
        """위도와 경도 칼럼을 추가하고, NaN 값을 제거"""
        # 위도, 경도 column 추가
        self.df['latitude'], self.df['longitude'] = zip(*self.df.apply(self.get_coordinates, axis=1))

        # 위도 또는 경도가 None인 행 삭제
        self.df = self.df.dropna(subset=['latitude', 'longitude'])

    def add_category(self, category="CIGARETTE"):
        """쓰레기 카테고리 칼럼 추가"""
        self.df['trash_category'] = category

    def save_to_excel(self):
        """결과 데이터를 엑셀 파일로 저장"""
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

        self.df.to_excel(self.output_file, index=False)
        print(f"엑셀 파일이 '{self.output_file}'에 저장되었습니다.")

    def run(self):
        """전체 프로세스 실행"""
        self.process_coordinates()
        self.add_category()
        self.save_to_excel()

# # main.py에서 사용할 수 있도록 아래 코드 작성
# if __name__ == "__main__":
#     input_file = "영등포구_담배꽁초_쓰레기통.xlsx"
#     output_dir = "resultFile"
#     output_file_name = "result_file2.xlsx"
#     output_file = os.path.join(output_dir, output_file_name)
#
#     # CoordinateProcessor 클래스 인스턴스 생성
#     processor = CoordinateProcessor(input_file, output_dir, output_file)
#
#     # 데이터를 처리하고 파일로 저장
#     processor.run()




