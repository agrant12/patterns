import sys, re
from timeit import Timer

#Global variables for input and output text files
inFile = sys.argv[1]
outFile = sys.argv[2]

def pattern_match(inFile, outFile):
	#Create empty list for patterns and paths
	patterns = []
	paths = []
	
	#Separate strings into paths and patterns
	with open(inFile, 'r') as i:
		for line in i:
			if ',' in line:
				patterns.append(line)
			elif '/' in line:
				paths.append(line)
	i.closed
	with open(outFile, 'w') as o:
		#Extract paths list items for comparisons
		for path in paths:
			#Modify path for matching against patterns array
			path = path.strip('/\n').split('/')

			#Check length of path list
			if len(path) > 2:
				regex = re.compile(r"(" + path[0] + "),.*")
				match = [m.group() for pattern in patterns for m in [regex.match(pattern)] if m]
				
				o.write(match[0] + '\n')
			else:
				o.write("NO MATCH\n")
	o.closed

if __name__ == '__main__':
	#Instantiate Program
	pattern_match(inFile, outFile)
	
	#Calculate algorithm complexity & print ot terminal
	t = Timer("pattern_match", "from __main__ import pattern_match")
	print 'Runtime: ' + repr(t.timeit())