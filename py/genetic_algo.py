import numpy as np
from turtle import *
from scipy.spatial.distance import cdist 

def travel(path,points_):
	loop = list(path)+[path[0]]
	loop_points = [points_[i,:] for i in loop]
	penup()
	goto(loop_points[0])
	for p in loop_points[1:]:
		pendown()
		goto(p)

class Genetic_Problem:
	def __init__(self):
		pass

	def evaluate(self):
		pass

	def encode(self):
		pass

	def decode(self):
		pass


class TSP_Problem(Genetic_Problem):
	def __init__(self,map_,init_state):
		Genetic_Problem.__init__(self)
		self.n_cities=len(map_)
		self.map=map_
		self.state = init_state #np.array([[1,2,0],[0,1,2],[1,0,2],[1,2,0]])#np.zeros((self.popsize, self.n_cities))
		self.evals=np.zeros(self.n_cities)

	def evaluate(self):
		pop_evaluate=[]
		for individual in self.state:
			pop_evaluate += [[sum([self.map[tup[0],tup[1]] for tup in zip(individual, list(individual)[1:]+[list(individual)[0]])])]]
		self.evals = np.array(pop_evaluate)
		return self.evals

	def encode(self):
		pop_encode=[]
		for individual in self.state:
			basis_pos = list(range(self.n_cities))
			i = 0
			bin_str=''
			while basis_pos!=[]:
				ord_i = basis_pos.index(individual[i])
				basis_pos.pop(ord_i)
				bin_str+="{0:08b}".format(ord_i)
				i+=1
			pop_encode+=[[int(b) for b in list(bin_str)]]
		return np.array(pop_encode)

	def decode(self,encoded_state):
		pop_state=[]
		for individual in encoded_state:
			# read 8 bits bytes
			ord_pos = [int("".join([str(b) for b in byte]), 2) for byte in np.split(individual,self.n_cities)]
			# 
			basis_pos = list(range(self.n_cities))
			state = []
			i = 0
			while basis_pos!=[]:
				state_i = basis_pos[ord_pos[i]]
				state += [state_i]
				basis_pos.pop(ord_pos[i])
				i+=1
			pop_state += [state]
		return np.array(pop_state)

	def cross_over(self,eval):
		ind_split = np.split(np.argsort(eval.flatten()),2)[0]
		self.state = self.state[ind_split,:]
		encoded_parents = list(self.encode())
		encoded_couples = [tup for tup in zip(encoded_parents,encoded_parents[1:]+[encoded_parents[0]])]
		offsprings = []
		for couple in encoded_couples:
			if self.n_cities%2==0:
				split_parent1 = np.split(couple[0],2)
				split_parent2 = np.split(couple[1],2)
			else:
				q=int(self.n_cities/2)
				split_parent1 = [couple[0][:8*q],couple[0][8*q:]]
				split_parent2 = [couple[1][:8*q],couple[1][8*q:]]
			children1 = np.hstack((split_parent1[0], split_parent2[1])) 
			children2 = np.hstack((split_parent2[0], split_parent1[1])) 
			offsprings += [children1] + [children2]
		return np.vstack(offsprings)

	def mutate(self,proba_):
		count_mutations=0
		for i in range(len(self.state)):
			if np.random.rand()<proba_:
				perm = np.random.permutation(range(self.state.shape[1]))
				temp = self.state[i,perm[0]]
				self.state[i,perm[0]] = self.state[i,perm[1]]
				self.state[i,perm[1]] = temp
				count_mutations+=1
		return count_mutations

	def training(self,n_iter,points_to_draw=None):

		self.evaluate()
		print("--------- initial state ----------\ninitial state: ", my_tsp.state,"\n")
		print("initial eval: \n",self.evals,"\n")

		if points_to_draw is not None:
			penup()
			goto((-275,-220))
			color("black")
			write("worst case cost:",True,align='right',font=("Arial", 10, "italic"))
			penup()
			goto((-215,-220))
			write("mutations:",True,align='right',font=("Arial", 10, "italic"))

			color(color_iter[0])
			i_worst_case = np.argsort([a[0] for a in self.evals])[-1]
			shape("turtle")
			pendown()
			travel(self.state[i_worst_case,:],rand_city_pos)
			penup()
			goto((-275,-230))
			write(str(int(self.evals[i_worst_case][0])),True,align='right',font=("Arial", 10, "bold"))

		for iter in range(n_iter):
			print("--------- iteration {} ----------\n".format(iter+1))
			new_evals = self.evaluate()
			offsprings_iter = self.cross_over(new_evals)#self.evals)
			self.state = self.decode(offsprings_iter)
			count_mut = self.mutate(0.15)
			print("number of mutations: ",count_mut,"\n")
			print("current state: \n",self.state,"\n")
			print("current eval: \n",self.evals,"\n")

			if points_to_draw is not None:
				i_worst_case = np.argsort([a[0] for a in self.evals])[-1]
				shape("turtle")
				color(color_iter[iter+1])
				pendown()
				travel(self.state[i_worst_case,:],rand_city_pos)
				penup()
				goto((-215,-230-(iter+1)*12))
				write(str(count_mut),True,align='right',font=("Arial", 10, "bold"))
				goto((-275,-230-(iter+1)*12))
				write(str(int(self.evals[i_worst_case][0])),True,align='right',font=("Arial", 10, "bold"))

		goto((0,0))
		my_tsp.evaluate()
		print("----------------------\nnumber of iterations: ",iter+1,"\nfinal evaluation:\n", my_tsp.evals,"\n")
		print("final state: \n",self.state,"\n")


if __name__ == '__main__':

	#map_3_cities = np.array([[0,1,5],[1,0,2],[5,2,0]])
	#map_4_cities = np.array([[0,5,3,7],[5,0,1,4],[3,1,0,6],[7,4,6,0]])
	#init_state_3_cities = np.array([[1,2,0],[0,1,2],[1,0,2],[1,2,0]])
	#init_state_4_cities = np.array([[0,1,2,3],[1,0,3,2],[0,1,3,2],[3,1,2,0]])

	color_iter = ['pink','violet','blue', 'orange', 'green', 'brown', 'purple', 'black', 'grey']
	city_names = ['AMSTERDAM','BERLIN','COTONOU','DEAUVILLE','EMPOLI','FRANCFORT','GRENOBLE','HANOI','IBIZA','JOINVILLE']
	rand_city_pos = 700*np.random.rand(len(city_names),2)-350
	city_map = cdist(rand_city_pos,rand_city_pos)
	population_size = 8

	rand_init_state = []
	for i in range(population_size):
		rand_init_state += [np.random.permutation(len(city_names))]
	rand_init_state = np.vstack(rand_init_state)
	#print("init state = ",rand_init_state)
	#print("map of tsp: \n",city_map,"\n")

	my_tsp = TSP_Problem(map_ = city_map, init_state = rand_init_state)

	drawing_option = True
	if drawing_option:
		for i, point in enumerate(rand_city_pos):
		  penup()
		  goto(point)
		  dot(6,"red")
		  write(city_names[i])

	my_tsp.training(8, rand_city_pos)

	ts = getscreen()
	ts.getcanvas().postscript(file="tsp.eps")

	done()
