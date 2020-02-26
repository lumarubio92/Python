import seaborn as sns

temperaturas = [30, 31.2, 33.8, 45, 32.17, 29.6, 28.4, 30.1, 20.4]
ph = [5, 5.1, 5.4, 7, 5.3, 4.9, 3.2, 5.05, 2.9]

sns.set() # preajusta a seaborn (opcional)

sns.scatterplot(temperaturas, ph)