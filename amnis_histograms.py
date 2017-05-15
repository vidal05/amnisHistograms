import numpy as np
import csv
import os
import re
import inspect
from matplotlib import pyplot
import sys

experiments_data = []

#path = "./amnis_170511/1/filtradas/"

def compare_strains(peptide,time,data_type): #data_type can be filtered or all (filtradas o todas)
	frame = inspect.currentframe()
	args, _, _, values = inspect.getargvalues(frame)
	strains = ["a","alfa","delta_bar1"]
	experiments_data = []
	#mat_a = "./amnis_170511/%s/%s/%s%s_a_%s.txt" % (peptide, data_type,peptide,exp_num,time)
	#mat_alfa = "./amnis_170702/%s/%s/%s%s_alfa_%s.txt" % (peptide, data_type,peptide,exp_num,time)
	#delta_bar1 = "./amnis_170420/%s/%s/%sBAR1delta_%s.txt" % (peptide, data_type,peptide,time)
	mat_a = "./amnis_170511/%s/%s/%sa_%s.txt" % (peptide, data_type,peptide,time)
	mat_alfa = "./amnis_170511/%s/%s/%salfa_%s.txt" % (peptide, data_type,peptide,time)
	if values["data_type"] == "filtradas":
		mat_a = mat_a[:-4]+"_filtradas.txt"
		mat_alfa = mat_alfa[:-4]+"_filtradas.txt"
		#delta_bar1 = delta_bar1[:-4]+"_filtradas.txt"
	paths = [mat_a,mat_alfa]#,delta_bar1]
	for path in paths:
		data = []
		f = open(path)
		reader = csv.reader(f, delimiter='\t')
		for row in reader:
			if len(row) > 1 and not row[0][0].isalpha():
				data.append(float(row[1]))
		experiments_data.append(data)
	bins = np.linspace(3000,200000,100)
	#f, axarr = pyplot.subplots(3,4)
	#for i in range(13):
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
compare_strains(sys.argv[1],sys.argv[2],sys.argv[3])
