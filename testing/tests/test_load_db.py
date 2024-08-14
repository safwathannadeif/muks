import random
from unittest import TestCase

from django.core.management.base import BaseCommand
from apptree.models import GrpLeafs,Leafs,Branch,Tree
'''
 python manage.py test testing.tests.test_load_db

where 
'''

class Load_Tree_TestCase(TestCase):
    def setUp(self):
        pass

    def test_load_test_db(self):
            GrpLeafs.objects.all().delete()
            Leafs.objects.all().delete()
            Branch.objects.all().delete()
            Tree.objects.all().delete()

            # create 5 Grp_Leafs
            grp_leafs = [GrpLeafs(groupLeafsName=f"groupLeaf{index}", Description=f"Leaf Group no.{index}") for index in
                         range(1, 9)]
            GrpLeafs.objects.bulk_create(grp_leafs)

            # pupulate the  leaf with grps. Attach var no pf grp fot generated leafs
            grp_leaf_qs = GrpLeafs.objects.all()
            leafs_lis = []
            i = 0
            tot_per_grp = 5
            occurrence = 0
            for k in range(0, 257):
                occurrence += 1

                if occurrence > tot_per_grp:
                    i += 1
                    if i == len(grp_leaf_qs): i = 0
                    occurrence = 1
                leaf = Leafs(name=f"leaf{k}", noOfpaper=random.randint(20, 300), leafgroupfrk=grp_leaf_qs[i])
                leafs_lis.append(leaf)
            Leafs.objects.bulk_create(leafs_lis)

            # create  Branch and insert grp_leaf in every Branch
            use_inx=0
            branches=[]
            for i in range(1, 126):
                branches.append(Branch(name=f"branch{i}",length=random.randint(27, 62), branchleafgroupfrk=grp_leaf_qs[use_inx]))
                use_inx += 1
                if use_inx == len(grp_leaf_qs): use_inx = 0

            Branch.objects.bulk_create(branches)

            # create n Tree  and insert many branches every Tree
            branches = Branch.objects.all()
            trees = []
            l = 0
            tot_br=19
            treeNo=1
            for tr in range(4):
                    for br in range(1,tot_br*tr):
                        trees.append(Tree(name=f"tree{tr}", orgination=f"orgination{tr}", branchesfrk=branches[l]))
                        l +=1
                        if  l  == len(branches): l=0
            Tree.objects.bulk_create(trees)

