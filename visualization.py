import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# https://sashamaps.net/docs/resources/20-colors/
colors = [
    "#e6194b",
    "#3cb44b",
    "#ffe119",
    "#4363d8",
    "#f58231",
    "#911eb4",
    "#46f0f0",
    "#f032e6",
    "#bcf60c",
    "#fabebe",
    "#008080",
    "#e6beff",
    "#9a6324",
    "#fffac8",
    "#800000",
    "#aaffc3",
    "#808000",
    "#ffd8b1",
    "#000075",
    "#808080",
    "#ffffff",
    "#000000",
]

plt.rcParams["font.family"] = "Arial"
plt.rcParams["pdf.fonttype"] = 42
cmap = mcolors.ListedColormap(colors)

sns.set_style("whitegrid")
sns.set_palette(sns.color_palette(colors))
