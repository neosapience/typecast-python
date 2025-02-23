FROM python:3.13-rc-slim

WORKDIR /app

# 기본 개발 도구 설치
RUN apt-get update && apt-get install -y \
    git \
    curl \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Poetry 설치 (의존성 관리를 위해)
RUN curl -sSL https://install.python-poetry.org | python3 -

# 환경 변수 설정
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PATH="/root/.local/bin:$PATH"

# 프로젝트 의존성 파일 복사
COPY pyproject.toml README.md ./

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-root

# 소스 코드 복사
COPY . .

RUN poetry install --no-interaction --no-ansi

# 개발 서버 실행을 위한 기본 명령
CMD ["poetry", "shell"] 