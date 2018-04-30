#! /usr/bin/env python3

import csv
from collections import Counter
import sys


fname = sys.argv[1]

best_taxa= []
lca_taxa = []



with open(fname,'r') as f:
    csv_reader = csv.reader(f, delimiter='\t')
    next(csv_reader) # in phyloassigner 6.166 there is a header line in the tab file. this skips it
    for line in csv_reader:
        best_taxa.append(line[2])
        lca_taxa.append(line[5])
    
count_best_dic = dict(Counter(best_taxa))
count_lca_dic = dict(Counter(lca_taxa))

write_fname = fname + '.counts'

with open(write_fname,'w+') as fout:
    fout.write('Best placements ({} total):\n'.format(len(best_taxa)))
    for k in sorted(count_best_dic.keys()):
        fout.write('{}\t{}\n'.format(k,count_best_dic[k]))
    fout.write('\n')
    fout.write('LCA placements ({} total):\n'.format(len(lca_taxa)))
    for k in sorted(count_lca_dic.keys()):
        fout.write('{}\t{}\n'.format(k,count_lca_dic[k]))

