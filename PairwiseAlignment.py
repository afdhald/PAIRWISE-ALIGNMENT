import numpy
##seq1 = "ATGCGT"
##seq2 = "ACGCGA"
##match = 1
##unmatch = -1
#gap_score = -2

seq1 = input("Sequence 1: ")
seq2 = input("Sequence 2: ")
match_score = int(input("Match Score: "))
unmatch_score = int(input("Unmatch Score: "))
gap_score = int(input("Gap Score:"))

rows, columns = len(seq1)+1, len(seq2)+1
table = numpy.zeros((rows, columns), int)

def sim(a,b):
    val = 1
    if a==b:
        val = match_score
    else:
        val = unmatch_score
        
    return int(val)

for i in range(rows):
    table[i][0] = i*gap_score

for j in range(columns):
    table[0][j] = j*gap_score

for i in range(1, rows):
    for j in range(1, columns):
        diagonal = table[i-1][j-1] + sim(seq1[i-1],seq2[j-1])
        atas = table[i][j-1] + gap_score
        kiri = table[i-1][j] + gap_score
        table[i][j] = max(diagonal, atas, kiri)

print(table)

i, j = rows-1, columns-1
x = i*j
seq1_new = seq2_new = ""
skor = 0
while i>0 and j>0:
    score = table[i][j]
    diag = table[i-1][j-1]
    up = table[i-1][j]
    left = table[i][j-1]
    
    if score == left+gap_score:
        seq1_new = "-" + seq1_new
        seq2_new = seq2[j-1] + seq2_new
        j -= 1
        skor = skor + gap_score
    elif score == up+gap_score:
        seq1_new = seq1[i-1] + seq1_new
        seq2_new = "-" + seq2_new
        i -= 1
        skor = skor + gap_score
    elif score == diag + sim(seq1[i-1],seq2[j-1]):
        seq1_new = seq1[i-1] + seq1_new
        seq2_new = seq2[j-1] + seq2_new
        if (sim(seq1[i-1],seq2[j-1])) == 1:
            skor = skor + match_score
        else:
            skor = skor + unmatch_score
        i -= 1
        j -= 1

while i > 0:
    seq1_new = seq1[i-1] + seq1_new
    seq2_new = "-" + seq2_new
    skor = skor + gap_score    
    i -= 1
    
while j > 0:
    seq1_new = "-" + seq1_new
    seq2_new = seq2[j-1] + seq2_new
    skor = skor + gap_score 
    j -= 1

print("Hasil Alignment :")    
print(seq1_new)
print(seq2_new)
print('score = ',skor)
        
