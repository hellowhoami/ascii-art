# usage:
# python3 echo-ascii.py <input> <output>

import sys

input = sys.argv[1]
output = sys.argv[2] + ".sh" 

with open(input, 'r') as rf:
	with open(output, 'w') as wf:
		wf.write("#!/bin/sh\n")
		for line in rf:
			wf.write("echo \"" + line.rstrip("\n") + "\"\n")







