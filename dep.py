d0 = {'A':['B','C'],'B':['C'], 'C':['E'], 'D':['A']}
d1={}
d2 = {'A':['B','C'],'B':['C'], 'C':['E'], 'D':['A'], 'E':['D']}

def dept(dept):
	# Add any elements that are not in keys
	for ii in sum(list(dept.values()),[]):
		if ii not in list(dept.keys()):
			dept.update({ii:[]})

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
		if dept[t]:
			for i in dept[t]:
				# if the dependent value is already in the order, remove it
				if i in o: 	dept[t].remove(i)
			# if we found something not in the order add it to our stack
			if dept[t]: stack.insert(0,dept[t][0])

		#this has no dependents so add it to the order and delete it from the stack
		if not dept[t]:
			cc=[]
			if stack[0] not in o: o.append(stack[0])
			del stack[0]

	return o

print(dept(d0))
print(dept(d1))
print(dept(d2))