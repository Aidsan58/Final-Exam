""" A reading frame is a way of dividing the DNA sequence of nucleotides into codons,
which are defined as consecutive, non-overlapping triplets. An open reading frame, or ORF, can encode a protein.
It starts with a start codon (ATG), and ends with a stop codon (TAA; TAG; TGA). """

def reading_frame(filename):
    """ Finds the longest open reading frame (ORF). """
    current_reading_frame = ''
    longest_reading_frame = 0
    with open(filename, 'r') as f:
        for line in f:
            if line.startswith('>'):
                if line.startswith('ATG'):
                    if line.endswith('TAA', 'TAG', 'TGA'):
                        if len(current_reading_frame) > longest_reading_frame:
                            longest_reading_frame = len(current_reading_frame)
                    current_reading_frame = ''
            else:
                current_reading_frame += line.strip()

        if len(current_reading_frame) > longest_reading_frame:
            longest_reading_frame = len(current_reading_frame)
                    
                

