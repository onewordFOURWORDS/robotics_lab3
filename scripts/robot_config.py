# import required modules
import robot_model as rm
import math

def main():
	### problem 2 part a ###
	# defining 2 link planar manipulator array
	two_link = [[1, 0, 0, math.pi/2], 
				[1, 0, 0, math.pi/2]]
					
	print("\n*** Problem 2 Part A ***")
	
	# calculate total homogenous transformation
	a = rm.kinematic_chain(two_link)
	
	# take the returned transformation and use get_pos get_rot to access those values
	print("x = %.2f meters \ny = %.2f meters \nz = %.2f meters" % (rm.get_pos(a)))
	# this doesnt display pi radians because pi radians is just a complete circle and at that point your just back at 0
	print("roll = %.2f radians \npitch = %.2f radians \nyaw = %.2f radians" % (rm.get_rot(a))) 
	



	### problem 2 part b ###
	# define 6 dof array cases provided by lecture slides and assignment
	
	# case 1
	six_dof_case_1 = [
#   |    a   |    alpha   |    d   |   theta   |
	[0       , math.pi/2  , 0.1625 , 0         ],
	[-0.425  , 0          , 0      , 0         ],
	[-0.3922 , 0          , 0      , 0         ],
	[0       , math.pi/2  , 0.1333 , 0         ],
	[0       , -math.pi/2 , 0.0997 , 0         ],
	[0       , 0          , 0.0996 , 0         ]]
	
	# case 2
	six_dof_case_2 = [
#   |    a   |    alpha   |    d   |   theta   |
	[0       , math.pi/2  , 0.1625 , 0         ],
	[-0.425  , 0          , 0      , -math.pi/2],
	[-0.3922 , 0          , 0      , 0         ],
	[0       , math.pi/2  , 0.1333 , 0         ],
	[0       , -math.pi/2 , 0.0997 , 0         ],
	[0       , 0          , 0.0996 , 0         ]]
	
	
	# 
	print("\n\n*** Problem 2 Part B Case 1 ***")
	# calculate total homogenous transformation for case 1
	b_case_1 = rm.kinematic_chain(six_dof_case_1)
	
	# take the returned transformation and use get_pos get_rot to access those values
	print("x = %.2f meters \ny = %.2f meters \nz = %.2f meters" % (rm.get_pos(b_case_1)))
	print("roll = %.2f radians \npitch = %.2f radians \nyaw = %.2f radians" % (rm.get_rot(b_case_1))) 

	
	print("\n\n*** Problem 2 Part B Case 2 ***")
	# calculate total homogenous transformation for case 2
	b_case_2 = rm.kinematic_chain(six_dof_case_2)
	
	# take the returned transformation and use get_pos get_rot to access those values
	print("x = %.2f meters \ny = %.2f meters \nz = %.2f meters" % (rm.get_pos(b_case_2)))
	print("roll = %.2f radians \npitch = %.2f radians \nyaw = %.2f radians" % (rm.get_rot(b_case_2))) 
	
	print()

if __name__ == '__main__':
	main()
