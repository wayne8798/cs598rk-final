vindex = []
with open('../data/feats/allvids_order.txt', 'rb') as f:
	for row in f:
		vindex.append(int(row))

vauto = []
with open('../data/feats/allvids_auto.arff', 'rb') as f:
	for row in f:
		if not '@' in row:
			vauto.append(row)

vmanu = []
with open('../data/feats/allvids_manu.csv', 'rb') as f:
	for row in f:
		if not 'ID' in row:
			vmanu.append(row)

with open('../data/feats/allvids_all.arff', 'wb') as f:
	f.write("@relation allvids*allfeats\n")
	f.write("@attribute id NUMERIC\n")
	f.write("@attribute letterfcount NUMERIC\n")
	f.write("@attribute digitfcount NUMERIC\n")
	f.write("@attribute spcharfcount NUMERIC\n")
	f.write("@attribute scenecount NUMERIC\n")
	f.write("@attribute openinglen NUMERIC\n")
	f.write("@attribute endinglen NUMERIC\n")
	f.write("@attribute stimgcount NUMERIC\n")
	f.write("@attribute isCG NUMERIC\n")
	f.write("@attribute moneyfcount NUMERIC\n")
	f.write("@attribute framewidth NUMERIC\n")
	f.write("@attribute frameheigth NUMERIC\n")
	f.write("@attribute framepersec NUMERIC\n")
	f.write("@attribute duration NUMERIC\n")
	f.write("@attribute framecount NUMERIC\n")
	f.write("@attribute blackcount NUMERIC\n")
	f.write("@attribute whitecount NUMERIC\n")
	f.write("@attribute grayscount NUMERIC\n")
	f.write("@attribute facecount NUMERIC\n")
	f.write("@attribute faceavelocx NUMERIC\n")
	f.write("@attribute faceavelocy NUMERIC\n")
	f.write("@attribute facesumarea NUMERIC\n")
	f.write("@data\n")
	for i in range(len(vauto)):
		f.write(vmanu[vindex[i]][:-1]+','+vauto[i])
