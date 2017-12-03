from logic import *
import numpy as np 

def reward(current_state,action):
	next_state_tmp = current_state
	reward = 1

	prob = 1.0#/np.count_nonzero(np.array(next_state_tmp)==0)
	next_state = add_two(next_state_tmp)
	
	done = 1
	return prob,next_state,reward,done

current_state = np.ones((4,4))
action = 1
prob,next_state,reward,done = reward(current_state,action)
print prob,next_state,reward,done