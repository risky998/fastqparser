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
    cgcontent = (seq.count('C')+seq.count('G'))/((seq.count('A'))+seq.count('T')+seq.count('G')+seq.count('C'))
    reverse = ''
    i = len(seq)-1
    while(i>=0):
        reverse+=seq[i]
        i-=1
    seq = (str(round(cgcontent, 3)) + "\t" + reverse)
    final_list.append(seq)
    
for line in sorted(final_list, reverse = True):
    print (line)