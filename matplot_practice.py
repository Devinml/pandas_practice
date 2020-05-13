import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv('company_sales_data.csv')

fig = plt.figure()
axes = fig.add_axes([0.15,0.1,.8,.8 ])
axes.set_xlabel('Month Number')
axes.set_ylim([0,500000])
axes.set_title('Company Profit Per Month')
axes.set_ylabel('Toal Profit')
axes.plot(data['month_number'],data['total_profit'],ls='--',color='red',marker='o',
                markerfacecolor='red',markeredgewidth=2,markeredgecolor='black',label='Profit Per Month',lw=3)
axes.legend(loc='lower right')


plt.show(block=True)