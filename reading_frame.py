""" A reading frame is a way of dividing the DNA sequence of nucleotides into codons,
which are defined as consecutive, non-overlapping triplets. An open reading frame, or ORF, can encode a protein.
It starts with a start codon (ATG), and ends with a stop codon (TAA; TAG; TGA). """

def reading_frame(filename):
    """ Finds the longest open reading frame (ORF). """

    def find_longest_frame(seq):
         start_codon = 'ATG'
         stop_codon = {'TAA', 'TAG', 'TGA'}
         longest_reading_frame = ''
         position = 0

         for k in range(3):
              i = k
              while i < len(seq) - 2:
                   codon = seq[i:i+3]
                   if codon == start_codon:
                        position = i
                        j = i + 3
                        while j < len(seq) - 2:
                                next_codon = seq[j:j+3]
                                if next_codon in stop_codon:
                                    orf = seq[i:j+3]
                                    if len(orf) > len(longest_reading_frame): # If the open reading frame we found is longer than the previous longest one, it replaces it.
                                        longest_reading_frame = orf
                                    break
                                j += 3
                        i = j + 3
                   else:
                        i += 3
         return longest_reading_frame, position

    longest_reading_frame = ''
    longest_identifier = ''

    with open(filename, 'r') as f:
         current_identifier = None
         current_seq = []

         for line in f:
              line = line.strip()
              if line.startswith('>'):
                   if current_identifier is not None:
                        seq = ''.join(current_seq).upper()
                        orf = find_longest_frame(seq)
                        if len(orf) > len(longest_reading_frame):
                             longest_reading_frame = orf
                             longest_identifier = current_identifier

                   current_identifier = line[1:].split()[0] # This gets the ID from the header.
                   current_seq = []
              else:
                    current_seq.append(line)

         if current_identifier is not None:
               seq = ''.join(current_seq).upper()
               orf = find_longest_frame(seq)
               if len(orf) > len(longest_reading_frame):
                    longest_reading_frame = orf
                    longest_identifier = current_identifier

    return longest_identifier, longest_reading_frame
    

print(reading_frame('dna.example.fasta'))