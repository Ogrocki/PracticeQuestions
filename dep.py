dep = {'A':['B','C'],'B':['C'], 'C':['E'], 'D':['A']}
d0={}
d1 = {'A':['B','C'],'B':['C'], 'C':['E'], 'D':['A'], 'E':['D']}

def dept(dept):
	# Add any elements that are not in keys
	for ii in sum(list(dept.values()),[]):
		if ii not in list(dept.keys()):
			dep.update({ii:[]})

	# Build my stack with all keys
	stack = list(dept.keys())
	cc = []
	# Empty first order in case of empty dict
	o=[]

	while stack:
		# t is the top of the stack
		t=stack[0]

		# Check for cycles
		if t in cc : return "Graph has a cycle"
		else: cc.append(t)


		# if there are values dependent on t
		if dep[t]:
			for i in dep[t]:
				# if the dependent value is already in the order, remove it
				if i in o: 	dep[t].remove(i)
			# if we found something not in the order add it to our stack
			if dep[t]: stack.insert(0,dep[t][0])

		#this has no dependents so add it to the order and delete it from the stack
		if not dept[t]:
			cc=[]
			if stack[0] not in o: o.append(stack[0])
			del stack[0]

	return o

print(dept(dep))
print(dept(d0))
print(dept(d1))