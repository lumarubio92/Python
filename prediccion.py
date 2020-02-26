#%% [markdown]
# # Análisis de Hongos (Comestibles y Venenosos)
# 
# Alan Badillo Salas (badillo.soft@hotmail.com)
# 
# Dado el dataset `agaricus` extraído de https://archive.ics.uci.edu/ml/datasets/Mushroom en específico de https://archive.ics.uci.edu/ml/machine-learning-databases/mushroom/agaricus-lepiota.data vamos a construir un predictor de Venenosidad o Comestibilidad de las 8124 muestras de hongos codificadas en 22 caracterísiticas.
# 
# 1. (CapShape) cap-shape: bell=b,conical=c,convex=x,flat=f, knobbed=k,sunken=s 
# 2. (CapSurface) cap-surface: fibrous=f,grooves=g,scaly=y,smooth=s 
# 3. (CapColor) cap-color: brown=n,buff=b,cinnamon=c,gray=g,green=r, pink=p,purple=u,red=e,white=w,yellow=y 
# 4. (Bruises) bruises?: bruises=t,no=f 
# 5. (Odor) odor: almond=a,anise=l,creosote=c,fishy=y,foul=f, musty=m,none=n,pungent=p,spicy=s 
# 6. (GillAttachment) gill-attachment: attached=a,descending=d,free=f,notched=n 
# 7. (GillSpacing) gill-spacing: close=c,crowded=w,distant=d 
# 8. (GillSize) gill-size: broad=b,narrow=n 
# 9. (GillColor) gill-color: black=k,brown=n,buff=b,chocolate=h,gray=g, green=r,orange=o,pink=p,purple=u,red=e, white=w,yellow=y 
# 10. (StalkShape) stalk-shape: enlarging=e,tapering=t 
# 11. (StalkRoot) stalk-root: bulbous=b,club=c,cup=u,equal=e, rhizomorphs=z,rooted=r,missing=? 
# 12. (StalkSurfaceARing) stalk-surface-above-ring: fibrous=f,scaly=y,silky=k,smooth=s 
# 13. (StalkSurfaceBRing) stalk-surface-below-ring: fibrous=f,scaly=y,silky=k,smooth=s 
# 14. (StalkColorARing) stalk-color-above-ring: brown=n,buff=b,cinnamon=c,gray=g,orange=o, pink=p,red=e,white=w,yellow=y 
# 15. (StalkColorBRing) stalk-color-below-ring: brown=n,buff=b,cinnamon=c,gray=g,orange=o, pink=p,red=e,white=w,yellow=y 
# 16. (VeilType) veil-type: partial=p,universal=u 
# 17. (VeilColor) veil-color: brown=n,orange=o,white=w,yellow=y 
# 18. (RingNumber) ring-number: none=n,one=o,two=t 
# 19. (RingType) ring-type: cobwebby=c,evanescent=e,flaring=f,large=l, none=n,pendant=p,sheathing=s,zone=z 
# 20. (SporePrintColor) spore-print-color: black=k,brown=n,buff=b,chocolate=h,green=r, orange=o,purple=u,white=w,yellow=y 
# 21. (Population) population: abundant=a,clustered=c,numerous=n, scattered=s,several=v,solitary=y 
# 22. (Habitat) habitat: grasses=g,leaves=l,meadows=m,paths=p, urban=u,waste=w,woods=d
#%% [markdown]
# 1. Adquirimos los datos mediante `read_csv` de pandas

#%%
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

# url = "https://archive.ics.uci.edu/ml/machine-learning-databases/mushroom/agaricus-lepiota.data"

url = "agaricus-lepiota.data"

data = pd.read_csv(url, header=None, names=columns)

data.sample(5)

#%% [markdown]
# P_1) odor=NOT(almond.OR.anise.OR.none)
#              120 poisonous cases missed, 98.52% accuracy
# 
# P_2) spore-print-color=green
#      48 cases missed, 99.41% accuracy
# 
# P_3) odor=none.AND.stalk-surface-below-ring=scaly.AND.
#           (stalk-color-above-ring=NOT.brown) 
#      8 cases missed, 99.90% accuracy
# 
# P_4) habitat=leaves.AND.cap-color=white
#          100% accuracy 
#%% [markdown]
# 2. Recodificar las columnas a tipos numéricos
# 
# Comenzando por `CapColor`:
#     
# (CapColor) cap-color: brown=n,buff=b,cinnamon=c,gray=g,green=r, pink=p,purple=u,red=e,white=w,yellow=y 
# 
# * n -> 1
# * b -> 2
# * c -> 3
# * g -> 4
# * r -> 5
# * p -> 6
# * u -> 7
# * e -> 8
# * w -> 9
# * y -> 10

#%%
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

#%% [markdown]
# (Odor) odor: almond=a,anise=l,creosote=c,fishy=y,foul=f,musty=m,none=n,pungent=p,spicy=s
#     
# * a -> 1
# * l -> 2
# * c -> 3
# * y -> 4
# * f -> 5
# * m -> 6
# * n -> 7
# * p -> 8
# * s -> 9

#%%
data["Odor-Cat"] = data["Odor"].map({
    "a": 1,
    "l": 2,
    "c": 3,
    "y": 4,
    "f": 5,
    "m": 6,
    "n": 7,
    "p": 8,
    "s": 9
})

data.sample(5)

#%% [markdown]
# Tarea: Hacer el mapeo a categorías como en `CapColor`, para las columnas `Odor`, `SporePrintColor`, `StalkSurfaceARing`, `StalkSurfaceBRing`, `Habitat`, `Population`, `Edibility`
#%% [markdown]
# Tarea: Extraer del dataframe de pandas `data` el sub-dataframe con sólo las columnas categóricas que serán usadas para el aprendizaje (`CapColor-Cat`, ... `Population-Cat`, i.e, todas excepto `Edibility-Cat`). Y extraer el vector que sólo contenga `Edibility-Cat`.
# 
# A la primer matriz le llamaremos `X_train` y al segundo vector le llamaremos `Y_train`.
#%% [markdown]
# Tarea: Revisar el tema de `SVM` de sklearn desde https://scikit-learn.org/stable/modules/svm.html y hacer un clasificador que se entrene a partir de `X_train` y `Y_train` para predecir la comestibilidad de los hongos. (Opcional) Medir el grado de exactitud de la clasifición.

#%%


