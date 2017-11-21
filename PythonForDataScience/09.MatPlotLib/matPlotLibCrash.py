#Samuel L. Peoples
import matplotlib.pyplot as plt

#defining the plot
def graph():
    values = [1, 5, 8, 9, 2, 0, 3, 10, 4, 7]
    values2 = [3, 8, 9, 2, 1, 2, 4, 7, 6, 6]
    #Let's make those axes look nice.
    ax = plt.axes()
    ax.set_xlim([0, 11])
    ax.set_ylim([-1, 11])
    ax.set_xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    ax.set_yticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    #labeling
    plt.xlabel('Entries')
    plt.ylabel('Values')
    #annotation
    plt.annotate(xy=[1,1], s='First Entry')
    #add some gridding!
    ax.grid()
    #graphs the values as a simple line-graph
    line1 = plt.plot(range(1,11), values,'H-.')#dash dotted, hexagon indicators
    line2 = plt.plot(range(1,11), values2,'d--')#dashed, thin diamond indicators
    #legend
    plt.legend(['First', 'Second'], loc=4)
    #title
    plt.title('My Graph')
    #let's save that. make sure it's before the show() or else it'll be blank!
    plt.savefig('plot.png', format='png')
    plt.show()
    
def main():
    graph()
if __name__ == "__main__": main()