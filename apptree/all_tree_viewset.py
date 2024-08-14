from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse, HttpResponseNotFound
from rest_framework import status, viewsets
# from rest_framework.permissions import DjangoObjectPermissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.decorators import action

from apptree.create_tree_view2 import Create_tree_B64
from apptree.json4tree import MkTreeJson
from apptree.models import Tree, Leafs, Branch
from apptree.all_tree_serializer import TreeSerializer

#@action(detail=False, methods=["get"],url_path="/tree_all")
'''
 httpx.get("http://127.0.0.1:8000/tree_api/all_tree/")
 httpx.get("http://127.0.0.1:8000/tree_api/filter_tree/?treename=tree1&no_of_Leaf_gt= 120")
 httpx.post("http://127.0.0.1:8000/tree_api/del_leafs/",data={"treename" : "tree1","leaf_name":"leaf25"})
 httpx.post("http://127.0.0.1:8000/tree_api/upd_branch/",data={"treename" : "tree2","branch_name":"branch3","upd_length":50,
                                                                     "upd_name":"branch33"})                             
 '''
class Tree_ALL_View(viewsets.ViewSet):
    def chek_inp_parms(self,tree,leaf_no):
        pass

    #http://127.0.0.1:8000/tree_api/all_tree/
    def get_all(self, request, *args, **kwargs):
        print("inside Tree_ALL_View get request====>")
        tree_qs_all = Tree.objects.prefetch_related('branchesfrk__branchleafgroupfrk__groupleafs')
        serl_out = TreeSerializer(tree_qs_all, many=True)
        # permission_classes = [DjangoObjectPermissions]
        # queryset = Tree.objects.all()
        # tree_qs_filter = Tree.objects.filter(name="tree2").prefetch_related(
        #     'branchesfrk__branchleafgroupfrk__groupleafs')
        return Response(serl_out.data, status=status.HTTP_201_CREATED)

    # For Extra GET Requests
    #http://127.0.0.1:8000/tree_api/filter_tree/?treename=tree1&no_of_Leaf_gt=260
    def get_with_filter (self, request):
        ContentType.objects.clear_cache()
        treename=request.GET['treename']
        print(treename)
        no_of_Leaf_gt = request.GET['no_of_Leaf_gt']
        print(no_of_Leaf_gt)
        no_of_Leaf_gt_int = int(no_of_Leaf_gt)
        mkTreeJson = MkTreeJson()
        out_all = []
        tree_qs = (Tree.objects.filter(name=treename)
                      .prefetch_related('branchesfrk__branchleafgroupfrk__groupleafs'))
        for tree in tree_qs:
                print("treenam:",tree.name)
                # get the branch attributes
                print("tree.branchesfrk.name:", tree.branchesfrk.name)
                mkTreeJson.add_barnch(tree.name, tree.orgination, tree.branchesfrk.name, tree.branchesfrk.length)
                out_leaf_lis=[]
                out_leaf_lis = [({"name": leaf.name, "noOfpaper": leaf.noOfpaper}) for leaf in
                                tree.branchesfrk.branchleafgroupfrk.groupleafs.all() if leaf.noOfpaper > no_of_Leaf_gt_int]
                if len(out_leaf_lis) == 0 : continue
                print ("nO of collected list for leafs after filter:", len(out_leaf_lis) )
                mkTreeJson.add_leaf_grp(out_leaf_lis, tree.branchesfrk.branchleafgroupfrk.groupLeafsName,
                                        tree.branchesfrk.branchleafgroupfrk.Description)
        #mkTreeJson.end_json()

        return Response(mkTreeJson.get_all(),status=status.HTTP_302_FOUND)

    # http://127.0.0.1:8000/tree_api/del_leafs_from_tree/?treename=tree1&Leaf_name=260
    def do_del_leafs(self,request):
        queryDict= request.data
        treename= queryDict.get("treename")
        leaf_name=queryDict.get("leaf_name")
        leaf_2_del_lis=[]
        tree_qs = (Tree.objects.filter(name=treename)
                   .prefetch_related('branchesfrk__branchleafgroupfrk__groupleafs'))
        for tree in tree_qs:
            leaf_2_del_lisx = [ ({"id":ll.id,"name": ll.name, "noOfpaper": ll.noOfpaper})
                               for ll in tree.branchesfrk.branchleafgroupfrk.groupleafs.all()       # reverse using the related name groupleafs
                               if ll.name == leaf_name ]
            #if len(leaf_2_del_lisx)  > 0:  leaf_2_del_lis.append(leaf_2_del_lisx)       # use extend and no need for list inside list
            if len(leaf_2_del_lisx) > 0:  leaf_2_del_lis.extend(leaf_2_del_lisx)  # use extend and no need for list inside list

            #print (len(leaf_2_del_lis))
            # for l in tree.branchesfrk.branchleafgroupfrk.groupleafs.all() :
            #     if leaf_name == l.name :  print(l.name)
        if len(leaf_2_del_lis) == 0 : return Response({"tree":treename, "leaf":leaf_name, "error" :"leaf Not Found"},status=status.HTTP_410_GONE)  ### instance.delete
        for l1 in leaf_2_del_lis:
              leaf2delete = Leafs.objects.get(id=l1["id"])
              #print(leaf2delete)
              leaf2delete.delete()
        #bulk is better del https://code.djangoproject.com/ticket/9519
        tree={"tree_name": treename,"leaf_deleted":leaf_2_del_lis}
        return Response(tree,status=status.HTTP_202_ACCEPTED)

    def do_upd_branch (self, request):
        queryDict = request.data
        treename = queryDict.get("treename")
        branchname = queryDict.get("branch_name")
        upd_length_s=queryDict.get("upd_length")
        upd_length=int(upd_length_s)
        upd_name=queryDict.get("upd_name")
        #branch_2_upd_lis = []
        tree_qs = (Tree.objects.filter(name=treename)
                   .prefetch_related('branchesfrk'))
        # for tt in tree_qs:
        #   print(tt.name,tt.branchesfrk.name,tt.branchesfrk.length)        #forward using the FK branchesfrk

        branch_2_upd_lisx = [{"id": treex.branchesfrk.id, "name": treex.branchesfrk.name}
                             for treex in tree_qs.all() if treex.branchesfrk.name == branchname]    ##forwrd using the FK branchesfrk
        #if len(branch_2_upd_lisx) > 0:  branch_2_upd_lis.append(branch_2_upd_lisx)

        if len(branch_2_upd_lisx) == 0:
            return Response({"tree": treename, "branch": branchname, "error": "Branch Not Found"},
                            status=status.HTTP_410_GONE)  ### instance.delete
        branch2upd = None
        for ix in branch_2_upd_lisx:
            id_upd= ix["id"]
            branch2upd = Branch.objects.filter(id=id_upd).update(name=upd_name,length=upd_length) #more efficient: one SQL update statement, and is much faster
            #branch2upd.save()
            #branch2upd = Branch.objects.get(id=ix["id"])
            #branch2upd.length = upd_length
            #branch2upd.save()

        return Response({"tree": treename, "branch": upd_name ,"length":upd_length} ,status=status.HTTP_200_OK)  ### instance.delete