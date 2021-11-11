import matplotlib.pyplot as plt
import pandas as pd
import openpyxl as xl


data=pd.read_excel(r'C:\Users\GB_2_Test\OneDrive - Stacked\Desktop\Price rank.xlsx')
x=data['Vow October Net']
y=data['Spicers Net']
plt.plot(x,y)
plt.xlabel('Vow Pricing')
plt.ylabel('Spicers Pricing')
plt.title('Demo Plot')
plt.show()