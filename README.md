Tree is a natural  one to many relationship chain. One Tree >>Many Branches>> one Branch, Many Group Of  Leafs >>  One Group Many Leafs.
Of curse  there are many tress: https://github.com/user-attachments/assets/e5345295-8740-4d7d-ab45-65b5389bc867

Django Model: Classes: 
		GrpLeafs , 
		Leafs ForeignKey=GrpLeafs and related_name=groupleafs ,
		Branch ForeignKey=GrpLeafs,
		Tree  ForeignKey=Branch
Refer to model classes 
				
Prefetch is used so with one hit to db to query all the hierarchy, captured and represented

Views and Urls:
tree_api/create_tree/				create_tree_view2.Create_tree_B64.as_view() ,
tree_api/all_tree/				 		all_tree_viewset.Tree_ALL_View.as_view({"get":"get_all"})) ,
tree_api/filter_tree/ 				all_tree_viewset.Tree_ALL_View.as_view({"get":"get_with_filter"})) ,
tree_api/del_leafs					all_tree_viewset.Tree_ALL_View.as_view({"post":"do_del_leafs"})) ,
tree_api/upd_branch/				all_tree_viewset.Tree_ALL_View.as_view({"post":"do_upd_branch"}))

Client APiIs side: https://github.com/safwathannadeif/httpxcli
