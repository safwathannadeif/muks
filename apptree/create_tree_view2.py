# from django.shortcuts import render

# Create your views here. Create Tree
# views.py

from django.http import HttpResponse
from rest_framework import status
from rest_framework.views import APIView

from apptree.do_Base64_ascii_parse import Base64_ASCII_Parser
from apptree.extract_tree2 import extract_cli2, Rotate
from apptree.models import GrpLeafs, Leafs, Tree, Branch


def create_grp(*args):
    grp_db_r = GrpLeafs.objects.create(groupLeafsName=args[0], Description=args[1])
    return grp_db_r


def create_leaf_grp(grp_ins, *args):
    leaf_db_r = Leafs.objects.create(leafgroupfrk=grp_ins, name=args[0], noOfpaper=args[1])
    return (leaf_db_r)


def create_br(grp_ins, *args):
    br_db_r = Branch.objects.create(branchleafgroupfrk=grp_ins, name=args[0], length=args[1])
    return (br_db_r)


def create_tr(br_ins, *args):
    tr_db_r = Tree.objects.create(branchesfrk=br_ins, name=args[0], orgination=args[1])
    return tr_db_r


class Create_tree_B64(APIView):
    """
    A view that can accept POST requests with special jSON content. create tree
    """
    rotate = Rotate()
    parser_classes = [Base64_ASCII_Parser]

    def post(self, request, format=None):
        rotate = Rotate()
        # parser_classes = [PlainTextParser]
        pr = Base64_ASCII_Parser()
        rjson = pr.parse(request)
        # print(rjson)
        f_l = extract_cli2(rjson)
        # grp
        for g in f_l.grp_lis:
            grp_r = create_grp(g["groupLeafsName"], g["Description"])
            rotate.add_grp_db(grp_r)
            print(grp_r)
        # leaf
        for lf in f_l.leaf_lis:
            leafgroupfrk_ins = rotate.next_grp_db()
            leaf_db_ret = create_leaf_grp(leafgroupfrk_ins, lf["name"], lf["noOfpaper"])
            print(leaf_db_ret)

        # branch
        for br in f_l.branch_lis:
            branchleafgroupfrk_ins = rotate.next_grp_db()
            br_db_ret = create_br(branchleafgroupfrk_ins, br["name"], br["length"])
            print(br_db_ret)
            rotate.add_br_db(br_db_ret)
            # tree
        for tr in f_l.tree_lis:
            branchleafgroupfrk_ins = rotate.next_br_db()
            tr_db_ret = create_tr(branchleafgroupfrk_ins, tr["name"], tr["orgination"])
            print(tr_db_ret)

        # str_to_cli = json.dumps(rjson, indent=2)
        # print("Resp to cli:\n",rjson)
        return HttpResponse(rjson, status=status.HTTP_200_OK)  ### instance.delete)
