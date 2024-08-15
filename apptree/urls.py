from django.urls import path

from apptree import create_tree_view2, all_tree_viewset

urlpatterns = [
    path("create_tree/", create_tree_view2.Create_tree_B64.as_view()),
    path("all_tree/", all_tree_viewset.Tree_ALL_View.as_view({"get": "get_all"})),
    path("filter_tree/", all_tree_viewset.Tree_ALL_View.as_view({"get": "get_with_filter"})),
    path("del_leafs/", all_tree_viewset.Tree_ALL_View.as_view({"post": "do_del_leafs"})),
    path("upd_branch/", all_tree_viewset.Tree_ALL_View.as_view({"post": "do_upd_branch"}))
]
