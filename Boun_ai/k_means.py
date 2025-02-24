import pandas as pd
import numpy as np
mall_customers = pd.read_csv("Mall_Customers.csv")
print(mall_customers.columns)
print(mall_customers.loc[:, "Genre"])