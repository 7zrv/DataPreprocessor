import pandas as pd
import requests

# 엑셀 파일 경로
input_file = "resultFile/영등포구_담배꽁초_쓰레기통_result_file.xlsx"
# API URL
url = "http://localhost:8080/api/trashcan"

def send_data_to_api():
    # 엑셀 파일 읽기
    df = pd.read_excel(input_file)

    for _, row in df.iterrows():
        # 각 행을 JSON 형식으로 변환
        data = {
            "roadNameAddress": row['road_name_address'],
            "detailedAddress": row['detailed_address'] if pd.notna(row['detailed_address']) else "",  # 기본값 설정
            "trashCategory": row['trash_category'],
            "latitude": row['latitude'],
            "longitude": row['longitude']
        }

        try:
            # POST 요청 보내기
            response = requests.post(url, json=data)
            response.raise_for_status()  # 요청이 실패하면 예외 발생
            print(f"데이터 전송 성공: {data}")
        except requests.exceptions.RequestException as e:
            print(f"데이터 전송 실패: {data}, 오류: {e}")

if __name__ == "__main__":
    send_data_to_api()
