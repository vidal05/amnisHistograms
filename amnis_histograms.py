"""
The purpouse of this code is to generate histograms from data collected by AMNIS.
Please type the folder containing all the files, strains used in the experiment,
peptide number, time of data collection and data type (filtradas o todas)
"""

import numpy as np
import csv
import os
import inspect
from matplotlib import pyplot
import sys

def compare_strains(folder,strains,peptide,time,data_type): #data_type can be filtered or all (filtradas o todas)
	frame = inspect.currentframe()
	args, _, _, values = inspect.getargvalues(frame)
	experiments_data = []
	paths = []
	for strain in strains:
		paths.append("./%s/%s/%s/%s%s_%s.txt" % (folder,peptide, data_type,peptide,strain,time))
	for path in paths:
		if values["data_type"] == "filtradas":
			path = path[:-4]+"_filtradas.txt"
		data = []
		f = open(path)
		reader = csv.reader(f, delimiter='\t')
		for row in reader:
			if len(row) > 1 and not row[0][0].isalpha():
				data.append(float(row[1]))
		experiments_data.append(data)
	bins = np.linspace(3000,100000,100)
	for num, exp in enumerate(experiments_data):
		pyplot.hist(exp, bins, alpha=0.5, stacked=True, label=strains[num])
	pyplot.ylabel("Cells")
	pyplot.xlabel("Fluorescence intensity (AU)")
	pyplot.legend(loc="upper right")
	pyplot.show()

"""
filenames = next(os.walk(path))[2]
for filename in filenames:
	time = re.search(r'_[0-9]+',filename)
	data = [time.group()[1:]]
	f = open(os.path.join(path,filename))
	reader = csv.reader(f,delimiter='\t')
	for row in reader:
		if len(row) > 1 and not row[0][0].isalpha():
			data.append(float(row[1]))
	experiments_data.append(data)	

bins = np.linspace(5000,100000,150)
colors = ["black","red","chocolate","orange","olive","yellow","chartreuse","turquoise","darkblue","indigo","magenta","pink"]

for num, exp in enumerate(experiments_data):
	pyplot.hist(exp[1:], bins, alpha=0.5, stacked=False, color=colors[num], label=exp[0])
pyplot.legend(loc='upper right')
pyplot.show()
"""
compare_strains("amnis_170511",["a","alfa"],1,0,"filtradas")
#compare_strains(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5])
