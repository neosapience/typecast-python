import os

TYPECAST_API_HOST = "https://api.typecast.ai"


def get_host(host=None):
    if host:  # 파라미터가 있으면 최우선
        return host
    env_host = os.getenv("TYPECAST_API_HOST")  # 환경변수 확인
    return env_host if env_host else TYPECAST_API_HOST  # 환경변수 없으면 기본값


def get_api_key(api_key=None):
    if api_key:  # 파라미터가 있으면 최우선
        return api_key
    return os.getenv("TYPECAST_API_KEY")  # 환경변수 반환
