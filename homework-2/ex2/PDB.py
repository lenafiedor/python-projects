import re, sys

class PDBFile:

    def __init__(self, filename):
        self.data = self.read(filename)

    def read(self, filename):
        try:
            with open(filename, 'r') as f:
                self.data = f.read()
        except FileNotFoundError:
            print(f'File {filename} not found in current directory')
    
    def getSequence(self, chain='A'):
        pattern = re.compile('^SEQRES[ \d]+{}[ \d]+(.+)$'.format(chain),re.M)
        seq = pattern.findall(self.data)
        return ' '.join([s.strip() for s in seq]).split() or None

    def getAtoms(self, chain='A'):
        pattern = re.compile('^ATOM[\dA-Z ]{{17}}{}\s.*$'.format(chain), re.M)
        atoms = pattern.findall(self.data)
        return ' '.join([atom.split()[-1] for atom in atoms]).split() or None
    
    def saveToFastaFile(self, filename):
        fasta_filename = filename.split('.')[0] + '.fasta'
        with open(fasta_filename, 'w') as f:
            f.write(' '.join(self.getSequence()))

    def getNumChains(self):
        pattern = re.compile('^SEQRES\s+\d+\s+([A-Z])', re.M)
        return len(set(pattern.findall(self.data)))

    def getCompounds(self):
        pattern = re.compile('^HETNAM\s+[A-Z]+\s+(.*)$', re.M)
        names = [compound.strip() for compound in pattern.findall(self.data)]
        pattern = re.compile('^FORMUL\s+\d+\s+[\dA-Z]+\s+(.*)$', re.M)
        formulas = [formula.strip() for formula in pattern.findall(self.data)]
        return dict(zip(names, formulas))

    def displayProperties(self):
        print(f'Number of polypetide chains: {self.getNumChains()}')
        print(f'Number of atoms: {len(self.getAtoms())}')
        print(f'Number of aminoacids: {len(self.getSequence())}')
        print('Compounds:')
        compounds = self.getCompounds()
        for index, (name, formula) in enumerate(compounds.items(), start=1):
            print(f'{index:3}   name: {name:45} formula: {formula}')



if __name__ == '__main__':
    args = sys.argv
    if len(args) != 2:
        print('Usage: python3 PDB.py <filename.pdb>')
    else:
        filename = args[1]
        pfh = PDBFile(filename)
        pfh.read(filename)
        seq = pfh.getSequence()
        atoms = pfh.getAtoms()
        print(f'First 5 aminoacids: {seq[:5]}')
        print(f'First 5 atoms: {atoms[:5]}')
        pfh.saveToFastaFile(filename)
        pfh.displayProperties()
