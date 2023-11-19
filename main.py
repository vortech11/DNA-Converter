string = ""
DNA = ""
DNA_list = []
mRNA_list = []
Amino_acid_list = []
mRNA = []
Amino_acid = []
DNA_mutation_string = []
DNA_mutation_point = []
mRNA_mutation_string = []
mRNA_mutation_point = []
Amino_acid_mutation_string = []
Amino_acid_mutation_point = []
  
def string_to_DNA(string):
  DNA = ""
  for x in range(len(string)):
    if string[x] == "A":
      DNA += "A"
    elif string[x] == "T":
      DNA += "T"
    elif string[x] == "C":
      DNA += "C"
    elif string[x] == "G":
      DNA += "G"
  return DNA

def DNA_to_mRNA(DNA):
  mRNA = []
  for x in range(len(DNA)):
    if DNA[x] == "A":
      mRNA.append("U")
    elif DNA[x] == "T":
      mRNA.append("A")
    elif DNA[x] == "G":
      mRNA.append("C")
    elif DNA[x] == "C":
      mRNA.append("G")
  return mRNA

def mRNA_to_Amino_acid(mRNA):
  Amino_acid = []
  for x in range(0, (len(mRNA) - (len(mRNA) % 3)), 3):
    if mRNA[x] == "A":
      if mRNA[x + 1] == "A":
        if mRNA[x + 2] == "A" or mRNA[x + 2] == "G":
          Amino_acid.append("Lys")
        else:
          Amino_acid.append("Asn")
      elif mRNA[x + 1] == "U":
        if mRNA[x + 2] == "G":
          Amino_acid.append("Met")
        else:
          Amino_acid.append("Ile")
      elif mRNA[x + 1] == "C":
        Amino_acid.append("Thr")
      elif mRNA[x + 1] == "G":
        if mRNA[x + 2] == "G" or mRNA[x + 2] == "A":
          Amino_acid.append("Arg")
        else:
          Amino_acid.append("Ser")
    elif mRNA[x] == "U":
      if mRNA[x + 1] == "A":
        if mRNA[x + 2] == "A" or mRNA[x + 2] == "G":
          Amino_acid.append("Stop")
        else:
          Amino_acid.append("Tyr")
      elif mRNA[x + 1] == "U":
        if mRNA[x + 2] == "A" or mRNA[x + 2] == "G":
          Amino_acid.append("Leu")
        else:
          Amino_acid.append("Phe")
      elif mRNA[x + 1] == "C":
        Amino_acid.append("Ser")
      elif mRNA[x + 1] == "G":
        if mRNA[x + 2] == "A":
          Amino_acid.append("Stop")
        elif mRNA[x + 2] == "U" or mRNA[x + 2] == "C":
          Amino_acid.append("Cys")
        else:
          Amino_acid.append("Trp")
    elif mRNA[x] == "C":
      if mRNA[x + 1] == "A":
        if mRNA[x + 2] == "A" or mRNA[x + 2] == "G":
          Amino_acid.append("Gln")
        else:
          Amino_acid.append("His")
      elif mRNA[x + 1] == "U":
        Amino_acid.append("Leu")
      elif mRNA[x + 1] == "C":
        Amino_acid.append("Pro")
      elif mRNA[x + 1] == "G":
        Amino_acid.append("Arg")
    elif mRNA[x] == "G":
      if mRNA[x + 1] == "A":
        if mRNA[x + 2] == "A" or mRNA[x + 2] == "G":
          Amino_acid.append("Glu")
        else:
          Amino_acid.append("Asp")
      elif mRNA[x + 1] == "U":
        Amino_acid.append("Val")
      elif mRNA[x + 1] == "C":
        Amino_acid.append("Ala")
      elif mRNA[x + 1] == "G":
        Amino_acid.append("Gly")
  return Amino_acid
  
def print_mRNA_sequence(mRNA):
  print("mRNA: ", end="")
  for x in range(len(mRNA)):
    print(mRNA[x], sep="", end="")
    if x % 3 == 2 and x + 1 != len(mRNA):
      print("-", end="")

def print_Amino_acid_sequence(Amino_acid):
  print("\n", "Amino acid: ", sep="", end="")
  for x in range(len(Amino_acid)):
    print(Amino_acid[x], sep="", end="")
    if x + 1 != len(Amino_acid):
      print("-", end="")

  print("\n", "\n")

def RESET_VARIABLES():
  global DNA
  global DNA_list
  global mRNA
  global mRNA_list
  global Amino_acid
  global Amino_acid_list
  
  DNA_list.append(DNA)
  DNA = ""
  mRNA_list.append(mRNA)
  mRNA = ""
  Amino_acid_list.append(Amino_acid)
  Amino_acid = ""

def DNA_Mutation_Finder(Mutated, list):
  Mutated_strand = set(Mutated)
  Original_strand = set(list[0])

  dif = Original_strand.difference(Mutated_strand)
  return dif
  
string = str(input("DNA: "))
DNA = string_to_DNA(string)
mRNA = DNA_to_mRNA(DNA)
Amino_acid = mRNA_to_Amino_acid(mRNA)
print_mRNA_sequence(mRNA)
print_Amino_acid_sequence(Amino_acid)

RESET_VARIABLES()

string = str(input("DNA: "))
DNA = string_to_DNA(string)
print(DNA_Mutation_Finder(DNA, DNA_list))
mRNA = DNA_to_mRNA(DNA)
    
print_mRNA_sequence(mRNA)
print_Amino_acid_sequence(Amino_acid)
print(DNA_mutation_string, mRNA_mutation_string, Amino_acid_mutation_string)