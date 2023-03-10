from modeller import *
from modeller.automodel import *


env = Environ()
a = AutoModel(env, alnfile='E7CRL0_6ksi.ali',
              knowns='6ksi', sequence='E7CRL0',
              assess_methods=(assess.DOPE,
                              assess.GA341))
a.starting_model = 1
a.ending_model = 5
a.make()
