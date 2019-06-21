seq1 = "ATGAATCGCACCGCGGGTCCCGCTCTGTCGTACACTAGACTCTTAGTTAAGGGTACGCTTACCAAGCTGTGTTGATCTATCAGGGTTCGTGGACTTAGCTATATACCTGGATGCTCAGGACTCGCACGAGAACGAAAATTCCGCGTCACCACGAAAGTTCCGATATTGCTGTCACAAAAACGCAGTATTCATGGATCCTGATGTGTGCTTAAACACGGGCCTATATTCATACGATAGTCTTATGGCACTATTTGCGCGCACTGTATGACAGCAAAAAAGCTTGGAGCTAGGCGAAGTCCGAGACGTATTACAAACCACCCAATTCTAGGATCAATCACCATTCCTACGTAACACGCGTTCTCAGATTGTATGCGGTTTAATAGTACCTCGGGCGGATCCCCCAAATAATGCTCGATCCGTCTAGTCGTGTGTTCGACAGCGACCTAGGGAGGTGGCCGCAAGCATAGAGAAGCCGCGATCACGTTATCTGATGATGATGACAAAGCACTAATCCAGTATCTAGTCAGAAATAATGCAAAGCGACACTAGTACTAGTCCTCCCGTCCACGCCCACCGAGCTGTGCAAATTTCTTGTCTTCGATAGGGAACGATAACACGGCTGCCCACGTATCTCTGTCCGGTGGACACAGCAAGAGGGTTGAATGCAGATACGCTGTACAGTATGGATGTGTGTAATCTAAAGAAGCGGCGTAACTTTACCGCCATTCCCCGTTATCGAAGTTTTTAATCGGAGGACGCCAAATACACACACGCCGATCGTTCAGTGGGACCTGATAGGATGGTTATTTTCTTTGCGCACCGATCCTTATATCGAGAAACGTATACCTCTGGGATTAAGAGTAACATAGCCGATTCGATCCTTCCACGCATCGAGAGCCAAAAATTATAAGTCCACCGCTAAGTGTCCACGTCAACACGCGCAGGCGTTCGTAAACAGGCTTCACGAGGTGGCCTAATTGATACGC"
seq2 = "AGCAACTAGCCGTAGGGGCGCTCTATCTCGAATATCCGAATCGTACGTAAGGCTAGGTATCCCGACCTTTAATGTTTATGCATGGTGCTTCGCTACGCCATTTTAACGGAATGTACAGCCCTGGTAAGGGTGCAGCGACACTTAGGAGCGCCGGCATTACACAGAAAACCCTAAACTTAATGATGCTTTCGTGCACTCTTATTTTTGATCGCACGCGCGTTTATGATACCCTGCTGGTGCAAAATGTTTGGTTCCACGAACTATATAAAGTTAAATCCGCTTGTTGCTCAAGGCTCAGCCATACTAGATAATAACCACCTAATCCTCGGACCTAACGCCATCCAGTCCCATCAAGCGACCTCGTATGGTTTCGACTTTAATAATTTGTCGTGCGACCGCCTTTTAAGGTTGACATACGATTTGCAGGTGACGAAGCCGGCGGCAGCCGGAAATGGTCGTAGCTCTCGAGGACACGTGATCAACTTAGCGGTTGATGGCGTGAAAACTGTGACCTAAGGGCAGGTCCTAAACCAGGCAAACACACACCTTGTCTTGTGCTCCAGACCGCGTCCAACGGACGTTGCCGCATTCTCGATAATCGTCGGGAGCGGATTTAGAGGAGCACACATGACACTGCCCATTTTCCACGTCACTGGTCCTGCCAAGTGGTACCGTGCGCAGCATGTACGCTCATAATGTTAGCTTCTGGATCTACAGATCCGCCCTTGCACGTTATCGTAGTTTTGAATGGGGCCCCGCCATTCACAGTCAACAGGCCTGATTAGAAAGACAAATTAGCGAGGATATGATCTTCGCGCTGACAAACCTACCTTGTTAACCGTGCGCAGATATGTGGGAGTATTATATAAAGCGGCCGATCGAGGGATACATAGACTCCCTCATGTTATAAGAAGCGCGTCAACTGTGAACGTATGCATAAACAGGCGACTTCACAAGCCGGTACACCTCTCGCTGTATTCGAATGC"

def hamming_distance(string1, string2):

    distance = 0
    L = len(string1)

    print(" Sequence 1 is {0}, sequence 2 is {1}.\n The lengths are {2}.".format(seq1, seq2, L))

    for i in range(L):
        if string1[i] != string2[i]:
            distance += 1
    return distance


example_distance = hamming_distance(seq1, seq2)
