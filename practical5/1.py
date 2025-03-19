#(1. Create and print a dictionary
#DECLARE language_percentage AS DICTIONARY
#language_percentage["JavaScript"] = 62.3
#language_percentage["HTML"] = 52.9
#language_percentage["Python"] = 51
#language_percentage["SQL"] = 46
#language_percentage["TypeScript"] = 38.5
#PRINT language_percentage
#2. Construct a bar plot
#// Assume we have a function to create bar plot, like createBarPlot(x_data, y_data)
#DECLARE languages AS ARRAY = ["JavaScript", "HTML", "Python", "SQL", "TypeScript"]
#DECLARE percentages AS ARRAY = [62.3, 52.9, 51, 46, 38.5]
#CALL createBarPlot(languages, percentages)
#3. Get the percentage of a specified language
#DECLARE input_language AS STRING // Assume it's assigned a value, e.g., "Python"
#DECLARE percentage AS FLOAT
#SET percentage = language_percentage[input_language] IF input_language IN language_percentage ELSE "Language not found"
#PRINT percentage）


language_percentage={"javaScript":62.3,"HTML":52.9,"Python":51,"SQL":46,"TypeScript":38.5}
import matplotlib.pyplot as plt
languages=list(language_percentage.keys())
percentages=list(language_percentage.values())
plt.bar(languages,percentages)
plt.xlabel("Programming Languages")
plt.ylabel("Precentage of Users")
plt.title("popularity of top 5 programming languages")
plt.show()
input_language=input(str("PLEASE INPUT A PROGRAMMING LANGUAGE"))#input Python as the selected language
percentage=language_percentage.get(input_language)
print("THE PRECENTAGE of",input_language,"is",percentage)