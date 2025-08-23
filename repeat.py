def repeat(filename, n):
    def find_repeats(seq, n):
        seen = set()
        repeats = set()
        
        for i in range(len(seq) - n + 1):
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
                current_sequence += line.strip()

        if current_sequence:
            repeats = find_repeats(current_sequence.upper(), n)
            num_repeats += len(repeats)
                
    return num_repeats

repeat_length = int(input())
print(repeat('dna.example.fasta', repeat_length))

