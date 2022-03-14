from circle_test import *
from params import *

def interaction_test(delta,epsilon,folder_name):
	params_inter = params.copy()
	params_inter["Nsteps"] = 500
	params_inter["freq"] = 10
	params_inter["N"] = 8
	params_inter["v0"] = 0
	params_inter["delta"],params_inter["epsilon"] =delta,epsilon
	thisSystem = pyABP.System(params_inter)
	nsave = int(params_inter["Nsteps"]/params_inter["freq"])

	for i in range(nsave):
			thisSystem.step(params_inter["freq"])
			filename1 = folder_name +'/data'+str(i)+'.dat'
			filename2 = folder_name +'/data'+str(i)+'.vtp'
			thisSystem.output(filename1,filename2,params_inter["saveText"],params_inter["saveVTK"])
			print("Ran and saved after " + str(params_inter["freq"]) + " steps, total at " + str((i+1)*params_inter["freq"]))