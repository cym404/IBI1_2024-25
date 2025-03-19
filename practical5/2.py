#1. Sort and print the population lists
#// Population of UK's constituent countries
#DECLARE uk_population AS ARRAY = [57.11, 3.13, 1.91, 5.45]
#SORT uk_population IN ASCENDING ORDER
#PRINT "UK's constituent countries sorted population list: ", uk_population

#// Population of provinces around Zhejiang Province
#DECLARE zj_neighbor_population AS ARRAY = [65.77, 41.88, 41.41, 61.27, 61.15]
#SORT zj_neighbor_population IN ASCENDING ORDER
#PRINT "Provinces around Zhejiang Province sorted population list: ", zj_neighbor_population
#2. Draw pie charts
#// Assume there is a function to draw pie charts, like drawPieChart(labels, data)

#// For the UK's constituent countries
#DECLARE uk_labels AS ARRAY = ["England", "Wales", "Northern Ireland", "Scotland"]
#DECLARE uk_population_data AS ARRAY = [57.11, 3.13, 1.91, 5.45]
#CALL drawPieChart(uk_labels, uk_population_data)
#PRINT "Population distribution pie chart of UK's constituent countries"

#// For provinces around Zhejiang Province
#DECLARE zj_labels AS ARRAY = ["Fujian", "Jiangxi", "Anhui", "Jiangsu"]
#DECLARE zj_neighbor_population_data AS ARRAY = [65.77, 41.88, 41.41, 61.27, 61.15]
#CALL drawPieChart(zj_labels, zj_neighbor_population_data)
#PRINT "Population distribution pie chart of provinces around Zhejiang Province"
uk_population=[57.11,3.13,1.91,5.45]
uk_population.sort()
zj_neighbor_population=[65.77,41.88,45.28,61.27,85.15]
zj_neighbor_population.sort()
print("	populations	of	countries	in	the	UK",uk_population)
print("population of Zhejiang-neighbouring	provinces	in	China",zj_neighbor_population)
import matplotlib.pyplot as plt
uk_labels=["England","Wales","Northern	Ireland","Scotland"]
uk_population=[57.11,3.13,1.91,5.45]
zj_labels=["Zhejiang","Fujian","Jiangxi","Anhui","Jiangsu"]
zj_neighbor_population=[65.77,41.88,45.28,61.27,85.15]
plt.figure(figsize=(6, 6))
plt.pie(uk_population, labels=uk_labels, autopct='%1.1f%%', colors=["r","g","b","y"])#make a pie map for uk population, and change the color of each country
plt.xlabel("countries in UK")
plt.ylabel("population")
plt.title('Population Distribution in UK Countries')
plt.show()
plt.figure(figsize=(6, 6))
plt.pie(zj_neighbor_population, labels=zj_labels, autopct='%1.1f%%', startangle=140)#make a pie map for Population Distribution in Zhejiang - Neighboring Provinces, and change the starting angle of the provinces
plt.xlabel("provinces around Zhejiang")
plt.ylabel("population")
plt.title('Population Distribution in Zhejiang - Neighboring Provinces')
plt.show()