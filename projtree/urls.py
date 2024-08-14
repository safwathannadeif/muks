
from django.urls import path, include

from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path("admin/", admin.site.urls),
    path("tree_api/", include('apptree.urls')),      # at http://127.0.0.1:8000/api/test1

]
'''
 httpx.get("http://127.0.0.1:8000/tree_api/all_tree/")
 httpx.get("http://127.0.0.1:8000/tree_api/filter_tree/?treename=tree1&no_of_Leaf_gt= 120")
 httpx.post("http://127.0.0.1:8000/tree_api/del_leafs/",data={"treename" : "tree1","leaf_name":"leaf25"})
 httpx.post("http://127.0.0.1:8000/tree_api/upd_branch/",data={"treename" : "tree2","branch_name":"branch3","upd_length":50,
                                                                     "upd_name":"branch33"})                             
 '''