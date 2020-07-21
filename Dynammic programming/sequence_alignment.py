# Problem: Given as an input two strings, X = x_{1} x_{2}... x_{m}, and Y = y_{1} y_{2}... y_{m}, output the alignment of the strings, character by character, 
#          so that the net penalty is minimised. 

gap_penalty = 3            # cost of gap
mismatch_penalty = 2       # cost of mismatch

memoScore = {}
memoSequence = {}

def sequenceAlignment(seq1, seq2):
    if (seq1,seq2) in memoScore:return memoScore[(seq1,seq2)]          # memoization

    if seq1 == "" and seq2 == "" :           # base case
        memoSequence[(seq1,seq2)] = ["",""]
        return 0

    elif seq1 == "" or seq2== "" :
        maxim = max(len(seq1),len(seq2))
        memoSequence[(seq1,seq2)] = [seq1.ljust(maxim,"_"), seq2.ljust(maxim,"_")]
        return gap_penalty*maxim


    penalty = 0 if seq1[0] == seq2[0] else mismatch_penalty           
    nogap = sequenceAlignment( seq1[1:],seq2[1:] ) + penalty        # cost of match/mistmatch
    seq1gap = sequenceAlignment( seq1,seq2[1:] ) + gap_penalty      # cost of gap in sequence 1
    seq2gap = sequenceAlignment( seq1[1:],seq2 ) + gap_penalty      # cost of gap in sequence 2

    if seq1gap < nogap and seq1gap <= seq2gap:
        result = seq1gap
        newSeq1 = "_" + memoSequence[(seq1,seq2[1:])][0]
        newSeq2 = seq2[0] + memoSequence[(seq1,seq2[1:])][1]

    elif seq2gap < nogap and seq2gap <= seq1gap:
        result = seq2gap
        newSeq1 = seq1[0] + memoSequence[(seq1[1:],seq2)][0]
        newSeq2 = "_" + memoSequence[(seq1[1:],seq2)][1]

    else:
        result = nogap
        newSeq1 = seq1[0] + memoSequence[(seq1[1:],seq2[1:])][0]
        newSeq2 = seq2[0] + memoSequence[(seq1[1:],seq2[1:])][1]


    memoScore[(seq1,seq2)] = result
    memoSequence[(seq1,seq2)] = [newSeq1,newSeq2]
    return result    



# Testing

sequence1 = "AGGGCT"
sequence2 = "AGGCA"

sequenceAlignment(sequence1,sequence2)
finalsequence = memoSequence[(sequence1,sequence2)]

print("First sequence : ", finalsequence[0])
print("Second sequence : ", finalsequence[1])
print("Min penalty : ",memoScore[(sequence1,sequence2)] )
