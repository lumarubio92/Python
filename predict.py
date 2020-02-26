# # Análisis de Hongos (Comestibles y Venenosos)
import pandas as pd

columns = [
    "Edibility",
    "CapShape",
    "CapSurface",
    "CapColor",
    "Bruises",
    "Odor",
    "GillAttachment",
    "GillSpacing",
    "GillSize",
    "GillColor",
    "StalkShape",
    "StalkRoot",
    "StalkSurfaceARing",
    "StalkSurfaceBRing",
    "StalkColorARing",
    "StalkColorBRing",
    "VeilType",
    "VeilColor",
    "RingNumber",
    "RingType",
    "SporePrintColor",
    "Population",
    "Habitat"

]

#url = "https://archive.ics.uci.edu/ml/machine-learning-databases/mushroom/agaricus-lepiota.data"

url = "agaricus-lepiota.data"

data = pd.read_csv(url, header=None, names=columns)

data["CapColor-Cat"] = data["CapColor"].map({
    "n": 1,
    "b": 2,
    "c": 3,
    "g": 4,
    "r": 5,
    "p": 6,
    "u": 7,
    "e": 8,
    "w": 9,
    "y": 10
})

data.sample(5)
