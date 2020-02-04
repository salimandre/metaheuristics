import numpy as np 
from random import random
from turtle import *

rosenbrock = lambda x: (1-x[0])**2 + 100*(x[1]-x[0]**2)**2
# min x = (1., 1.)
# optim = 0.

class PSO:
	def __init__(self,fitness_,dim_,pop_size,param_1=1., param_2=2., vmax_=0.5, plot_rosenbrock=False):
		self.fitness = fitness_

		self.particle_army = [Particle(0,np.zeros(dim_))]*pop_size
		for i in range(pop_size):
			rand_init_pos = 30*np.random.rand(dim_)-15
			self.particle_army[i] = Particle(i,rand_init_pos,param_1, param_2, vmax_)

		self.id_best_particle = None
		self.best_particle_eval = 1e6

	def evaluate(self):
		for i, p in enumerate(self.particle_army):
			p.evaluate(self.fitness)
			if plot_rosenbrock:
				goto(p.cur_pos*20)
				dot(8,"green")
			if p.best_eval < self.best_particle_eval:
				self.id_best_particle = i
				self.best_particle_eval = p.best_eval
		if plot_rosenbrock:
			goto(self.particle_army[self.id_best_particle].cur_pos*20)
			dot(8,"purple")

	def update(self):
		captain_pos = self.particle_army[self.id_best_particle].cur_pos
		for i, p in enumerate(self.particle_army):
			if plot_rosenbrock:
				goto(p.cur_pos*20)
				dot(8,"white")

			p.update(captain_pos)
			if plot_rosenbrock:
				pendown()
				goto(p.cur_pos*20)
				if i == self.id_best_particle :
					dot(8,"purple")
				else:
					dot(8,"green")
				penup()


class Particle:
	def __init__(self, id_, init_pos, param_1=1., param_2=2., vmax_=0.5):
		self.id = id_

		self.cur_pos = init_pos
		self.cur_eval = 0
		self.velocity = 0

		self.best_pos = 0
		self.best_eval = 1e6

		self.c_1 = param_1
		self.c_2 = param_2
		self.vmax = vmax_

	def evaluate(self,fitness_):
		self.cur_eval  = fitness_(self.cur_pos)
		if self.cur_eval<self.best_eval:
			self.best_eval = self.cur_eval
			self.best_pos = self.cur_pos

	def update(self,captain_pos):
		self.velocity = self.c_1 * random() * (self.best_pos - self.cur_pos) + self.c_2 * random() * (captain_pos - self.cur_pos)
		if np.linalg.norm(self.velocity)>self.vmax:
			self.velocity = np.sign(self.velocity) * self.vmax
		self.cur_pos += self.velocity


if __name__ == '__main__':

	c_1 = 1.
	c_2 = 1.
	vmax = 3.
	plot_rosenbrock = True

	pso_model = PSO(fitness_ = rosenbrock, dim_ = 2, pop_size = 10, vmax_=vmax, plot_rosenbrock=True)

	if plot_rosenbrock:
		penup()
		shape(None)
		shapesize(0.01, 0.01, 0.01)
		goto(np.array([-100,200]))
		write("Rosenbrock minimization by PSO algorithm",align='left',font=("Arial", 15, "bold"))
		goto(np.array([-250,-200]))
		write("Legend",align='left',font=("Arial", 15, "bold"))
		goto(np.array([-250,-220]))
		dot(8,"red")
		goto(np.array([-250,-225]))
		write("   Rosenbrock optimum",align='left',font=("Arial", 15, "normal"))
		goto(np.array([-250,-240]))
		dot(8,"green")
		goto(np.array([-250,-245]))
		write("   Particle",align='left',font=("Arial", 15, "normal"))
		goto(np.array([-250,-260]))
		dot(8,"purple")
		goto(np.array([-250,-265]))
		write("   Best Particle",align='left',font=("Arial", 15, "normal"))
		goto(np.array([20,20]))
		dot(8,"red")
		write("      (1,1)",align='left')

	print("-------- initial state --------\n")
	for p in pso_model.particle_army:
		print(p.cur_pos)
	pso_model.evaluate()
	for p in pso_model.particle_army:
		print(p.cur_eval)

	print("\n")
	for k in range(3):
		print("-------- iteration {} --------\n".format(k+1))
		pso_model.update()
		pso_model.evaluate()
		print("best particle id: ", pso_model.id_best_particle)

	print("-------- final state --------\n")
	for p in pso_model.particle_army:
		print(p.cur_pos)
	for p in pso_model.particle_army:
		print(p.cur_eval)

	if plot_rosenbrock:
		done()
