import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv('company_sales_data.csv')
data['moisturizer'] = data['moisturizer'] * 3.5
fig = plt.figure()
axes = fig.add_axes([0.15,0.1,.8,.8 ])
axes.set_xlabel('Month Number')
axes.set_ylim([0,500000])
axes.set_title('Company Profit Per Month')
axes.set_ylabel('Toal Profit')
axes.plot(data['month_number'],data['total_profit'],ls='--',color='red',marker='o',
                markerfacecolor='red',markeredgewidth=2,markeredgecolor='black',label='Profit Per Month',lw=3)
axes.legend(loc='lower right')

fig_2 = plt.figure()
axes_2 = fig_2.add_axes([.14,.1,.8,.8])
axes_2.set_xlabel('Month Number')
axes_2.set_ylabel('Sales')
axes_2.set_title('Sales Data')
axes_2.plot(data['month_number'],data['facewash'],color='orange',marker='o',label='Face Wash')
axes_2.plot(data['month_number'],data['facecream'],color='red',marker='o',label='Face Cream')
axes_2.plot(data['month_number'],data['toothpaste'],color='yellow',marker='o',label='Toothpaste')
axes_2.plot(data['month_number'],data['bathingsoap'],color='green',marker='o',label='Bathing Soap')
axes_2.plot(data['month_number'],data['shampoo'],color='blue',marker='o',label='Shampoo')
axes_2.plot(data['month_number'],data['moisturizer'],color='black',marker='o',label='Moisturizer')
axes_2.legend(loc='upper left')
plt.xticks(range(1,13,1))

fig_3 = plt.scatter(data['month_number'],data['toothpaste'])
#axes_3 = fig_3.add_axes([.14,.1,.8,.8])
#axes_3.set_xlabel('Month Number')
#axes_3.set_ylabel('Toothpaste Units Sold')
#axes_3.plot(data['month_number'],data['toothpaste'])



print(data.head())
plt.show(block=True)