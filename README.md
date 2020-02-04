# metaheuristics

My own work for the Metaheuristics course consisted on implementing the following algorithms:
* Brute Force Algorithm
* Simulated Annealing (SA)
* Simplex method
* Genetic Annealing (GA)
* Particle swarm optimization (PSO)

These algorithms have been tested on toy examples. 

Although some have been tried in the context of <strong>Google Challenge</strong>. More details on this competition below.

## Brute Force Algorithm on Integer Linear Programming (ILP) problem

We solved the following ILP problem using a very naive method since we did an exhaustive search over basic feasible solutions of this ILP. Basic feasible solutions are a subset of vertices of constraint polytope, here an hypercube of dimension d with 2^d vertices. we generate vertices on the fly as binary arrays and evaluate them.

<img src="img/naive_lp_eq2.png" width="25%">

<img src="img/naive_lp.gif" width="45%">

## Simulated Annealing applied to non-convex optimization problem

We used SA to maximize the following fitness function:

<img src="img/sa_fitness.png" width="35%">
with a fast update using uniform sampling and the following cooling schedule:
<img src="img/sa_cooling.png" width="15%">

<img src="img/sa.png" width="45%">

## Simplex Method applied to Linear Programming (LP)

We applied Revisited Simplex Method to the following LP problem in dimension 50.

<img src="img/simplex_eq.png" width="25%">

<img src="img/simplex_method.gif" width="45%">

## Genetic Algorithm applied to Traveling Salesman Problem

We applied GA to solve TSP on a sample of 9 random points. We computed euclidian distances between them as cost for edges. We used a population of 8 individuals, a proba of mutation of 0.15. We show the loop corresponding to the worst solution at each generation and added the associated cost in terms of distance. The number of mutations at each generation is also indicated.

![0.3](img/ga_tsp2.gif)

## Particle Swarm Optimization algorithm applied to Rosenbrock minimization

We used PSO in order to solve the following optimization problem:

<img src="img/pso_eq.png" width="30%">

![0.3](img/pso_rosen.gif)

## Google Challenge

Original optimization problem:

![0.3](img/google_challenge_eq.jpg)

Relaxed optimization problem: 

![0.3](img/google_challenge_relax_eq.jpg)

We get a LP optimization problem: 

![0.3](img/google_challenge_can_eq.jpeg)
