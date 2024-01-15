import matplotlib.pyplot as plt


def turn_off_right_upper_spines(ax:plt.Axes):
    ax.spines[['top', 'right']].set_visible(False)
    return ax


def rotate_xticks_labels(ax:plt.Axes, degree:int):
    for tick in ax.get_xticklabels():
        tick.set_rotation(90)
    return ax