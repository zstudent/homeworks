# Question 6

def readGenome(filename):
    genome = ''
    with open(filename, 'r') as f:
        for line in f:
            if not line[0] == '>':
                genome += line.rstrip()
    return genome


def reverseComplement(sequence):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', 'N': 'N'}
    t = ''
    for base in sequence:
        t = complement[base] + t
    return t


def naive_2mm(p, t):
    occurrences = []
    for i in range(len(t) - len(p) + 1):
        mismatches = 0
        for j in range(len(p)):
            if t[i + j] != p[j]:
                mismatches += 1
                if mismatches > 2:
                    break
        if mismatches <= 2:
            occurrences.append(i)
            break
    return occurrences


seq = "AGGAGGTT"

print(naive_2mm(seq, readGenome("lambda_virus.fa")))
