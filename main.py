from circle_test import *
from params import params

root_data = "/mnt/c/Users/bennm/Documents/UNI/Year3/Modelling Tissues Project/data"
project_name = "pyABP_delta_tests"
folder_name = f"{root_data}/{project_name}"
# search_grid = pickle.load(open(f"{root_data}/{project_name}/search_grid.p","rb"))
n_delta,n_ep = 6,7
delta_range,ep_range  = (0,0.6),(0.05,0.35)
epsilon,delta = make_param_lists(ep_range,delta_range,n_ep,n_delta)
sg = make_search_grid(["epsilon","delta"],[epsilon,delta],True)
sg = [list(row) for row in sg]
del sg[0:3]
print(sg)
simulation(folder_name,sg,params)

# k2s = [0.4]
# epsilons = [0.05] 
# params["inter_type"] = 1 b
# # k2s = [0.4,0.8,1.2,1.6,2]
# # epsilons = [0.05,0.1,0.15,0.2,0.25,0.3] 
# for k2 in k2s:
# 	for epsilon in epsilons:
# 		params["k2"] = k2
# 		params["epsilon"] = epsilon
# 		folder_name = f"./data/pyABP_k2_{k2}_ep_{epsilon}"
# 		circle_test(params,folder_name)