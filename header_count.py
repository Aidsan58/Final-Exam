# f = open('D:/Programs/Python Programs/Python for Genomics/dna.example.fasta')

def header_count(filename):
    """ Finds the number of headers in a sequence. """
    count = 0
    with open(filename, 'r') as f :
        for line in f :
            if line.startswith('>') :
                count += 1
    
    return count

file_path = 'D:/Programs/Python Programs/Python for Genomics/Final Exam/dna.example.fasta'

count = header_count(file_path) # Retrieves header count
print(f'The total number of headers in the file is {count}.')
