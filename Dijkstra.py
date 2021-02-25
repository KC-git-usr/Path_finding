import numpy as np 


def Dijstra(node_matrix):

	max_cost = np.amax(node_matrix)+1 #my substitute for infinity

	path_data = [['a',0,[],[]], 
				 ['b',max_cost,[],[]], 
				 ['c',max_cost,[],[]], 
				 ['d',max_cost,[],[]], 
				 ['e',max_cost,[],[]], 
				 ['f',max_cost,[],[]], 
				 ['g',max_cost,[],[]]]

	for from_node, costs in enumerate(node_matrix): #extracting from node data
		u = path_data[from_node][1] #storing the cost taken to reach from node
		for to_node, to_cost in enumerate(costs): #exctracting cost values between from and to node
			if not to_cost == 0: #checking if connection exists
				v = to_cost #storing cost taken to reach to_node from from_node
				if (u+v)<path_data[to_node][1]: #checking if new cost is lesser than previous known cost value
					path_data[to_node][1] = u + v #updating cost
					path_data[to_node][2] = path_data[from_node][0] #storing prev_node data to post-process min cost path

	#reconstructing min cost path
	for node in path_data:
		current_node = node
		while True: 
			prev_node = current_node[2] #current node's from node
			if current_node[0] == 'a':
				break
			node[3].append(prev_node)
			for search_node in path_data: #search for from node, make it current node
				if search_node[0]==prev_node:
					current_node = search_node
					break

	for node in path_data:
		if node[1] == max_cost:
			node[1] = -1 
	
	return path_data		


def main():

					        #a b c d e f g   (see pic 3)
	node_matrix = np.array([[0,2,0,1,0,0,0],   #a 0
							[0,0,0,3,10,0,0],  #b 1
							[4,0,0,0,0,5,0],   #c 2
							[0,0,2,0,2,8,4],   #d 3
							[0,0,0,0,0,0,6],   #e 4
							[0,0,0,0,0,0,0],   #f 5
							[0,0,0,0,0,1,0]], np.float)  #g 6

	path_data = Dijstra(node_matrix)

	print(path_data)
	print("NOTE : -1 implies node is unreachable")

if __name__ == '__main__':
	main()