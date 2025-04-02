
seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'
import re

intron_lengths = []
matches = re.finditer(r'GT(.+?)AG', seq)
for match in matches:
    print(len(match.group(0)))