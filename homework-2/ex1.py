
with open('PF00061-seed.fasta', 'r') as f:
    sequences = [seq for seq in f.read().split('>') if seq]
    lines = [seq.split('\n') for seq in sequences]

    seq_dict = {line[0]: line[1:4] for line in lines}

    f.close( )