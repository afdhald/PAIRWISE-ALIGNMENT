# PAIRWISE-ALIGNMENT
Needleman-Wunsch Algorithm
The Needleman–Wunsch algorithm is an algorithm used in bioinformatics to align protein or nucleotide sequences. It was one of the first applications of dynamic programming to compare biological sequences. The algorithm was developed by Saul B. Needleman and Christian D. Wunsch and published in 1970 (https://en.wikipedia.org/wiki/Needleman%E2%80%93Wunsch_algorithm).

T[i,j] = max{T[i-1,j-1]+sim(S1(i),S2(i), T[i-1,j]+gap penalty, T[i,j-1]+gap penalty]}

Reference: http://experiments.mostafa.io/public/needleman-wunsch/
