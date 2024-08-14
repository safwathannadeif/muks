from apptree.json4tree import MkTreeJson
from apptree.models import Tree


def prefetch_and_filter(treename,no_of_Leaf_gt):
    mkTreeJson = MkTreeJson()
    out_all = []
    tree_qs = (Tree.objects.filter(name=treename)
               .prefetch_related('branchesfrk__branchleafgroupfrk__groupleafs'))
    for tree in tree_qs:
        mkTreeJson.add_barnch(tree.name, tree.orgination, tree.branchesfrk.name, tree.branchesfrk.length)
        out_leaf_lis = [({"name": leaf.name, "noOfpaper": leaf.noOfpaper}) for leaf in
                        tree.branchesfrk.branchleafgroupfrk.groupleafs.all() if leaf.noOfpaper > no_of_Leaf_gt]
        mkTreeJson.add_leaf_grp(out_leaf_lis, tree.branchesfrk.branchleafgroupfrk.groupLeafsName,tree.branchesfrk.branchleafgroupfrk.Description)
    mkTreeJson.end_json()