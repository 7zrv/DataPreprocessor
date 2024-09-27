from enum import Enum

class UrlOfApi():

    #################### 카카오 오픈 api ########################
    KAKAO_MAP_API = "https://dapi.kakao.com/v2/local/search/address.json?query="



    ##################### 공공 데이터 관련 api url####################

    # 서울특별시 중랑구_담배꽁초쓰레기통
    JUNGNANG_GU = (
        "https://api.odcloud.kr/api/15103187/v1/uddi:9128d7f0-d389-4cb7-a89c-95037206da2e"
        "?serviceKey=6ocvfqmViKN%2Bfoy%2FxYMeBpRGaw%2BcBxvUMTU5%2B6VZkUh6DsjaNh7dMv46EqL3"
        "%2F5w6WW8dWCWkdO7gOVU8g2avxw%3D%3D&page=1&perPage=200"
    )

    # 서울특별시 양천구_담배꽁초쓰레기통
    YANGCHEON_GU = (
        "https://api.odcloud.kr/api/15104425/v1/uddi:dc6901e7-c26b-4afa-aeac-806996d6bef6"
        "?serviceKey=6ocvfqmViKN%2Bfoy%2FxYMeBpRGaw%2BcBxvUMTU5%2B6VZkUh6DsjaNh7dMv46EqL3"
        "%2F5w6WW8dWCWkdO7gOVU8g2avxw%3D%3D&page=1&perPage=30"
    )

    # 서울특별시 동작구_담배꽁초 전용 쓰레기통
    DONGJAK_GU = (
        "https://api.odcloud.kr/api/15102166/v1/uddi:d161fb1e-9485-4228-9d08-c0f4d1a50cee"
        "?serviceKey=6ocvfqmViKN%2Bfoy%2FxYMeBpRGaw%2BcBxvUMTU5%2B6VZkUh6DsjaNh7dMv46EqL3"
        "%2F5w6WW8dWCWkdO7gOVU8g2avxw%3D%3D&page=1&perPage=30"
    )

    #종로구 담배꽁초 쓰레기통
    JONGRO_GU = (
        "https://api.odcloud.kr/api/15102250/v1/uddi:8d03feef-5b39-435d-b423-9f9842bfdce3?serviceKey=6ocvfqmViKN%2Bfoy%2FxYMeBpRGaw%2BcBxvUMTU5%2B6VZkUh6DsjaNh7dMv46EqL3"
        "%2F5w6WW8dWCWkdO7gOVU8g2avxw%3D%3D&"
        "page=1&perPage=100"
    )

    GANGNAM_GU = (
        "https://api.odcloud.kr/api/15103349/v1/uddi:06daef13-9cbe-463d-b7b4-b80b1b3ab815?serviceKey=6ocvfqmViKN%2Bfoy%2FxYMeBpRGaw%2BcBxvUMTU5%2B6VZkUh6DsjaNh7dMv46EqL3%2F5w6WW8dWCWkdO7gOVU8g2avxw%3D%3D&page=1&perPage=100"
    )

    YEONGDEUNGPO_GU = (
        "https://api.odcloud.kr/api/15103114/v1/uddi:601f96bb-8d30-4e78-90b4-bc8be09c9b9b?serviceKey=6ocvfqmViKN%2Bfoy%2FxYMeBpRGaw%2BcBxvUMTU5%2B6VZkUh6DsjaNh7dMv46EqL3%2F5w6WW8dWCWkdO7gOVU8g2avxw%3D%3D&page=1&perPage=300"
    )
    #일반쓰레기통 데이터 url

