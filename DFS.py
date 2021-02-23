def DFS(node_matrix, goal):
	
	stack = [node_matrix[0]]
	path_taken = [node_matrix[0]]
	path_taken_index = [0]
	flag = False # to check if a new path was found

	while not node_matrix[goal] in path_taken:

		for index, connection in enumerate(stack[-1]):
			if connection == 1:
				if not node_matrix[index] in path_taken:
					stack.append(node_matrix[index])
					path_taken.append(node_matrix[index])
					path_taken_index.append(index)
					flag = True
					break

		if flag == False:
			stack.pop(-1)

		flag = False

	print(path_taken_index)


def main():
	'''
					 #A B C D E F G H S       (goal = 7) (see pic 1 in this folder)
	node_matrix = [ [0,1,0,0,0,0,0,0,1],        #a 0
					[1,0,0,0,0,0,0,0,0],		#b 1
					[0,0,0,1,1,1,0,0,1],		#c 2
					[0,0,1,0,0,0,0,0,0],		#d 3
					[0,0,1,0,0,0,0,1,0],		#e 4
					[0,0,1,0,0,0,1,0,0],		#f 5
					[0,0,0,0,0,1,0,1,1],		#g 6
					[0,0,0,0,0,0,1,0,0],		#h 7
					[1,0,1,0,0,0,1,0,0] ]       #s 8
	'''
					#0 1 2 3 4 5 6 7 8 9 0 1 2       (goal = 4) (see pic 2 in this folder)
	node_matrix = [ [0,0,0,0,0,0,0,1,0,1,0,1,0],        # 0
					[0,0,0,0,0,0,0,0,1,0,1,0,0],		# 1
					[0,0,0,1,0,0,0,0,0,0,0,0,1],		# 2
					[0,0,1,0,1,0,0,1,0,0,0,0,0],		# 3
					[0,0,0,1,0,0,0,0,0,0,0,0,0],		# 4
					[0,0,0,0,0,0,1,0,0,0,0,0,0],		# 5
					[0,0,0,0,0,1,0,1,0,0,0,0,0],		# 6
					[1,0,0,1,0,0,1,0,0,0,0,1,0],		# 7
					[0,1,0,0,0,0,0,0,0,1,0,0,1],		# 8
					[1,0,0,0,0,0,0,0,1,0,1,0,0],		# 9
					[0,1,0,0,0,0,0,0,0,1,0,0,0],		# 10
					[1,0,0,0,0,0,0,1,0,0,0,0,0],		# 11
					[0,0,1,0,0,0,0,0,1,0,0,0,0] ]       # 12

	DFS(node_matrix, goal=4)


if __name__ == '__main__':
	main()