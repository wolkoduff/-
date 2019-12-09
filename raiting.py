import pandas as pd
import numpy as np

df = pd.read_csv('group.tsv', sep='\t')
a = df.to_numpy()
df["Рейтинг"] = np.zeros(len(df))
df["Рейтинг20"] = np.zeros(len(df))
stepper = 0
for i in range(0, len(a) - 1, 1):
    for j in range(6, 18, 1):
        if a[i, j] == "+":
            stepper += 2
        elif a[i, j] == "-":
            stepper -= 1
        elif a[i, j] == "+-":
            stepper += 1
    b = a[i, 18].split(',')
    for c in b:
        if c == "+":
            stepper += 2.5
        elif c == "+-":
            stepper += 2
        elif c == "-+":
            stepper += 1
    df.loc[i, "Рейтинг"] = stepper
    if stepper >= 20:
        df.loc[i, "Рейтинг20"] = 20
    stepper = 0

df.to_csv('group_res.tsv', decimal=',', sep='\t')
