#this is the compiler
import pandas as pd

print("hello world")

raw = pd.read_excel("ODR Report.xlsx",
                   skiprows=[1,2,3,4,5,6,7,8,9])

print(raw)
