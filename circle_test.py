# Debugging ABP script
# Where to look for the module:
import sys
sys.path.append("./build") 
import os
import shutil
import pyABP
##FILLING PARAMETER DICTIONARY
params={}
# system
params["N"]=2000
params["L"]= 100.0

# dynamics
params["dt"]=0.01
params["seed"]=1

# ABPs
params["mu"]=1.0
params["Dr"]=0.001
params["v0"]=0.1
# Interaction
params["type"] = 1
params["k"]= 1.0
params["k2"] = 1.0
params["delta"] = 1.0
params["epsilon"] = 0.15
params["poly"]=0.2

# C++ internal: debugging output?
params["verbose"]=False

# Python script options only
params["Nsteps"]=100000
params["freq"]=1000
params["saveText"]=True
params["saveVTK"]=False

def circle_test(params,folder_name):
	"""Creates a system of ABPs configured randomly in a circle with given parameters 
	and runs for time steps, saving to folder_name."""
	thisSystem = pyABP.System(params)
	nsave = int(params["Nsteps"]/params["freq"])
	try:
		os.mkdir(folder_name)
	except FileExistsError:
		shutil.rmtree(folder_name)
		os.mkdir(folder_name)

	for i in range(nsave):
		thisSystem.step(params["freq"])
		filename1 = folder_name +'/data'+str(i)+'.dat'
		filename2 = folder_name +'/data'+str(i)+'.vtp'
		thisSystem.output(filename1,filename2,params["saveText"],params["saveVTK"])
		print("Ran and saved after " + str(params["freq"]) + " steps, total at " + str((i+1)*params["freq"]))

k2s = [0.4]
epsilons = [0.05] 
params["inter_type"] = 1
# k2s = [0.4,0.8,1.2,1.6,2]
# epsilons = [0.05,0.1,0.15,0.2,0.25,0.3] 
for k2 in k2s:
	for epsilon in epsilons:
		params["k2"] = k2
		params["epsilon"] = epsilon
		folder_name = f"./data/pyABP_k2_{k2}_ep_{epsilon}"
		circle_test(params,folder_name)