from modeller import *

env = Environ()
aln = Alignment(env)

mdl = Model(env, file='6ksi', model_segment=('FIRST:A','LAST:A'))
aln.append_model(mdl, align_codes='6ksi', atom_files='6ksi.pdb')
aln.append(file='E7CRL0.ALI', align_codes='E7CRL0')
aln.align2d(max_gap_length=50)
aln.write(file='E7CRL0_6ksi.ali', alignment_format='PIR')
aln.write(file='E7CRL0_6ksi.pap', alignment_format='PAP')
