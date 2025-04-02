# 定义TATA box的保守序列模式，这里使用TATAWAW，W代表A或T
tata_pattern = r"TATA[AT][AT][AT]"
import re

# 打开输入文件（从Learn下载的文件）
with open('C:\\Users\\lenovo\\Downloads\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r') as infile:
    current_gene_name = ""
    current_gene_sequence = ""
    # 打开输出文件用于保存结果
    with open('tata_genes.fa', 'w') as outfile:
        for line in infile:
            if line.startswith('>'):
                # 如果遇到新的基因序列头，先处理上一个基因
                if current_gene_name:
                    if re.search(tata_pattern, current_gene_sequence):
                        outfile.write(current_gene_name + '\n')
                        outfile.write(current_gene_sequence + '\n')
                current_gene_name = line.strip()
                current_gene_sequence = ""
            else:
                current_gene_sequence += line.strip()
        # 处理最后一个基因
        if current_gene_name:
            if re.search(tata_pattern, current_gene_sequence):
                outfile.write(current_gene_name + '\n')
                outfile.write(current_gene_sequence + '\n')