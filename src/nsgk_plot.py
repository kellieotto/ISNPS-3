import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

nsgk = pd.read_csv("https://raw.githubusercontent.com/statlab/nsgk/master/nsgk/results.csv")

nsgk_significant = nsgk.loc[nsgk['overall_pvalue'] <= 0.05]

sd_names = nsgk.columns[26:34]
novariance = nsgk[sd_names].sum(1)
nsgk_filter = nsgk.loc[novariance>0]

concordance_names = nsgk_filter.columns[10:18]
avg_concordance = nsgk_filter[concordance_names].mean(1)


fig = plt.scatter(avg_concordance, nsgk_filter['overall_pvalue'],
            color = "#629e1f", alpha = 0.6)
plt.axis([0.45, 1.05, -0.05, 1.05])
plt.xticks(size = 14, color = "#143264")
plt.yticks(size = 14, color = "#143264")
plt.xlabel("Average Concordance", size = 16, color = "#143264")
plt.ylabel("Overall P-value", size = 16, color = "#143264")
plt.title("Average Concordance Across 8 Videos vs P-value", color = "#143264")
#plt.show()

plt.savefig("../slides/fig/nsgk", format = 'png')