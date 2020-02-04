# lab of metaheuristics course on Simulated Annealing
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

# Q1: define fitness function to optmize
def m(v):
	return 1+np.cos(0.04*v)**2
def n(v):
	return np.exp(-v**2/20000)
def fitness(v):
	return m(v)*n(v)
'''
 # Q2: plot fitness surface
npoints = 1000
x = np.linspace(-500,500,npoints)
y = fitness(x)
plt.ylabel('fitness')
plt.xlabel('x')
plt.plot(x,y,'r-')
plt.show()
'''

# Q3: apply SA algorithm for scipy to fitness function
class opt_sa:
	def __init__(self,func,x0,T0,maxiter,upper,lower):
		self.func = func
		self.x0 = x0
		self.maxiter = maxiter
		self.upper = upper
		self.lower = lower
		self.T = T0
		self.states = [self.x0]
		self.energies = []
		self.state_opt = x0
		self.energy_opt = self.func(self.x0)
	
	def energy_eval(self,y):
		return self.func(y)
	
	def transition_sampling(self,y):
		u = np.random.rand()
		delta = self.energy_eval(self.states[-1]) - self.energy_eval(y)
		p = np.exp(-delta/self.T)
		if u <= p:
			return True
		else:
			return False
	
	def temp_update(self,k):
		self.T = self.T/np.log(1+0.1*k)
		#if self.T < 0.5:
		#	self.T = 0.5
	
	def search(self):
		u=np.random.rand()
		sign = np.sign(u - 0.5)
		learn_rate = self.T * ((1 + 1/self.T)**np.abs(2*u - 1) - 1.0) # 0 if u~0.5; 1 if u~0 or u~1, 0.5 if |u|=0.75 
		y = sign * learn_rate
		step = y * 0.5*(self.upper-self.lower)
		state_new = self.states[-1] + step # sample a neighbour    
		return state_new
	
	def optimize(self,plot_bool):
		if plot_bool:
			npoints = 1000
			x = np.linspace(-500,500,npoints)
			y = self.func(x)
			plt.figure()
			plt.ylabel('fitness')
			plt.xlabel('x')
			ax=plt.gca()
			ax.set_xlim((-600, 600))
			xc = [self.states[-1]]
			yc = [0]
			cur_state = plt.scatter(xc, yc, marker = '*', c = 'green')
			plt.plot(x,y,'k-')

		k=1
		self.energies+=[self.func(self.x0)]
		while k<self.maxiter:
			print("temperature: ",self.T)

			neigh_state = self.search()
			self.temp_update(k) # update temperature
			#print("temp = ", self.T)
			neigh_energy = self.energy_eval(neigh_state)
			
			if neigh_energy > self.energies[-1]:
				self.states+=[neigh_state]
				self.energies+=[neigh_energy]
				if neigh_energy > self.energy_opt:
					self.state_opt = neigh_state
					self.energy_opt = neigh_energy

			if self.transition_sampling(neigh_state):
				self.states+=[neigh_state]
				self.energies+=[neigh_energy]
			
			k+=1

			if plot_bool and (k-1)%10==0:
				xs = [self.state_opt,self.state_opt]
				ys = [0, self.energy_opt]
				loc_opt = plt.plot(xs,ys,'ro-')

				xc = [self.states[-1]]
				yc = [0]
				cur_state = plt.scatter(xc, yc, marker = '*', c = 'green')
				plt.show(block=False)
				plt.pause(0.5)

		if plot_bool:
			plt.legend([mlines.Line2D([], [], color='red', marker='o',
                          markersize=6), cur_state], ['local optimum', 'visited state'])
			plt.savefig('lab1.png')
		return self.energy_opt, self.state_opt
	
x0 = -500+np.random.rand()*1000 
print("x0 = ",x0)
T0 = 1e9
n_iter = 100
my_sa = opt_sa(fitness,x0,T0,n_iter,500,-500)
print(my_sa.optimize(True))

plt.imread("lab1.png")
plt.show()