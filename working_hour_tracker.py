import csv
from csv import writer
import datetime
import webbrowser
import os
import sys
import numpy as np; np.random.seed(sum(map(ord, 'calmap')))
import pandas as pd
import calmap
from matplotlib import pyplot as plt




def update_date(argv):
	print(argv)
	if len(argv)==4:
		year = argv[0]
		month = argv[1]
		day = argv[2]
		hrs = argv[3]
	else:
		d = datetime.datetime.today()
		year = d.year
		month = d.month
		day = d.day
		if len(argv) > 0:
			hrs = argv[0]
		else:
			hrs = '0'
	# the date is in the format of: y, m, d, hrs
	file_name = os.getcwd()+'/data.txt'
	data = np.loadtxt(file_name,dtype=str,delimiter=',')
	if hrs!='0':
		date = str(year)+"-"+str(month)+"-"+str(day)
		new = 2
		# print (d.year, d.month, d.day)


		
		# if os.path.getsize(file_name) > 0:
		# 	df=pd.read_csv(file_name, sep=',',header=None)
		# 	data = df.values
		# else: 
			# data = []

		flag = True
		for i in range(len(data)):
			if date==data[i,0]:
				data[i,1]  = float(hrs) + float(data[i,1])
				print(data[i,1])
				flag = False
				break
		if flag:
			data = np.vstack((data,[date,hrs]))
		np.savetxt(file_name,data,delimiter=',',fmt="%s")


	# show the visualization
	# url = "file://" + os.getcwd()+"/working_hour_visualization.html"
	# webbrowser.open(url,new=new)

	# days = (d - datetime.datetime(2020,4,13)).days
	days = data.shape[0]

	# all_days = pd.date_range('4/13/2020', periods=days, freq='D')
	# days = np.random.choice(all_days, 500)
	events = pd.Series([float(i) for i in data[:,1]], index=pd.to_datetime(data[:,0]))
	print(events)
	fig,ax = calmap.calendarplot(events, monthticks=1, daylabels='MTWTFSS',
                    dayticks=[0, 1, 2, 3, 4, 5, 6], cmap='YlGn',
                    fillcolor='silver', linewidth=0.5,
                    fig_kws=dict(figsize=(10,4)))
	# calmap.yearplot(events, year=2020)
	fig.colorbar(ax[0].get_children()[1], ax=ax.ravel().tolist(),orientation='horizontal')
	fig.suptitle('Irony of a sleeper',fontsize=40)
	fig.savefig('tracking.png')
	# plt.show()

if __name__ == '__main__':
	update_date(sys.argv[1:])			
	
