from unittest import TestCase

from django.db import models
from django.db.models import Prefetch

from apptree.models import Tree, Branch
from testing.tests.test_load_db import Load_Tree_TestCase

'''
Run:::   ->>>  python manage.py test testing.tests.test_prefetch_with_filters
'''


class Grp_leaf_TestCase(TestCase):
    def setUp(self):
        load = Load_Tree_TestCase()
        load.test_load_test_db()

    def test_tree_list(self):
        # tree_qs = Tree.objects.prefetch_related(models.Prefetch('branchesfrk',
        #                     queryset=Branch.objects.filter(models.Q(name="branch1") | models.Q(name="branch2"))))

        tree_qs_all = Tree.objects.prefetch_related(Prefetch('branchesfrk__branchleafgroupfrk__groupleafs',
                                                             queryset=Branch.objects.filter(
                                                                 models.Q(name="branch1") | models.Q(name="branch2"))))

# branchleafgroupfrk__groupleafs')

#
# '''
#         grp_qs = GrpLeafs.objects.prefetch_related(
#             models.Prefetch(  "groupleafs", queryset=Leafs.objects.filter( models.Q(noOfpaper__gt= 100) | models.Q(noOfpaper=90)) ))
#         for grp in grp_qs:
#             print(grp.groupLeafsName)
#             leaf_from_one_grp_qs = grp.groupleafs.all()  # prefetch_related to make reverse:
#             print(leaf_from_one_grp_qs.query)
#             print("...." , leaf_from_one_grp_qs, "...........")
#
#             #### # reverse Django here means get the leafs attributes from Group without any hit the database ##############
#             for lf in leaf_from_one_grp_qs:
#                 print("Leaf====>", lf.name, "->", lf.noOfpaper)
# '''
