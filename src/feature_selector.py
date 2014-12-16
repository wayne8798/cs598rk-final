import os
import sys
import itertools

WEKA_PATH = "~/Downloads/weka-3-6-11/weka.jar"

def load_data(fn):
	with open(fn, 'r') as f:
		lines = f.readlines()
	attrs = []
	vecs = []
	for l in lines:
		if l[0] == '%':
			continue
		elif l[0] == '@':
			if l[:10] == '@attribute':
				attrs.append(l[11:-1])
		elif len(l) > 1:
			vecs.append(l[:-1])

	return [attrs, vecs]

def check_performance(path):
	output = os.popen("java -classpath " + WEKA_PATH \
		+ " weka.classifiers.bayes.NaiveBayes -t " + path).read()	

	results = []
	for line in output.split('\n'):
		if len(line) > 9 and line[:9] == 'Correctly':
			results.append(line)

	return float(results[-1].split()[-2])

def test_features_bruteforce(attrs, vecs):
	feats_count = len(attrs) - 1
	for i in range(1, feats_count + 1):
		set_indices = list(itertools.combinations(range(feats_count), i))
		for index in set_indices:
			new_attrs = [attrs[i] for i in index] + [attrs[-1]]

			new_vecs = []
			for v in vecs:
				new_vec = ','.join([v.split(',')[i] for i in index]) + ',' + v[-1]
				new_vecs.append(new_vec)

			test_arff = open('test.arff', 'w')
			test_arff.write('@relation test\n')
			for a in new_attrs:
				test_arff.write('@attribute ' + a + '\n')
			test_arff.write('@data\n')
			for v in new_vecs:
				test_arff.write(v + '\n')
			test_arff.close()

			print new_attrs
			print check_performance('test.arff')

def test_features_greedy(attrs, vecs):
	feats_count = len(attrs) - 1
	selected_feats = []
	feats_left = range(feats_count)

	while len(feats_left) > 0:
		selected_feat = -1
		best_performance = 0
		best_attrs = []

		for f in feats_left:
			index = selected_feats + [f]
			new_attrs = [attrs[i] for i in index] + [attrs[-1]]
	
			new_vecs = []
			for v in vecs:
				new_vec = ','.join([v.split(',')[i] for i in index]) + ',' + v[-1]
				new_vecs.append(new_vec)
	
			test_arff = open('test.arff', 'w')
			test_arff.write('@relation test\n')
			for a in new_attrs:
				test_arff.write('@attribute ' + a + '\n')
			test_arff.write('@data\n')
			for v in new_vecs:
				test_arff.write(v + '\n')
			test_arff.close()
	
			performance = float(check_performance('test.arff'))
			if performance > best_performance:
				best_performance = performance
				selected_feat = f
				best_attrs = new_attrs

		selected_feats += [selected_feat]
		feats_left.remove(selected_feat)

		print new_attrs[:-1]
		print best_performance

attrs, vecs = load_data(sys.argv[1])
test_features_greedy(attrs, vecs)

