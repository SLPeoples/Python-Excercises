#Samuel L. Peoples
import matplotlib.pyplot as plt
import matplotlib.pylab as plb
import numpy as np
import datetime as dt
import pandas as pd
from mpl_toolkits.basemap import Basemap
import networkx as nx


#let's manipulate some pie charts
def pieCharts():
    #weighting the values
    values = [5, 8, 9, 10, 4, 7]
    #setting colors
    colors = ['b', 'g', 'r', 'c', 'm', 'y']
    labels = ['Entertainment', 'Eating Out', 'Bills', 'Utilities', 'Savings', 'Travel']
    explode = (0, 0.2, 0, 0, 0, 0)
    plt.pie(values, colors=colors, labels=labels,explode=explode, autopct='%1.1f%%',counterclock=False, shadow=True)
    plt.title('Expenses')
    plt.show()
    
#comparing bar charts
def barCharts():
    values = [5, 8, 9, 10, 4, 7]
    widths = [0.7, 0.8, 0.7, 0.7, 0.7, 0.7]
    #nice red one
    colors = ['b', 'r', 'b', 'b', 'b', 'b']
    plt.bar(range(0, 6), values, width=widths,color=colors, align='center')
    plt.show()

#lets power up some histograms
def histograms():
    x = 20 * np.random.randn(10000)
    #Step-filled
    plt.hist(x, 25, range=(-50, 50), histtype='stepfilled',align='mid', color='g', label='Test Data')
    plt.legend()
    plt.title('Step Filled Histogram')
    plt.show()

#boxplots
def boxplots():
    spread = 100 * np.random.rand(100)
    center = np.ones(50) * 50
    flier_high = 100 * np.random.rand(10) + 100
    flier_low = -100 * np.random.rand(10)
    data = np.concatenate((spread, center,flier_high, flier_low))
    plt.boxplot(data, sym='gx', widths=.75, notch=True)
    plt.show()

#scatterplots
def scatterplots():
    #simple scatter plot
    x1 = 5 * np.random.rand(40)
    x2 = 5 * np.random.rand(40) + 25
    x3 = 25 * np.random.rand(20)
    x = np.concatenate((x1, x2, x3))
    y1 = 5 * np.random.rand(40)
    y2 = 5 * np.random.rand(40) + 25
    y3 = 25 * np.random.rand(20)
    y = np.concatenate((y1, y2, y3))
    plt.scatter(x, y, s=[100], marker='^', c='m')
    #let's save that. make sure it's before the show() or else it'll be blank!
    plt.savefig('scatter1.png', format='png')
    plt.show()
    
    #more advanced scatterplots
    x1 = 5 * np.random.rand(50)
    x2 = 5 * np.random.rand(50) + 25
    x3 = 30 * np.random.rand(25)
    x = np.concatenate((x1, x2, x3))
    y1 = 5 * np.random.rand(50)
    y2 = 5 * np.random.rand(50) + 25
    y3 = 30 * np.random.rand(25)
    y = np.concatenate((y1, y2, y3))
    #Sets colors to each cluster of data
    #notice 1 is clustered between [0,5] on both the x and y
    #notice 2 is clustered between [0,30]
    #notice 3 is clustered between [25,30]
    color_array = ['b'] * 50 + ['g'] * 50 + ['r'] * 25
    plt.scatter(x, y, s=[50], marker='D', c=color_array)
    #let's save that. make sure it's before the show() or else it'll be blank!
    plt.savefig('scatter2.png', format='png')
    plt.show()

#correlations
def correlations():
    #Adding a trendline means calling the NumPy polyfit() function with the data, which returns a vector of coefficients, p, that minimizes the least squares error. 
    x1 = 15 * np.random.rand(50)
    x2 = 15 * np.random.rand(50) + 15
    x3 = 30 * np.random.rand(30)
    x = np.concatenate((x1, x2, x3))
    y1 = 15 * np.random.rand(50)
    y2 = 15 * np.random.rand(50) + 15
    y3 = 30 * np.random.rand(30)
    y = np.concatenate((y1, y2, y3))
    color_array = ['b'] * 50 + ['g'] * 50 + ['r'] * 25
    plt.scatter(x, y, s=[90], marker='*', c=color_array)
    #this creates the function for the trend line
    z = np.polyfit(x, y, 1)
    p = np.poly1d(z)
    #this draws the trend line
    plb.plot(x, p(x), 'm-.')
    #let's save that. make sure it's before the show() or else it'll be blank!
    plt.savefig('correlations.png', format='png')
    plt.show()

#working with time on axes    
def timeSeries():
    df = pd.DataFrame(columns=('Time', 'Sales'))
    #set start and end date
    start_date = dt.datetime(2015, 7,1)
    end_date = dt.datetime(2015, 7,10)
    daterange = pd.date_range(start_date, end_date)
    for single_date in daterange:
        row = dict(zip(['Time', 'Sales'],[single_date,int(50*np.random.rand(1))]))
        row_s = pd.Series(row)
        row_s.name = single_date.strftime('%b %d')
        df = df.append(row_s)
    #this defines the x axis date range
    df.ix['Jul 01':'Jul 07', ['Time', 'Sales']].plot()
    plt.ylim(0, 50)
    plt.xlabel('Sales Date')
    plt.ylabel('Sale Value')
    plt.title('Plotting Time')
    #let's save that. make sure it's before the show() or else it'll be blank!
    plt.savefig('timeSeries.png', format='png')
    plt.show()
    
