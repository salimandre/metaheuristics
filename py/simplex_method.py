import numpy as np
import matplotlib.pyplot as plt

def revised_simplex_method(A, b, c, indB, indN, dim_ = None, plot_choice=False):
	m,n = A.shape

	print("indB: ", indB)
	print("indN:", indN)

	"""
	if plot_choice and dim_ is not None:
		plt.figure()
		plt.suptitle("Simplex Method in dimension {}".format(dim_))
		ax1 = plt.subplot(3,1,1)
		ax1.imshow(np.zeros((hypercube_.dim,1)),cmap='gray')
		plt.show(block=False)
	"""
	iter=0
	list_eval=[]
	opt_vertex = np.empty(dim_)
	best_eval=-1e6
	if plot_choice:
		plt.figure()
		plt.suptitle("Revised Simplex Method in dimension {}".format(dim_))
	while True:

		print("--------- iter {} ------------".format(iter))

		#STEP 0
		# compute initial basis inverse
		#print("B = ", A[:,indB])
		invB = np.linalg.inv(A[:,indB])
		#print("invB = ", invB)
		b_s = invB @ b
		#print("check >0: ", invB @ b)

		#compute x_B and evaluate <c, x>
		x = np.hstack((b_s, np.zeros(n-m)))
		x = [a[0] for a in sorted(zip(x,indB+indN), key = lambda x: x[1])]
		print("x = ", x)
		lp_eval = np.dot(x,c)
		list_eval+=[lp_eval]
		if list_eval[-1]>=best_eval:
			best_eval=list_eval[-1]
			opt_vertex = x[:dim_] 
		print("LP eval = ", lp_eval)

		if plot_choice and dim_ is not None:
			ax1 = plt.subplot(3,1,1)
			plt.title("current vertex")
			ax1.imshow(np.reshape(x[:dim_],(dim_,1)),cmap='gray') #OrRd
			plt.xticks([])
			plt.yticks([])
			plt.subplot(3,1,2)
			plt.title("objective evaluation")
			print("list_eval: ", list_eval)
			plt.plot(np.arange(len(list_eval)),list_eval,'mo-')
			plt.subplot(3,1,3)
			plt.subplots_adjust(hspace=0.6)
			plt.xticks([])
			plt.yticks([])
			plt.title("optimal vertex")
			print("opt_vertex: ", opt_vertex)
			plt.imshow(np.reshape(opt_vertex,(len(opt_vertex),1)),cmap='gray') #OrRd
			plt.show(block=False)
			plt.pause(1./(dim_**2))

		# compute vector of simplex multipliers
		y = c[indB] @ invB

		#STEP 1
		# compute gradient of cost over x_N
		delta_c = c[indN] - y @ A[:,indN]

		#print("delta_c: ", delta_c)
		if (delta_c<=0).all():
			print("optimal found")
			break

		#STEP 2
		j_in = indN[np.argmax(delta_c)]
		print("in: ", j_in)
		# check if unbounded
		A_s = invB @ A[:,j_in]
		#print("check unbounded: ", A_s)
		if (A_s <= 0).all():
			print("unbounded situation")
			break

		#STEP 3
		j_out = indB[np.argmin(np.divide(b_s,[np.maximum(a,1e-3) for a in A_s]))]
		print("j_out: ", j_out)
		indB = [i if i!=j_out else j_in for i in indB]
		indN = [i if i!=j_in else j_out for i in indN]

		iter+=1

	print("--------- iter {} ------------".format(iter))

	#compute x_B and evaluate <c, x>
	x = np.hstack((b_s, np.zeros(n-m)))
	x = [a[0] for a in sorted(zip(x,indB+indN), key = lambda x: x[1])]
	print("x = ", x)
	lp_eval = np.dot(x,c)
	list_eval+=[lp_eval]
	if list_eval[-1]>=best_eval:
		best_eval=list_eval[-1]
		opt_vertex = x[:dim_]#*255
		print("opt_vertex: ",opt_vertex)
	print("LP eval = ", lp_eval)

	if plot_choice and dim_ is not None:
		ax1 = plt.subplot(3,1,1)
		plt.title("current vertex")
		ax1.imshow(np.reshape(x[:dim_],(dim_,1)),cmap='gray') #OrRd
		plt.xticks([])
		plt.yticks([])
		plt.subplot(3,1,2)
		plt.title("objective evaluation")
		plt.plot(np.arange(len(list_eval)),list_eval,'mo-')
		plt.subplot(3,1,3)
		plt.subplots_adjust(hspace=0.6)
		plt.xticks([])
		plt.yticks([])
		plt.title("optimal vertex")
		plt.imshow(np.reshape(opt_vertex,(len(opt_vertex),1)),cmap='gray') #OrRd
		plt.show(block=False)
		plt.pause(1./(dim_**2))
		plt.savefig('simplex_method.png')


def pl_cube(c):
    n=len(c)
    b = np.ones(n)
    A_eq = np.hstack((np.eye(n),np.eye(n)))
    c = np.hstack((c,np.zeros(n)))
    return A_eq, b, c

def pl_pizza(c,M):
    n=len(c)
    A_eq = np.hstack((np.eye(n),np.eye(n),np.zeros((n,1))))
    A_eq = np.vstack((A_eq,np.hstack((c,np.eye(n+1)[-1,:]))))
    b = n*[1]+[M]
    c = np.hstack((c,np.zeros(n+1)))
    return A_eq, b, c

if __name__ == '__main__':

	""" toy poblem 1
	A=np.array([[1,0,0,1,0,0,0],[0,1,0,0,1,0,0],[0,0,1,0,0,1,0],[3,6,2,0,0,0,1]])
	b=np.array([1000,500,1500,6750])
	c= np.array([4,12,3,0,0,0,0])

	permut=[6,5,4,3,2,1,0]
	"""

	""" toy poblem 2
	A = np.array([[1, 0, -1, 0],[0, 1, 0, -1]])
	c = np.array([1, 1, 0,0 ])
	b = np.array([1,1])

	AA = np.array([[1, 0, 1, 0],[0, 1, 0, 1]])
	cc = np.array([1, 1, 0, 0])
	bb = np.array([1, 1])
	"""

	""" small pizza problem
	c = np.array([4,14,15,18,29,32,36,82,95,95])
	dim = len(c)
	A,b,c = pl_pizza(c,100)
	"""

	"""medium pizza problem"""
	c = np.array([7,12,12,13,14,28,29,29,30,32,32,34,41,45,46,56,61,61,62,63,65,68,76,77,77,92,93,94,97,103,113,114,114,120,135,145,145,149,156,157,160,169,172,179,184,185,189,194,195,195])
	dim = len(c)
	A,b,c = pl_pizza(c,4500)

	print("A: \n", A)
	print("b: ", b)
	print("c: ", c)
	print("shape of A: ", A.shape)
	print("rank of A: ", np.linalg.matrix_rank(A))
	permut=list(range(A.shape[1]))[::-1]
	revised_simplex_method(A, b, c, permut[:A.shape[0]], permut[A.shape[0]:], dim, True)

	plt.imread("naive_linear_prog.png")
	plt.show()

