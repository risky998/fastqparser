"""
This Parser Functions in a very similar way to the first one, but instead produces and prints the sorted lines by reverse complement. 

"""

file = open("/home/local/CORNELL/public/hw1_files/Sample_Alignment.fastq", "r")

lines = file.readlines()
dna_lines = []

for line in lines: 
    line=line.strip("\n")
    
    num_a = line.count('A')
    num_c = line.count('C')
    num_g = line.count('G')
    num_t = line.count('T')
    
    if (num_a + num_c + num_g + num_t) == len(line):
        dna_lines.append(line)
    

final_list = []

for seq in dna_lines: 
    reverse = ''
    i = len(seq)-1
    while(i>=0):
        if seq[i] == 'A':
            reverse+='T'
            i -=1
        elif seq[i] == 'T':
            reverse += 'A'
            i-=1
        elif seq[i] == 'C':
            reverse += 'G'
            i-=1
        elif seq[i] == 'G':
            reverse += 'C'
            i-=1
    cgcontent = (reverse.count('C')+reverse.count('G'))/((reverse.count('A'))+reverse.count('T')+reverse.count('G')+reverse.count('C'))
    seq = str((round(cgcontent,3))) + "\t" + reverse
    final_list.append(seq)
    
for line in sorted(final_list, reverse = True):
    print (line)
