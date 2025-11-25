import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from tueplots import axes, bundles

from matplotlib.legend_handler import HandlerPatch
import matplotlib as mpl


pixel = 1/plt.rcParams['figure.dpi']

snp_cov = np.load('data/ancient_snp_coverage.npy')
print(np.min(snp_cov), np.max(snp_cov))

with plt.rc_context({**bundles.aistats2022(family="serif"), **axes.lines()}):
  f, ax = plt.subplots(1, 1, figsize=(488*pixel, 0.68*488*pixel))
  ax.hist(snp_cov, 50, color='gray', alpha=0.5)
  ax.set_xlabel(r'SNP coverage')
  plt.tight_layout()
  plt.savefig('paper_figures/figure_S01.pdf', dpi=150)