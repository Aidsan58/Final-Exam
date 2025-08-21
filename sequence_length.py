def sequence_length(filename):
    """ Finds the longest DNA sequence, and the shortest DNA sequence. """
    current_sequence = ''
    longest_sequence = 0
    shortest_sequence = float('inf') # Chose to use inf instead of an arbitrary value
    with open(filename, 'r') as f:
        for line in f:
            if line.startswith('>'):
                if len(current_sequence) > longest_sequence:
                    longest_sequence = len(current_sequence)
                if len(current_sequence) > 0:
                    if len(current_sequence) < shortest_sequence:
                        shortest_sequence = len(current_sequence)
                current_sequence = ''
            else:
                current_sequence += line.strip()

        if len(current_sequence) > longest_sequence:
            longest_sequence = len(current_sequence)
            
        if len(current_sequence) < shortest_sequence:
            shortest_sequence = len(current_sequence)
            

        
    return longest_sequence, shortest_sequence


file_path = 'D:/Programs/Python Programs/Python for Genomics/Final Exam/dna.example.fasta'

# Retrieves and prints the shortest and longest sequence lengths
longest_sequence, shortest_sequence = sequence_length(file_path)
print(f'The longest sequence has a length of {longest_sequence}. The shortest sequence has a length of {shortest_sequence}.')
