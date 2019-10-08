
def parser(file):

    lines = file.readlines()
    dna_lines = []

    for line in lines:
        line=line.strip("\n")

        num_a = line.count('A')
        num_c = line.count('C')
        num_g = line.count('G')
        num_t = line.count('T')

        if (num_a + num_c + num_g + num_t) == len(line): #ensures that the line only contains known DNA sequences, with no unknown DNA included
            dna_lines.append(line)


    final_list = []

    for seq in dna_lines:
        cgcontent = (seq.count('C')+seq.count('G'))/((seq.count('A'))+seq.count('T')+seq.count('G')+seq.count('C'))
        reverse = []
        i = len(seq)-1
        while(i>=0):
            reverse.append(seq[i])
            i-=1
        seq = (str(round(cgcontent, 3)) + "\t").join(reverse)
        final_list.append(seq)

    for line in sorted(final_list, reverse = True):
        print (line)

def main():
    parser = argparse.ArgumentParser(
    description='Calculate sequence alignments for two sequences with a linear gap penalty.')
    parser.add_argument('-f', action="store", dest="f", type=str, required=True)

    args = parser.parse_args()
    file = args.f
    parser(file)

if __name__ == "__main__":
    main()
