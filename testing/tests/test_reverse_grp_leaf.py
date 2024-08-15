from django.test import TestCase

from apptree.models import GrpLeafs, Leafs
from testing.tests.test_load_db import Load_Tree_TestCase


# Run::  ++++>  python manage.py test testing.tests.test_reverse_grp_leaf
# from  Stack Overflow
# https://stackoverflow.com/questions/50193842/django-prefetch-related-with-reverse-foreign-key-lookup
class Tree_list_leaf_TestCase(TestCase):
    def setUp(self):
        load = Load_Tree_TestCase()
        load.test_load_test_db()

    def test_tree_list(self):
        # straight forward
        print("start testing")
        leaf_with_frkey = Leafs.objects.all()
        for lf in leaf_with_frkey:
            ## print("ForwardFromFkey:",  lf.leafgroupfrk,lf.noOfpaper)
            # #### forward group attributes from Leaf Foreign key #### #
            ## Pass it it works
            pass

        grp_Of_leaf_qs = GrpLeafs.objects.prefetch_related('groupleafs')
        print(grp_Of_leaf_qs.query)
        for grp in grp_Of_leaf_qs:
            grpName = grp.groupLeafsName
            print("Group====>", grpName)
            leaf_from_one_grp_qs = grp.groupleafs.all()  # prefetch_related to make reverse:
            print(leaf_from_one_grp_qs.query)
            #### # reverse Django here means get the leafs attributes from Group without any hit the database ##############
            for lf in leaf_from_one_grp_qs:
                print("Leaf====>", lf.name, "->", lf.noOfpaper)
