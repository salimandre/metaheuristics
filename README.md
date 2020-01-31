# metaheuristics

My own work for the Metaheuristics course consisted on implementing the following algorithms:
* Brute Force Algorithm
* Simulated Annealing (SA)
* Simplex method
* Genetic Annealing (GA)
* Particle swarm optimization (PSO)

These algorithms have been tested on toy examples. 

Although some have been tried in the context of <strong>Google Challenge</strong>. More details on this competition below.

## Brute Force Algorithm on LP with hypercube constraint

## Simulated Annealing applied to non-convex optimization problem

We used SA to maximize the following fitness function:

<img src="sa_fitness.png" width="45%">
with a fast update using uniform sampling and the following cooling schedule:
<img src="sa_cooling.png" width="15%">

<img src="sa.png" width="45%">

## Simplex Method applied to linear programming

## Genetic Algorithm applied to Traveling Salesman Problem

![0.3](ga_tsp.gif)

## Particle Swarm Optimization algorithm applied to Rosenbrock minimization

We used PSO in order to solve the following optimization problem:

<img src="pso_eq.png" width="30%">

![0.3](pso_rosen.gif)

## Google Challenge

Original optimization problem:

![0.3](google_challenge_eq.jpg)

Relaxed optimization problem: 

![0.3](google_challenge_relax_eq.jpg)

We get a LP optimization problem: 

![0.3](google_challenge_can_eq.jpeg)
