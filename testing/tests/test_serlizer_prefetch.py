import os
import sys
from pprint import pprint

from django.db.models import Q
from django.test import TestCase
from apptree.models import GrpLeafs,Leafs,Branch,Tree
from apptree.all_tree_serializer import TreeSerializer
from testing.tests.test_load_db import Load_Tree_TestCase
#   TO rUN::::  ->> python manage.py test testing.tests.test_serlizer_prefetch
# cle
# sys.stdout = open('C:/Users/Public/py_dev/django/muks/others/output_files/outx.txt', 'w')
class Tree_list_TestCase(TestCase):
    def setUp(self):
        load = Load_Tree_TestCase()
        load.test_load_test_db()

    def test_prefetch_serl(self):
        print("start testing")
        tree_qs_all = Tree.objects.prefetch_related('branchesfrk__branchleafgroupfrk__groupleafs')
        serializer_class = TreeSerializer
        serializer = TreeSerializer(tree_qs_all, many=True)
        # return self.get_paginated_response(self.paginate_queryset(serializer.data))
        pprint (serializer.data)
