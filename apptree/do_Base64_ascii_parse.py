# Re-Usable Base64 Parser
import base64
import json

from rest_framework.parsers import BaseParser


class Base64_ASCII_Parser(BaseParser):
    def parse(self, stream, media_type='application/base64', parser_context=None):
        in_str = stream.read()
        string_bytes = base64.b64decode(in_str)
        w_str = string_bytes.decode("ascii")
        data_json_obj = json.loads(w_str)
        # print(data_json_obj)
        return data_json_obj
