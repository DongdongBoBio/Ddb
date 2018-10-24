#统计行数
wc ERR332577.fastq ERR332578.fastq ERR332581.fastq ERR332585.fastq ERR332588.fastq ERR332593.fastq ERR470101.fastq  ERR470103.fastq ERR470105.fastq >> fastq.info

########### 思路 #######################
# ERR332574共709400684行，也就是177350171段序列（目前最少的一个文件有167622281条序列）
# 1. 在1~177350171范围内生成167620000个互不相同的随机整数。  for i in random.sample(range(177350170),167620000):
# 2. @开头的序列标识行所在的行数应该是4*i
# 3. 将第4*i、4*i+1、4*i+2、4*i+3行提取出来


######## 以下是脚本 ###############

# -*- coding:utf-8 -*-

# 用法：python test.py 输入文件 输出文件 输入文件中的序列数(总行数/4 - 1)

from sys import argv
import random
import string

script, from_file, to_file, number_of_sequence = argv # number_of_sequence刚输入时，是字符串类型

n = string.atoi(number_of_sequence) # 将number_of_sequence转化为数字类型

with open(from_file,'r') as input_file, open(to_file,'w') as output_file:
	line = input_file.readlines()
	for i in random.sample(range(n),167620000): # 因为要提取的序列数是固定的(167620000)，所以就不另设参数了
		output_file.write(line[4*i])
		output_file.write(line[4*i+1])
		output_file.write(line[4*i+2])
		output_file.write(line[4*i+3])
	input_file.close()
	output_file.close()
	
######################################################################	
	
	
	
	
	
	

