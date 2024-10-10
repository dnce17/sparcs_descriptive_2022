import matplotlib.pyplot as plt
import seaborn as sns

def defineAxes(x_label, y_label, title):
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()


def create_bar(column_name_1, data, x_label, y_label, title, order=None, column_name_2=None):
    if column_name_2 is None:
        sns.countplot(x=column_name_1, data=data, order=order)
    else:
        sns.barplot(x=column_name_1, y=column_name_2, data=data, order=order)
    defineAxes(x_label, y_label, title)


def create_hist(column_name, data, x_label, y_label, title, binwidth):
    sns.histplot(x=column_name, data=data, binwidth=binwidth)
    defineAxes(x_label, y_label, title)


# MAJOR CREDIT to https://stackoverflow.com/questions/72265579/how-can-this-box-plot-be-improved-when-there-is-a-strong-outlier
# Code from link was adapted to create broken axis for a nicer looking box plot
def create_broken_axis_box(data, x_label, y_label, title, y_start):
    # NOTE: () not necessary but added for clarity; subplot returns 3 vals: one figure object + an array of two axes. 
    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
    fig.subplots_adjust(hspace=0.05) 
    
    box = plt.boxplot(data)

    ax1.boxplot(data)
    ax2.boxplot(data)

    # box['whiskers'] contains 2 whiskers (lower and upper whiskers).
    # box['whiskers'][1] corresponds to the upper whisker (max, non-outlier val).
    # .get_ydata() returns the y-values of the whisker, and the second value [1] corresponds to the maximum value.
    ax1.set_ylim(box['whiskers'][1].get_ydata()[1] + 30000, int(data.max()) + 300000)  # Get outlier range
    ax2.set_ylim(y_start, box['whiskers'][1].get_ydata()[1] + 20000)  # Get non-outliers (where most of data lies)
    
    # Removes certain borders that separate the two subplot, making it look like 1 box plot 
    ax1.spines.bottom.set_visible(False)
    ax2.spines.top.set_visible(False)
    ax1.xaxis.tick_top()
    ax1.tick_params(labeltop=False) 
    ax2.xaxis.tick_bottom()

    ax1.set_title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    # Remove exponential notation
    plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)

    # Shows the small diagonal break links
    d = 0.5 
    kwargs = dict(marker=[(-1, -d), (1, d)], 
                markersize=12,
                linestyle="none", 
                color='k', 
                mec='k', 
                mew=1, 
                clip_on=False
                )
                
    ax1.plot([0, 1], [0, 0], transform=ax1.transAxes, **kwargs)
    ax2.plot([0, 1], [1, 1], transform=ax2.transAxes, **kwargs)

    plt.show()