#### import data

from molsfunc import *

#### RESULTS FOR PAIRS ####

pairs = list(generate_pairs(nodes)) ## generate pairs
fh_pairs = count_fh(pairs, 2) ## count for pairs with 2 full houses

print "----------------------------------------------------------------"
print "*** RESULTS FOR PAIRS ***"

#### The number of pairs including complement pairs

print "The number of assignable pairs including complement pairs is", len(pairs)

#### The number of pairs excluding complement pairs

nocomp_pairs = remove_comp_pairs(pairs) ## remove complement pairs
print "The number of assignable pairs excluding complement pairs is", len(nocomp_pairs)

#### The number of pairs with both distributions being full house

print "The number of assignable pairs with 2 distributions being full house is", len(fh_pairs)
print "----------------------------------------------------------------"

#### RESULTS FOR TRIPLES ####

cycles = list(generate_triples(nodes)) ## generate triples
two_fh_triples = count_fh(cycles, 2) ## count for triples with >= 2 full houses
three_fh_triples = count_fh(cycles, 3) ## count for triples with 3 full houses
triples_grow = fh_grow_triples(fh_pairs) ## grow triples from pairs with 2 full houses

print "*** RESULTS FOR TRIPLES ***"

#### The number of triples including complement triples

print "The number of mutually assignable triples including complement triples is", len(cycles)

#### The number of triples excluding complement triples

nocomp_triples = remove_comp_triples(cycles) ## remove complement triples
print "The number of mutually assignable triples excluding complement triples is", len(nocomp_triples)
print "----------------------------------------------------------------"

#### Full house including complement triples
print "-*- Including complement triples -*-"
#### The number of triples with at least 2 full houses

print "The number of mutually assignable triples with at least 2 distributions being full house is", len(two_fh_triples)

#### The number of triples with 3 full houses

print "The number of mutually assignable triples with 3 distributions being full house is", len(three_fh_triples)
print "----------------------------------------------------------------"

#### Full house excluding complement triples
print "-*- Excluding complement triples -*-"
#### The number of triples with at least 2 full houses

two_fh_triples = count_fh(cycles, 2) ## count for triples with >= 2 full houses
print "The number of mutually assignable triples with at least 2 distributions being full house is", len(two_fh_triples)

#### The number of triples with 3 full houses

three_fh_triples = count_fh(cycles, 3) ## count for triples with 3 full houses
print "The number of mutually assignable triples with 3 distributions being full house is", len(three_fh_triples)
print "----------------------------------------------------------------"

#### The number of triples obtained by growing from pairs with 2 full houses

print "The number of mutually assignable triples obtained by growing from pairs of 2 full house distributions is", len(triples_grow)

#### The frequencies of recurrence of popular pairs in the triples

print "The frequencies of recurrence of popular full house pairs in the mutually assignable triples"
top_fh_freq = count_fh_freq(triples_grow, fh_pairs)

for k, v in top_fh_freq.items():
	for i in v:
		if i >= 70:
			print k, v



