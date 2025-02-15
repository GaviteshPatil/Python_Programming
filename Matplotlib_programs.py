"Matplotlib is a widely-used library in python for creating static, interactive, and animated visualizations.It's especially popular in data science and research fieds , as it offers a way to create a variety of plots and charts. "
import matplotlib.pyplot as plt
import numpy as np
#Program to create the Basic plots
"Line plots are ideal for showing trends over time or ordered categories."
#Sample data
x=np.array([1,2,3,4,5])
y=np.array([1,4,9,16,25])

plt.plot(x,y)   #Create a line plot
plt.xlabel('X-axis')  #Label X-axis
plt.ylabel("Y-axis")   #Label Y-axis
plt.title("Simple Line Plot")  #Title of the plot

plt.show() #Display the plot

#program to demostrate the Scatter Plot 
"Scatter plots are useful for showing relationships between two sets of data."
plt.scatter(x,y)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Scatter Plot Example")
plt.show()

#Program to demostrate the bar chart 
"Bar charts are suitabel for comparing different categories"
categories=np.array(["A","B","C","D"])
values=np.array([4,7,1,8])

plt.bar(categories,values)
plt.xlabel("Categories")
plt.ylabel("Vaues")
plt.title("Bar Chart Example")
plt.show()

#Programs to demostrate the Histogram
data = np.random.randn(1000)  #Generate random data
plt.hist(data,bins=30)   #Plot histogram with 30 bins
"In the context of histograms in Matplotlib ,'bins' refer to interevals or 'buckets' that divide the range of data into smaller segements."

plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("histogram with 10 Bins")
plt.show()
#bins controls the number of bars.

"Intermediate Plot customizations"
#Adding Legends
'Legends help differentiate multiple data series in one plot.'
plt.plot(x,y,label="Line")
plt.scatter(x,y,color="red",label="Points")
plt.legend() #Display the legend
plt.show()

#Subplots
"syntax :- plt.subplot() allows you to create multiple plots in a single figure."
plt.subplot(1,2,1)  #1 row ,2 columns , 1st plot
plt.plot(x,y)
plt.title("Plot 1")

plt.subplot(1,2,2)  # 1 row,2 columns, 2st plot
plt.bar(categories,values)
plt.title("plot 2")
plt.show()

#Styling Plots
"Matplotlib offers various styling options to customize the look and feel of plots."
plt.plot(x,y,color="green",linestyle="--",linewidth=2,marker="o")
plt.title("Styled LIne Plot")
plt.show()

"""
# color :- sets the color.
# linestyle :- allows you to use dashed (-- ),dotted (:),etc.
# linewidht :- controls the thickness of the line.
# marker :- adds markers for each data point."""


#Adding Grids
"Grids can enhance readability,especially for data-heavy plots."
plt.plot(x,y)
plt.grid(True) #Enable grid lines
plt.show()

#Saving Plots
# "You can save plots as image files instead of displaying them."
# plt.plot(x,y)
# plt.savefig("line_plot.png ") #Saves the plot as a png.file
# plt.show()

#Box Plot
"Box plots show the distribution and outliers of a dataset."
data = [np.random.normal(0,std,100) for std in range(1,4)]
plt.boxplot(data)
plt.xlabel("Dataset")
plt.ylabel("Value")
plt.title("Box Plot Example")
plt.show()

#Pie Chart
"Pie charts display proportions within a whole"
labels=["A","B","C","D"]
sizes=[15,30,45,10]

plt.pie(sizes,labels=labels,autopct="%1.1f%%")
plt.title("Pie Chart Example")
plt.show()

#Advanced Customizations with fig and ax Objects 
"Using fig and ax objects allows finer control over plots,especially when creating multiple subplots or sharing axes."
fig,ax=plt.subplots()
ax.plot(x,y)
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_title("Advanced Plot with ax Object")
plt.show()