#Plotting trends over time
def trends():
    df = pd.DataFrame(columns=('Time', 'Sales'))
    start_date = dt.datetime(2015, 7,1)
    end_date = dt.datetime(2015, 7,10)
    #daterange is the start and end date
    daterange = pd.date_range(start_date, end_date)
    for single_date in daterange:
        #choosing a random values
        row = dict(zip(['Time', 'Sales'],[single_date,int(50*np.random.rand(1))]))
        row_s = pd.Series(row)
        row_s.name = single_date.strftime('%b %d')
        #append it to the dataframe
        df = df.append(row_s)
    #x range
    df.ix['Jul 01':'Jul 10', ['Time', 'Sales']].plot()
    #plotting the trend line, similar to before
    z = np.polyfit(range(0, 10),df.as_matrix(['Sales']).flatten(), 1)
    p = np.poly1d(z)
    plb.plot(df.as_matrix(['Sales']),p(df.as_matrix(['Sales'])), 'm-')
    plt.ylim(0, 50)
    plt.xlabel('Sales Date')
    plt.ylabel('Sale Value')
    plt.title('Plotting Time')
    plt.legend(['Sales', 'Trend'])
    #let's save that. make sure it's before the show() or else it'll be blank!
    plt.savefig('trends.png', format='png')
    plt.show()
    #When you plot the initial data, the call to plot() automatically generates a
    #legend for you. MatPlotLib doesn't automatically add the trendline, so you
    #must also create a new legend for the plot.

#Geographical data
#if the basemap program isn't working well with python3
#conda install -c conda-forge basemap-data-hires=1.0.8.dev0

def geo():
    #coordinates of cities
    austin = (-97.75, 30.25)
    hawaii = (-157.8, 21.3)
    washington = (-77.01, 38.90)
    chicago = (-87.68, 41.83)
    losangeles = (-118.25, 34.05)
    #determines map longitude and latitude sizing
    m = Basemap(projection='merc',llcrnrlat=10,urcrnrlat=50,llcrnrlon=-160,urcrnrlon=-60)
    m.drawcoastlines()
    #colors the land and lakes
    m.fillcontinents(color='lightgray',lake_color='lightblue')
    #draws the parallels and meridian lines
    m.drawparallels(np.arange(-90.,91.,30.))
    m.drawmeridians(np.arange(-180.,181.,60.))
    #aqua colored ocean (note difference between lakes)
    m.drawmapboundary(fill_color='aqua')
    #draw the country borders
    m.drawcountries()
    x, y = m(*zip(*[hawaii, austin, washington,chicago, losangeles]))
    m.plot(x, y, marker='o', markersize=6,markerfacecolor='red', linewidth=0)
    plt.title("Mercator Projection")
    #let's save that. make sure it's before the show() or else it'll be blank!
    plt.savefig('geo.png', format='png')
    plt.show()
    
#undirected graphs
def undirected():
    G = nx.Graph()
    H = nx.Graph()
    #adds node 1
    G.add_node(1)
    #adds node 2 and 3
    G.add_nodes_from([2, 3])
    #adds nodes 3,5,6
    G.add_nodes_from(range(4, 7))
    #adds 7 to H (this is the only one present in H)
    H.add_node(7)
    #adds the nodes from H
    G.add_nodes_from(H)
    #edges from 1 to 2
    G.add_edge(1, 2)
    G.add_edge(1, 1)
    #adds edges from 2 to 3, 3 to 6, 4 to 6, 5 to 6
    G.add_edges_from([(2,3), (3,6), (4,6), (5,6)])
    H.add_edges_from([(4,7), (5,7), (6,7), (1,7)])
    #adds edges from H to G
    G.add_edges_from(H.edges())
    nx.draw_networkx(G)
    #let's save that. make sure it's before the show() or else it'll be blank!
    plt.savefig('undirected.png', format='png')
    plt.show()

#directed graphs
def directed():
    # NetworkX package also supportsMultiGraph() and MultiDiGraph() graph types. 
    #creates a digraph
    G = nx.DiGraph()
    #adds nodes
    G.add_node(1)
    G.add_nodes_from([2, 3])
    G.add_nodes_from(range(4, 6))
    #defines a path
    #The add_path() call lets you create nodes and edges at the same time
    G.add_path([6, 7, 8])
    G.add_edge(1, 2)
    G.add_edges_from([(1,4), (4,5), (2,3), (3,6), (5,6)])
    #sets colors
    colors = ['r', 'g', 'g', 'g', 'g', 'm', 'm', 'r']
    #label start and end
    labels = {1:'Start', 2:'2', 3:'3', 4:'4',5:'5', 6:'6', 7:'7', 8:'End'}
    sizes = [800, 300, 300, 300, 300, 600, 300, 800]
    nx.draw_networkx(G, node_color=colors, node_shape='D',
                    with_labels=True, labels=labels,node_size=sizes)
    #let's save that. make sure it's before the show() or else it'll be blank!
    plt.savefig('directed.png', format='png')
    plt.show()
def main():
    #pieCharts()
    #barCharts()
    #histograms()
    #boxplots()
    #scatterplots()
    #correlations()
    #timeSeries()
    #trends()
    #geo()
    #undirected()
    directed()
if __name__ == "__main__": main()