def find_restriction_sites(dna_sequence, enzyme_sequence):
    valid_nucleotides = set('ACGT')
    if not set(dna_sequence).issubset(valid_nucleotides) or not set(enzyme_sequence).issubset(valid_nucleotides):
        raise ValueError("Both sequences should only contain ACGT nucleotides")
    cut_sites = []
    for i in range(len(dna_sequence) - len(enzyme_sequence) + 1):
        if dna_sequence[i:i+len(enzyme_sequence)] == enzyme_sequence:
            cut_sites.append(i)
    return cut_sites

# 函数调用示例
try:
    dna = "ACGTCGATCGATCGATCGACGT"
    enzyme = "CGAT"
    result = find_restriction_sites(dna, enzyme)
    print(f"The restriction enzyme cut sites are at positions: {result}")
except ValueError as e:
    print(e)