import pandas as pd

class DataProcessor:
    def __init__(self, data):
        self.data = data

    def process_data(self, keys_to_rename):
        # 필드 이름 변경
        processed_data = [{keys_to_rename.get(k, k): v for k, v in item.items()} for item in self.data]
        return pd.DataFrame(processed_data)

    def save_to_excel(self, df, filename):
        try:
            # 기존 엑셀 파일 읽기
            existing_df = pd.read_excel(filename, sheet_name='Sheet1')
            # 새 데이터를 기존 데이터와 연결
            combined_df = pd.concat([existing_df, df], ignore_index=True)

            # 통합된 데이터프레임을 같은 파일에 저장
            with pd.ExcelWriter(filename, mode='w', engine='openpyxl') as writer:
                combined_df.to_excel(writer, index=False, sheet_name='Sheet1')
            print(f"데이터가 {filename}에 추가되었습니다.")
        except FileNotFoundError:
            # 파일이 없으면 새 파일 생성
            with pd.ExcelWriter(filename, mode='w', engine='openpyxl') as writer:
                df.to_excel(writer, index=False, sheet_name='Sheet1')
            print(f"{filename}가 새로 생성되었습니다.")
        except Exception as e:
            print(f"엑셀 파일 저장 중 오류가 발생했습니다: {e}")
