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

We solved the following LP problem using a very naive method since we did an exhaustive search over basic feasible solutions of this LP. Basic feasible solutions are vertices of constraint polytope.

<img src="naive_lp_eq.png" width="25%">

<img src="naive_lp.gif" width="45%">

## Simulated Annealing applied to non-convex optimization problem

We used SA to maximize the following fitness function:

<img src="sa_fitness.png" width="35%">
with a fast update using uniform sampling and the following cooling schedule:
<img src="sa_cooling.png" width="15%">

<img src="sa.png" width="45%">

## Simplex Method applied to linear programming

## Genetic Algorithm applied to Traveling Salesman Problem

We applied GA to solve TSP on a sample of 9 random points. We computed euclidian distances between them as cost for edges. We used a population of 8 individuals, a proba of mutation of 0.15. We show the loop corresponding to the worst solution at each generation and added the associated cost in terms of distance. The number of mutations at each generation is also indicated.

![0.3](ga_tsp2.gif)

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
