import random
from django.core.management.base import BaseCommand
from apptree.models import GrpLeafs,Leafs,Branch,Tree
'''
Run    python manage.py load_db

'''

class Command(BaseCommand):
      def handle(self, *args, **options):
        GrpLeafs.objects.all().delete()
        Leafs.objects.all().delete()
        Branch.objects.all().delete()
        Tree.objects.all().delete()

        # create 9 Grp_Leafs
        tot_no_of_grp=9
        grp_leafs = [GrpLeafs(groupLeafsName=f"groupLeaf{index}", Description=f"Leaf Group no.{index}") for index in
                     range(1,tot_no_of_grp)]
        GrpLeafs.objects.bulk_create(grp_leafs)

        # pupulate the leaf with grps. Attach var no of grp for generated leafs
        grp_leaf_qs = GrpLeafs.objects.all()
        leafs_lis = []
        brnch_id = 0
        chg_grp_afer = 3        # use the grp for 5 times then switch to next grp
        Grp_occurrence = 0
        tot_no_of_leafs=25                            #257
        for k in range(0, tot_no_of_leafs):
            Grp_occurrence += 1
            if Grp_occurrence > chg_grp_afer:
                brnch_id += 1
                if brnch_id == len(grp_leaf_qs): brnch_id = 0
                Grp_occurrence = 1
            leaf = Leafs(name=f"leaf{k}", noOfpaper=random.randint(20, 300), leafgroupfrk=grp_leaf_qs[brnch_id])
            leafs_lis.append(leaf)
        Leafs.objects.bulk_create(leafs_lis)

        # create  Branch and insert grp_leaf in every Branch
        tot_no_of_branches=10                                 #126
        use_grp_inx = 0
        branches = []
        for branch_id in range(0, tot_no_of_branches):
            branches.append(
                Branch(name=f"branch{branch_id}", length=random.randint(27, 62), branchleafgroupfrk=grp_leaf_qs[use_grp_inx]))
            use_grp_inx += 1
            if use_grp_inx == len(grp_leaf_qs): use_grp_inx = 0

        Branch.objects.bulk_create(branches)

        # create n Tree  and insert many branches every Tree
        branches = Branch.objects.all()
        trees = []
        br_inx_to_use = 0
        tot_br_per_tree=3                       #19
        tot_no_of_trees=3                       #4
        for tr in range(tot_no_of_trees):
            for br in range(0, tot_br_per_tree * tr):       # make var no of branches for each tree
                trees.append(Tree(name=f"tree{tr}", orgination=f"orgination{tr}", branchesfrk=branches[br_inx_to_use]))
                br_inx_to_use += 1
                if br_inx_to_use == len(branches): br_inx_to_use = 0
        Tree.objects.bulk_create(trees)

