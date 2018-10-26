# Ddb

#脚本说明：
Fastq_random_extraction.py
功能：
从fastq文件中随机提取一定数量的“记录”（从序列标识到phred质量值的4行合称1条“记录”），适用于采用个体DNA建库的全基因组重测序之后的“人工混池”。

Fastq_random_extraction_plus.py
功能同Fastq_random_extraction.py，改进了算法，同时避免了一次将fastq文件读入内存，优化了运算速度。