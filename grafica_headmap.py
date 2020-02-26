import seaborn as sns; sns.set()

mat = [
    #X  Y  Z  W
    [1, 2, 3, 4], # A
    [5, 6, 7, 8], # B
    [2, 1, 0, 9], # C
]

sns.heatmap(mat)