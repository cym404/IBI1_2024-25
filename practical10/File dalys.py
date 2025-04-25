import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
dalys_data = pd.read_csv(r'C:\Users\lenovo\Desktop\新建文件夹\IBI1_2024-25\practical10\dalys-rate-from-all-causes.csv')
os.chdir(r"C:\Users\lenovo\Desktop\新建文件夹\IBI1_2024-25\practical10")
first_10_years=dalys_data.iloc[:10,2]
print(first_10_years)
afghenistan_data=dalys_data[dalys_data["Entity"]=="Afghanistan"]
afghenistan_first_10_years=afghenistan_data.iloc[:10,2]
tenth_year=afghenistan_first_10_years.iloc[9]
print(tenth_year)

dalys_1990=dalys_data[dalys_data["Year"]==1990]
print(dalys_1990.head())

uk = dalys_data.loc[dalys_data["Entity"]=="United Kingdom", ["DALYs", "Year"]]
france = dalys_data.loc[dalys_data["Entity"]=="France", ["DALYs", "Year"]]
uk_mean=uk["DALYs"].mean()
france_mean=france["DALYs"].mean()
if uk_mean>france_mean:
    print("uk is bigger")
else:
    print("france is bigger")

plt.figure(figsize=(10, 6))
plt.plot(uk["Year"], uk["DALYs"], 'b+', label="United Kingdom DALYs")
plt.title("UK DALYs Over Time")
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.xticks(uk["Year"], rotation=-90)  
plt.legend()
plt.grid(True)
plt.show()

china_data = dalys_data[dalys_data["Entity"] == "China"][["DALYs", "Year"]]
plt.figure(figsize=(10, 6))
plt.plot(uk["Year"], uk["DALYs"], 'b-', label="UK")
plt.plot(china_data["Year"], china_data["DALYs"], 'r-', label="China")
plt.title("DALYs Comparison: China vs UK")
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.xticks(rotation=-90)
plt.legend()
plt.grid(True)
plt.show()
