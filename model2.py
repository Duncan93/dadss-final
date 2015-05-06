import json

info = {
	"assumptions": {
		"Natural Light": {
			"Basement": 0,
			"First": 0.95,
			"Second": 0.15,
			"Third": 0.9,
			"Fourth": 0.25
		},
		"Close to Outlet": {
			"Basement": 0.3,
			"First": 0.35,
			"Second": 0.45,
			"Third": 0.95,
			"Fourth": 0.6
		},
		"Quietness": {
			"Basement": 0.05,
			"First": 0.05,
			"Second": 0.15,
			"Third": 1,
			"Fourth": 0.4
		},
		"Close to Food": {
			"Basement": 0.7,
			"First": 1,
			"Second": 0.7,
			"Third": 0.35,
			"Fourth": 0
		},
		"Working Alone": {
			"Basement": 0.1,
			"First": 0.1,
			"Second": 0.15,
			"Third": 1,
			"Fourth": 0.45
		},
		"Total Chairs": {
			"Basement": 33.0,
			"First": 70.0,
			"Second": 72.0,
			"Third": 146.0,
			"Fourth": 76.0
		}
	},
	"availability": {
		"Monday": {
			"10:30 AM": {
				"Basement": 24,
				"First": 41,
				"Second": 29,
				"Third": 51,
				"Fourth": 32
			},
			"1:30 PM": {
				"Basement": 18,
				"First": 38,
				"Second": 28,
				"Third": 43,
				"Fourth": 20
			},
			"4:30 PM": {
				"Basement": 8,
				"First": 21,
				"Second": 18,
				"Third": 14,
				"Fourth": 17
			},
			"7:30 PM": {
				"Basement": 16,
				"First": 30,
				"Second": 20,
				"Third": 30,
				"Fourth": 21
			},
			"10:30 PM": {
				"Basement": 23,
				"First": 13,
				"Second": 13,
				"Third": 9,
				"Fourth": 14
			}
		},
		"Tuesday": {
			"10:30 AM": {
				"Basement": 19,
				"First": 45,
				"Second": 21,
				"Third": 42,
				"Fourth": 23
			},
			"1:30 PM": {
				"Basement": 15,
				"First": 30,
				"Second": 16,
				"Third": 30,
				"Fourth": 15
			},
			"4:30 PM": {
				"Basement": 14,
				"First": 16,
				"Second": 17,
				"Third": 18,
				"Fourth": 13
			},
			"7:30 PM": {
				"Basement": 18,
				"First": 13,
				"Second": 15,
				"Third": 20,
				"Fourth": 18
			},
			"10:30 PM": {
				"Basement": 17,
				"First": 33,
				"Second": 19,
				"Third": 39,
				"Fourth": 17
			}
		},
		"Wednesday": {
			"10:30 AM": {
				"Basement": 28,
				"First": 25,
				"Second": 41,
				"Third": 64,
				"Fourth": 43
			},
			"1:30 PM": {
				"Basement": 14,
				"First": 32,
				"Second": 11,
				"Third": 38,
				"Fourth": 15
			},
			"4:30 PM": {
				"Basement": 17,
				"First": 17,
				"Second": 11,
				"Third": 21,
				"Fourth": 13
			},
			"7:30 PM": {
				"Basement": 14,
				"First": 16,
				"Second": 29,
				"Third": 42,
				"Fourth": 12
			},
			"10:30 PM": {
				"Basement": 18,
				"First": 22,
				"Second": 24,
				"Third": 44,
				"Fourth": 16
			}
		},
		"Thursday": {
			"10:30 AM": {
				"Basement": 21,
				"First": 39,
				"Second": 26,
				"Third": 55,
				"Fourth": 27
			},
			"1:30 PM": {
				"Basement": 15,
				"First": 20,
				"Second": 16,
				"Third": 38,
				"Fourth": 18
			},
			"4:30 PM": {
				"Basement": 17,
				"First": 14,
				"Second": 15,
				"Third": 24,
				"Fourth": 14
			},
			"7:30 PM": {
				"Basement": 17,
				"First": 51,
				"Second": 30,
				"Third": 61,
				"Fourth": 28
			},
			"10:30 PM": {
				"Basement": 21,
				"First": 30,
				"Second": 20,
				"Third": 49,
				"Fourth": 24
			}
		},
		"Friday": {
			"10:30 AM": {
				"Basement": 18,
				"First": 25,
				"Second": 37,
				"Third": 44,
				"Fourth": 32
			},
			"1:30 PM": {
				"Basement": 22,
				"First": 41,
				"Second": 41,
				"Third": 42,
				"Fourth": 27
			},
			"4:30 PM": {
				"Basement": 20,
				"First": 20,
				"Second": 34,
				"Third": 37,
				"Fourth": 31
			},
			"7:30 PM": {
				"Basement": 28,
				"First": 38,
				"Second": 39,
				"Third": 42,
				"Fourth": 20
			},
			"10:30 PM": {
				"Basement": 30,
				"First": 43,
				"Second": 40,
				"Third": 44,
				"Fourth": 34
			}
		}
	}
}

