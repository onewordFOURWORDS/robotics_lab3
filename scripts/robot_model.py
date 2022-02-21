# import required modules
import math
import numpy as np


# Accept Denavit-Hertenberg parameters
def dh_transformation(a, alpha, d, theta):
	# The following matrix implements the DH parameters in a combined homogenous transformation
	dh = np.array([
	[math.cos(theta) , -math.sin(theta)*math.cos(alpha) , math.sin(theta)*math.sin(alpha)  , a*math.cos(theta)],
	[math.sin(theta) , math.cos(theta)*math.cos(alpha)  , -math.cos(theta)*math.sin(alpha) , a*math.sin(theta)],
	[0               , math.sin(alpha)                  , math.cos(alpha)                  , d                ],
	[0               , 0                                , 0                                , 1                ]
	])
	# return the combined transformation array
	return dh


# accept 2d array of DH parameters
def kinematic_chain(dh_params):
	# initilize total transformation array with identity matrix
	tot_tran = np.identity(4)
	
	# loop through each set of DH parameters
	for i in range(len(dh_params)):	
		# matrix multiplcation between tot_tran and the result of the DH parameters in dh_transformation
		tot_tran = np.matmul(tot_tran, dh_transformation(dh_params[i][0],dh_params[i][1],dh_params[i][2],dh_params[i][3]))
		
	# return the result of all DH parameters multiplied together
	return tot_tran
	
	
# accept homogenous transformation as input
def get_pos(trans):
	# pull x y z out of the transformation
	x = trans[0][3]
	y = trans[1][3]
	z = trans[2][3]
	
	return x, y, z
	

# accept homogenous transformation as input
def get_rot(trans):
	
	roll = math.atan(trans[2][1] / trans[2][2])
	pitch = math.atan(-trans[2][0] / (math.sqrt( trans[2][1]**2 + trans[2][2]**2 )))
	yaw = math.atan(trans[1][0] / trans[0][0])
		
	return roll, pitch, yaw
