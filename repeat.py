def repeat(filename, n):
    def find_repeats(seq, n):
        seen = set()
        repeats = set()
        
        for i in range(len(seq) - n + 1): # Two sets are created, one called seen which has all substrings of a certain length, and one called repeats which contains all repeats of length n.
            substring = seq[i:i+n]
            if substring in seen:
                repeats.add(substring)
            else:
                seen.add(substring)

        return repeats



    with open(filename, 'r') as f:
        current_sequence = ''
        num_repeats = 0
        for line in f:
            if line.startswith('>'):
                if current_sequence:
                    repeats = find_repeats(current_sequence.upper(), n)
                    num_repeats += len(repeats)
                    current_sequence = ''
            else:
                current_sequence += line.strip() # Goes to the next sequence once the previous one has been read through.

        if current_sequence: # This part of the code checks the last sequence for repeats.
            repeats = find_repeats(current_sequence.upper(), n)
            num_repeats += len(repeats)
                
    return num_repeats

repeat_length = int(input())
print(repeat('dna.example.fasta', repeat_length))

