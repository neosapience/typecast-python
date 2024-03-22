class ApiError(Exception):
    def __init__(self, status_code, body) -> None:
        self.status_code = status_code
        self.body = body

    def __str__(self):
        return f'Api error: status: {self.status_code}, body: {self.body}'
