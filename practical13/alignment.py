import numpy as np
from Bio import SeqIO
def load_fasta(filename):
    with open(filename) as f:
      record = SeqIO.read(f, "fasta")
    return str(record.seq)
human_seq=load_fasta(r"C:\Users\lenovo\Desktop\新建文件夹\IBI1_2024-25\practical13\human sequence.fasta")
mouse_seq=load_fasta(r"C:\Users\lenovo\Desktop\新建文件夹\IBI1_2024-25\practical13\mouse sequence.fasta")
random_seq=load_fasta(r"C:\Users\lenovo\Desktop\新建文件夹\IBI1_2024-25\practical13\random sequence.fasta")

def load_blosum(filename):
    blosum={}
    with open(filename) as f:
        while True:
            line = f.readline()
            if not line.startswith("#"):
               break
        amino_acids = line.strip().split()
        for line in f:
            if line.strip() == "":
                continue
            parts = line.strip().split()
            aa = parts[0]
            scores= list(map(int, parts[1:]))
            blosum[aa] = {k:v for k,v in zip(amino_acids, scores)}

    return blosum

blosum62 = load_blosum(r"C:\Users\lenovo\Desktop\新建文件夹\IBI1_2024-25\practical13\BLOSUM.txt")

def calculate_alignment(seq1, seq2, matrix):
    score=0
    identical=0
    for aa1, aa2 in zip(seq1, seq2):
        score += matrix[aa1][aa2]
        if aa1 == aa2:
            identical += 1
    
    percent_identity = (identical / len(seq1)) * 100
    return score, percent_identity
print("comparing results")
score1,identity1=calculate_alignment(human_seq,mouse_seq,blosum62)
print(f"human-mouse: score={score1}, identity={identity1}%")
score2,identity2=calculate_alignment(human_seq,random_seq,blosum62)
print(f"human-random: socre={score2}, identity={identity2}%")
score3,identity3=calculate_alignment(mouse_seq,random_seq,blosum62)
print(f"mouse-random: score={score3}, identity={identity3}%")
