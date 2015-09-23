#### import data

import mols10 # contains all details of frequency distributions and assignments
import operator # for dictionary sorting

nodes = mols10.nodes 
comp = mols10.comp
fullhouse = mols10.fullhouse

#### 1. FUNCTIONS FOR PAIRS ####

#### 1.1. function for counting pairs

def generate_pairs(nodes):
	visited_nodes = set() # to prevent double count
	for node_i in nodes:  # look inside the dictionary of nodesw
		for node_j in nodes[node_i]: # look inside node i
			if node_j in visited_nodes:	# if node j is visited
				continue				# pass to the next nodes
			else:						# otherwise, the connection between i and j indicate a pair
				yield tuple(sorted((node_i, node_j)))		   
				continue				# move to the next nodes
		visited_nodes.add(node_i)       # add node i to the set of visited node

#### 1.2. function for eliminating complements pairs

def remove_comp_pairs(pairs):
	for pair in pairs:
		(p1, p2) = pair
		for c1 in comp[p1]: # find the complements of distribution p1
			for c2 in comp[p2]: # find the complements of distribution p2
				temp_pair = tuple(sorted((c1, c2)))
				if temp_pair in pairs and temp_pair <> pair:
					pairs.remove(temp_pair) # delete if the complement pair is already in the set
	return pairs

#### 2. FUNCTIONS FOR TRIPLES ####

#### 2.1. function for counting undirected cycles

def generate_triples(nodes):
	visited_ids = set() # mark visited node
	for node_a_id in nodes: # starting with distribution A
		temp_visited = set() # to get undirected triangles
		for node_b_id in nodes[node_a_id]: # see what distribution can be assigned to A
			if node_b_id in visited_ids:
				continue # if B is already visited, pass
			for node_c_id in nodes[node_b_id]:
				if node_c_id in visited_ids:
					continue # if C is already visited, pass
				elif node_c_id in temp_visited:
					continue # if C is temporary visited, pass
				elif node_a_id in nodes[node_c_id]:
					yield tuple(sorted((node_a_id, node_b_id, node_c_id))) # produce a 3-tuple, sorted in ascending order
				else:
					continue
			temp_visited.add(node_b_id) # add B to temporary visited nodes
		visited_ids.add(node_a_id) # add A to visited nodes

#### 2.2. function for eliminating the complement triples

def remove_comp_triples(triples):
	for cycle in triples:
		(p1, p2, p3) = cycle
		for c1 in comp[p1]: # find the complement of distribution p1
			for c2 in comp[p2]:	# find the complement of distribution p2
				for c3 in comp[p3]: # find the complement of distribution p3
					temp_cycle = tuple(sorted((c1, c2, c3)))
					if temp_cycle in triples and temp_cycle <> cycle:
						triples.remove(temp_cycle) # delete if the cycle is already in the set
	return triples

#### 2.3. function for counting the frequency of recurrence of pairs in triples

def count_fh_freq(fh_grow, fh_pairs): # fh_grow is the triples growing from 2 full house pairs, fh_pairs is the set of 2 full house pairs
	fh_freq = {} # to store the pairs and their frequencies
	for pair in fh_pairs: # start from a pair of 2 full house distributions
		fh_freq[pair] = []	# empty to store the pair frequency
		count_freq = 0
		for triple in fh_grow: # compare to the triples in fh_grow
			(p1, p2, p3) = triple
			if (p1, p2) == pair or (p1, p3) == pair or (p2, p3) == pair: # if any 2 distributions in this triple are 2 full house pairs
				count_freq += 1 # add 1 to the counter
		fh_freq[pair].append(count_freq) # after going through all the triples, add the final counter value to the corresponding pair

	#sorted_fh_freq = sorted(fh_freq.items(), key=operator.itemgetter(1)) # produce an ordered list of popular pairs
	return fh_freq


#### 3. FUNCTION CAN BE USED FOR BOTH PAIRS AND TRIPLES

#### 3.1. function for counting number of pairs/triples with at least n distributions being fullhouse

def count_fh(tuples, n): # tuples can either be pairs or triples; n is the number of full house distributions in the pairs/triples
	n_fh = [] # list to store pairs/cycles with at least 2 full houses
	for tup in tuples:
		t = 0 # initiate a counter for number of full houses in the pairs/triple
		for p in tup:
			if p in fullhouse:
				t += 1 # add 1 to the counter if p is full house
		if t >= n:
			n_fh.append(tup) # add the pair/triple to the set if there are more than or equal to n number of full houses

	return n_fh

#### 3.2. function for growing triples from a pair of 2 full house

def fh_grow_triples(fh_pairs): # fh_pairs is the set of pairs which have 2 full house distributions
	fh_grow = [] # list to store triples

	for pair in fh_pairs: # pick a full house pairs
		(f1, f2) = pair 
		for key in nodes: # go through the list of distributions, start from distribution i
			if f1 in nodes[key] and f2 in nodes[key]: # if distribution i can be assigned to both full house f1 and f2
				triple = tuple(sorted((key, f1, f2))) # a triple is found consisting of i, f1, f2; this is sorted in ascending order
				if triple in fh_grow: # ignore if this triple is already found
					continue
				else:
					fh_grow.append(triple) # otherwise, add to the list

	fh_grow2 = remove_comp_triples(fh_grow) # remove the complement triples
	return fh_grow2