# These will change according to simulations
weight = {'Close to Outlet': 4, 'Working Alone': 1, 'Natural Light': 4, 'Close to Food': 4, 'Quietness': 1}
rank = {'Close to Outlet': 1, 'Working Alone': 2, 'Natural Light': 5, 'Close to Food': 3, 'Quietness': 4} # 1 is most important, so rank * of 5
day = 'Thursday'
time = '1:30 PM'

preferences = ['Close to Outlet','Working Alone','Natural Light','Close to Food','Quietness']

# Adjust weight to scoring standard (opposite scale than rank)
adjusted_weight = {}
for p in preferences:
	if weight[p] == 5: # least important
		adjusted_weight[p] = 1
	elif weight[p] == 4:
		adjusted_weight[p] = 0.75
	elif weight[p] == 3:
		adjusted_weight[p] = 0.5
	elif weight[p] == 2:
		adjusted_weight[p] = 0.25
	elif weight[p] == 1: # most important
		adjusted_weight[p] = 0

# Adjust rank to scoring standard
adjusted_rank = {}
# add adjusted ranks
for r in rank.keys():
	adjusted_rank[r] = 6 - rank[r] # 5 turns into multiplier of 1; 1 turns into multiplier of 5

print adjusted_rank
print adjusted_weight

# Load assumption and availability data
# with open('assumptions.json', 'r') as f:
# 	info = f.read()
# info = json.loads(info)
assumptions = info["assumptions"]
total_chairs = info["assumptions"]["Total Chairs"]
availability = info["availability"][day][time]
# Turn availabilities into probabilities
for t in total_chairs:
	availability[t] /= total_chairs[t]

floors = ['Basement','First','Second','Third','Fourth']


# Find utility given a assumption, rank, weight, availability, and if a 'no' path is followed
def utility(p, r, w, a, invert):
	if invert: return (1-p)*r*(1-w)*a
	else: return p*r*w*a

with open('tree2.json','r') as f:
	tree = f.read()
tree = json.loads(tree)
options = tree['paths']

# iterate through options
for o in options:
	# iterate through choice node indexes
	for c in xrange(len(o['path'])):
		# see if inverse is needed
		if o['path'][c] == "no": i = True
		else: i = False
		# iterate through preferences in adjusted_rank dict
		for p in adjusted_rank.keys():
			# check that rank applies to correct node
			if 5 - adjusted_rank[p] == c: # ex. c = 0 means first node; assign multiplier then
				r_mult = adjusted_rank[p]
				w_mult = adjusted_weight[p]
				# iterate through floors
				for f in floors:
					# calculate utility
					u = utility(assumptions[p][f], r_mult, w_mult, availability[f], i)
					# add utility to this option's floor's utility
					o[f] += u

with open("tree_results.json","w") as f:
    f.write(str(json.dumps(options, indent=2)))

def find_best_overall():
	# calculate best option(s)
	best_paths = []
	best_floors = []
	best_utility = 0
	# iterate through options
	for o in options:
		# iterate through floors
		for f in floors:
			# if utility is highest, change values
			if o[f] > best_utility: 
				best_utility = o[f]
				best_paths = [o['path']]
				best_floors = [f]
			# if utility is tied, add floor to values
			elif o[f] == best_utility:
				best_paths.append(o['path'])
				best_floors.append(f)
	print best_paths
	print best_floors
	print best_utility

def find_best_results():
	# Initialize variables with [path, floor, utility]
	forgo_none = [['yes','yes','yes','yes','yes'], '', 0]
	forgo_5 = [['yes','yes','yes','yes','no'], '', 0]
	forgo_45 = [['yes','yes','yes','no','no'], '', 0]
	forgo_345 = [['yes','yes','no','no','no'], '', 0]
	endings = [forgo_none, forgo_5, forgo_45, forgo_345]
	# Iterate through options
	for o in options:
		# Iterate through endings
		for e in endings:
			# Check if path matches
			if e[0] == o['path']:
				best_utility = 0
				best_floor = ''
				# Iterate through floors
				for f in floors: # For the sake of time I'm avoiding duplicates
					# Find best utility
					if o[f] > best_utility:
						best_utility = o[f]
						best_floor = f
				e[1] = best_floor
				e[2] = round(best_utility, 3)
	for g in endings: 
		print g

find_best_results()

"""
Next:
It would be cool if I could simulate every single possible rank, weight, day and time.
This might be too computationally intensive, so why don't I start out with:
1. Refactor code into functions within a class and test
2. Given the current ranks and weights, generate a file with the results for all possible days and times
3. Do 2 but go through all possible ranks
4. Do 3 but go through all possible weights
5. Figure out how to analyze this data


"""



"""
Notes:
Although it may be too early to tell if there are common results since this isn't integrating the proper data yet, we may want to consider a function governing option for alternative solutions based on user rankings. For example, although we ask for 5 preferences, we can assume the first three are the most important, and later ones are less so (We should analyze user surveys to see the probability of each preference being in the top 3). Based on this assumption, students will be seeking out those things specifically, so we can eliminate the alternatives in those cases (i.e. get rid of the "no" branch). That leaves alternatives ("no" branch) for the remaining two preferences. This may be a good approach because it reduces the overall complexity of the tree, as well as alternatives students may not care for.
A different way to do this would be to analyze the following alternatives: yyyyn, yyyny, yynyy, ynyyy, nyyyy

"""
	