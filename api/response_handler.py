from rest_framework import status
from rest_framework.response import Response


class CommonResponse(Response):
    def __init__(self, status_code, message, data, code=None):
        if not code:
            code = '%s%s' % (str(status_code), '0000')
        response = {
            'code': str(code),
            'message': message,
            'payload': data
        }
        super().__init__(status=status_code, data=response)
