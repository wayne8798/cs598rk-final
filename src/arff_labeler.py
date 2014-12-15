import sys

with open('percent.dat', 'r') as f:
	raw_data = f.readlines()

percent_data = {}
for line in raw_data:
	pair = line[:-1].split()
	percent_data[int(pair[0])] = float(pair[1])

with open('allvids_order.txt') as f:
	percent_lines = f.readlines()


arff_fname = sys.argv[1]
assert(arff_fname[-5:] == '.arff')

new_fname = arff_fname[:-5] + '_labeled.arff'
fout = open(new_fname, 'w')

with open(arff_fname, 'r') as f:
	count = 0
	for l in f.readlines():
		if l[0] == '@':
			fout.write(l)
		else:
			p = percent_data[int(percent_lines[count][:-1])]
			if p >= 3:
				fout.write(l[:-1] + ',T\n')
			else:
				fout.write(l[:-1] + ',F\n')
			count += 1

fout.close()
