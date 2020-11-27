from numpy import matrix

class Matrix(object):
	"""docstring for Matrix"""
	def __init__(self, arg):
		super(Matrix, self).__init__()
		self.arg = arg

	def mul(self,matrix):
		matrix = matrix.arg
		to_return = []
		for i in range(len(self.arg)):
			to_return.append([0]*len(matrix[0]))

		for i in range(len(self.arg)):
			for j in range(len(matrix[0])):
				for k in range(len(self.arg[0])):
					to_return[i][k] += self.arg[i][j] * matrix[j][k]
		return Matrix(to_return)

def myMatrix(arg):
	return matrix(arg)