


def BFS(node_matrix, goal):

	current_node_index = 0
	path_taken = []
	next_possible_path = []

	while not current_node_index == goal:

		print('\n')
		queue = [node_matrix[current_node_index]]

		#searching for connectivity and adding to queue
		for index, connection in enumerate(queue[0]):
			if connection == 1:
				print("Index {} is connected with {}".format(current_node_index, index))
				if not( index in path_taken or index in next_possible_path):
					queue.append( node_matrix[index] )
					next_possible_path.append(index)

		path_taken.append(current_node_index)
		queue.pop(0)

		if not next_possible_path[0] == current_node_index:
			current_node_index = next_possible_path[0]
			next_possible_path.pop(0)

	print("Path taken: ", path_taken)



def main():
	'''
					#A B C D E F G H S       (goal = 7)
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
					#0 1 2 3 4 5 6 7 8 9 0 1 2       (goal = 4)
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

	BFS(node_matrix, goal=4)


if __name__ == '__main__':
	main()