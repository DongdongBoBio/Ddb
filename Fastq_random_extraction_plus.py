#-*- coding:utf-8 -*-

# 本例为提取10%的序列

from sys import argv
import random

script, from_file, to_file = argv

with open(from_file, "r") as f1, open(to_file, "w") as f2:
	i=5
	temp_reads = []
	line = f1.readline()
	for line in f1:
		if i % 4 == 0:
			rand_i = random.randint(1,100)
			if rand_i < 10:
				f2.write("".join(temp_reads))
			temp_reads = []
			temp_reads.append(line)
		else:
			temp_reads.append(line) 
		i = i + 1