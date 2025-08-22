header_count.py finds the total number of headers (the total number of records) in a fasta file. A header begins with '>' and provides a unique identifier for a sequence. It tells us how many sequences are in the file.

sequence_length.py returns the shortest and longest sequences in a fasta file.

reading_frame.py  finds the longest open reading frame (ORF) in a file. It also finds the identifier for the sequence that contains the longest ORF, and the starting position for the ORF in that sequence. An open reading frame starts with an 'ATG' codon and ends with either a 'TAA', 'TAG', or a 'TGA' codon. ORFs are able to encode proteins.

repeat.py returns the number of all repeats of length n in all sequences in a file.