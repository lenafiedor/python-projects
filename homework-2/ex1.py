import sys

def sequences_to_dict(file):
    sequences = [seq for seq in file.read().split('>') if seq]
    lines = [seq.split('\n') for seq in sequences]
    seq_dict = {line[0]: ''.join(line[1:4]) for line in lines}
    return seq_dict

def remove_hyphens(seq_dict):
    return {key: seq_dict[key].replace('-', '') for key in seq_dict}

def aa_composition(sequence):
    keys = ['A', 'R', 'N', 'D', 'B', 'C', 'Q', 'Z', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V']
    values = [sequence.count(key) * 100 / len(sequence) for key in keys]
    aminoacids = dict(zip(keys, values))
    for aa, value in aminoacids.items():
        print(f'Percent of {aa} : {value}')


if __name__ == "__main__":
        
    arguments = sys.argv[1:]
    file = open('PF00061-seed.fasta', 'r')

    if not arguments:
        seq_dict = sequences_to_dict(file)
        print(seq_dict['Q8QFM7_CHICK/35-178'])

    elif len(arguments) == 1:
        seq_dict = sequences_to_dict(file)
        if (arguments[0] == '-nh'):
            seq_dict = remove_hyphens(seq_dict)

    elif len(arguments) == 2:
        seq_dict = sequences_to_dict(file)
        if (arguments[0] == '-nh'):
            seq_dict = remove_hyphens(seq_dict)
            aa_composition(seq_dict[arguments[1]])
        else:
            new_dict = remove_hyphens(seq_dict)
            aa_composition(new_dict[arguments[1]])

    else:
        print('Usage: python3 ex1.py <-h (to display hyphens)/-nh (to hide hyphens)> <sequence_id> (optional)')   
    
    file.close()
