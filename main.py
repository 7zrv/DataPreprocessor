from processor.preprocessor import TrashDataProcessor
from processor.create_result_file import CoordinateProcessor
from url_of_api import UrlOfApi
import os


def main():

    # 1단계: TrashDataProcessor 실행
    url = UrlOfApi.YEONGDEUNGPO_GU
    road_address = "road_name_address"
    detail_address = "detailed_address"
    category = "trash_category"
    result_filename = "영등포구_담배꽁초_쓰레기통3.xlsx"

    # TrashDataProcessor 인스턴스 생성
    processor = TrashDataProcessor(
        url=url,
        road_address=road_address,
        detail_address=detail_address,
        category=category,
        result_filename=result_filename
    )

    # 데이터 처리 및 엑셀 파일 저장 실행
    processor.run()

    # 2단계: CoordinateProcessor 실행
    input_file = os.path.join("resultFile", result_filename)
    output_dir = "resultFile"
    output_filename = result_filename.rstrip('.xlsx') + '_result.xlsx'
    output_file = os.path.join(output_dir, output_filename)

    # CoordinateProcessor 인스턴스 생성
    coord_processor = CoordinateProcessor(input_file, output_dir, output_file)

    # 위도와 경도 처리 및 파일 저장 실행
    coord_processor.run()


if __name__ == "__main__":
    main()
