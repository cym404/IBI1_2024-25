import re


def spliced_tata_genes():
    # 定义可能的剪接供体/受体组合
    splice_combinations = ["GTAG", "GCAG", "ATAC"]
    user_combination = input(f"Please enter one of the splice donor/acceptor combinations {splice_combinations}: ")
    while user_combination not in splice_combinations:
        print("Invalid input. Please try again.")
        user_combination = input(f"Please enter one of the splice donor/acceptor combinations {splice_combinations}: ")

    output_file_name = f"{user_combination}_spliced_genes.fa"
    tata_pattern = r"TATA[AT][AT][AT]"
    spliced_genes = []

    with open('C:\\Users\\lenovo\\Downloads\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r') as infile:
        current_gene_name = ""
        current_gene_sequence = ""
        for line in infile:
            if line.startswith('>'):
                if current_gene_name:
                    if user_combination in current_gene_sequence:
                        tata_count = len(re.findall(tata_pattern, current_gene_sequence))
                        if tata_count > 0:
                            new_gene_name = f"{current_gene_name}_{tata_count}"
                            spliced_genes.append((new_gene_name, current_gene_sequence.replace('\n', '')))
                current_gene_name = line.strip().lstrip('>')
                current_gene_sequence = ""
            else:
                current_gene_sequence += line

        # 处理最后一个基因
        if current_gene_name:
            if user_combination in current_gene_sequence:
                tata_count = len(re.findall(tata_pattern, current_gene_sequence))
                if tata_count > 0:
                    new_gene_name = f"{current_gene_name}_{tata_count}"
                    spliced_genes.append((new_gene_name, current_gene_sequence.replace('\n', '')))

    with open(output_file_name, 'w') as outfile:
        for gene_name, gene_sequence in spliced_genes:
            outfile.write(f">{gene_name}\n{gene_sequence}\n")


if __name__ == "__main__":
    spliced_tata_genes()