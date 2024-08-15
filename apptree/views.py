# Create your views here.
# views.py
import base64
import json

from django.http import JsonResponse
from rest_framework.parsers import BaseParser
from rest_framework.viewsets import ModelViewSet

from apptree.models import Tree, Branch, Leafs


# media_type='text/plain' or 'application/base64' the preferd  is base 64
# content-type= 'application/json'
class Base64_ASCII_Parser(BaseParser):
    def parse(self, stream, media_type='application/base64', parser_context=None):
        in_str = stream.read()
        string_bytes = base64.b64decode(in_str)
        w_str = string_bytes.decode("ascii")
        print(w_str)
        data_json = json.loads(w_str)
        return data_json


def create_tree(*args, id_br):
    id = Tree.objects.create(t_name_inx=args[0], origination=args[1], dob=args[2], t2bs=id_br)
    return (id)


def create_branch(*args, id_b2ls):
    id_br = Branch.objects.create(b_name_inx=args[0], strength=args[1], length=args[2], woody=args[3], b2ls=id_b2ls)
    return (id_br)


def create_Leaf(*args):
    id_b2ls = Leafs.objects.create(sbl_name_inx=args[0], color=args[1], density=args[2], no_of_paper=args[3],
                                   smooth_level=args[4])
    return id_b2ls


class B64_parser(ModelViewSet):
    parser_classes = [Base64_ASCII_Parser]

    def post(self, request):
        print("starts post of B64_parser")
        pr = Base64_ASCII_Parser()
        rjson = pr.parse(request)
        print(rjson)

        return JsonResponse(rjson)
