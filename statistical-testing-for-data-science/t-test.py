import pandas as pd
from scipy.stats import ttest_lsamp

solar_data = pd.read_csv('data/solar_cell_efficiencies.csv')
ttest_lsamp(solar_data['efficiency'], 14, alternative='two-sided')