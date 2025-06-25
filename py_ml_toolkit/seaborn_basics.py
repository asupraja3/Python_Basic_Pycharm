
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
# Sample DataFrame for illustration
df = sns.load_dataset('iris')

# sns.scatterplot(): Draw a scatter plot with support for color, size, and style encodings based on DataFrame variables.
# Full Parameter Reference:
#
# x: (str or vector) Variable name in `data` for the x-axis. Can also be passed as a list/array directly.
# y: (str or vector) Variable name in `data` for the y-axis. Can also be passed as a list/array directly.
# hue: (str or vector) Variable that defines groups for color encoding. Creates a legend and colors each group differently.
# style: (str or vector) Variable that maps to different marker styles (e.g., circle, square, triangle).
# size: (str or vector) Variable that controls the relative size of each point based on its value.
# data: (DataFrame) The data source containing all variables. Required if variable names (x, y, hue, etc.) are passed as strings.
# palette: (str, list, or dict) The color palette to use (e.g., 'deep', 'muted', ['red', 'blue'], or {'A': 'red', 'B': 'blue'}).
# hue_order: (list of str) Specific order in which levels of the `hue` variable should appear in the plot and legend.
# size_order: (list of str) Specific order in which levels of the `size` variable should be mapped to marker sizes.
# sizes: (tuple or dict) Range (min_size, max_size) for numeric variables or dictionary for categorical size mapping.
# marker: (str or dict) Marker style for all points or dictionary mapping levels of `style` variable to marker shapes.
# style_order: (list of str) Explicit order of `style` levels to maintain control over marker mapping.
# ax: (matplotlib.axes.Axes) Axes to draw the plot on, otherwise uses current active axes.
# legend: ({"auto", "brief", "full"} or bool) Controls legend content:
#         - "auto": try to determine best format
#         - "brief": only essential entries
#         - "full": all possible combinations
#         - False: hide legend entirely
# linewidth: (float) Width of marker edge lines.
# edgecolor: (str or color) Color of the edge surrounding each marker.
# alpha: (float between 0 and 1) Opacity of the marker.
# s: (float) Size of all markers in points² (ignored if `size` is used).

# Load a sample dataset
df = sns.load_dataset("penguins")

# Create a detailed scatterplot with multiple semantic mappings
sns.scatterplot(
    x='bill_length_mm',                # x-axis from 'bill_length_mm' column
    y='bill_depth_mm',                 # y-axis from 'bill_depth_mm' column
    data=df,                           # data source
    hue='species',                     # color represents species
    style='sex',                       # marker shape represents sex
    size='body_mass_g',                # size represents body mass
    hue_order=['Adelie', 'Chinstrap', 'Gentoo'],       # specific color order
    style_order=['Male', 'Female'],                    # specific style order
    sizes=(20, 300),                   # min and max marker size
    palette='Set2',                    # pastel-like colors
    marker='o',                        # default marker for all if `style` not used
    linewidth=0.7,                     # thin border around points
    edgecolor='black',                 # black border color for visibility
    alpha=0.8,                         # slightly transparent points
    s=100,                             # default size if `size` not used (ignored here)
    legend='full'                      # show full legend including all mappings
)

plt.show()
# ----------------------------------------------------------------------------------------------------------------------

# sns.lineplot(): Draw a line plot with optional color, style, and size encodings for grouped data.
# Full Parameter Reference:
#
# x: (str or array-like) Name of variable for x-axis. Can be column in `data` or a Series/array.
# y: (str or array-like) Name of variable for y-axis. Can be column in `data` or a Series/array.
# data: (DataFrame or dict-like) Dataset containing the variables to plot.
# hue: (str or array-like) Variable that determines the line color. Each unique level will get a different color.
# hue_order: (list) Order to plot levels of the `hue` variable in both the plot and the legend.
# palette: (str, list, dict) Color palette. E.g., "deep", "Set1", ["red", "blue"], or {'class1': 'red'}.
# style: (str or array-like) Variable that determines the line dash style.
# style_order: (list) Order to plot levels of the `style` variable.
# dashes: (bool, list, dict) Dash styles for lines. True enables default dashed lines, False makes solid lines.
# markers: (bool, list, dict) Whether to draw markers on data points. If True, uses default marker. Can also specify per-group.
# size: (str or array-like) Grouping variable that controls line width.
# size_order: (list) Order of size groups.
# sizes: (tuple of 2 floats or dict) Range (min_width, max_width) or dict mapping categories to line widths.
# estimator: (callable or None) Function to aggregate multiple y values at each x (e.g., mean, median). Use None to plot all data points.
# ci: (int or "sd" or None) Confidence interval size to show around the estimator. 95 = 95% CI. "sd" = standard deviation.
# n_boot: (int) Number of bootstrap samples used to compute CI.
# sort: (bool) Whether to sort data by x-axis before plotting. Default is True.
# err_style: ("band" or "bars") Type of CI visualization (shaded band or error bars).
# err_kws: (dict) Additional arguments passed to error bar drawing function.
# legend: ("auto", "brief", "full", or False) Controls legend content:
#         - "auto": tries to find best layout
#         - "brief": minimal legend
#         - "full": all levels of mappings
#         - False: suppress legend
# ax: (matplotlib.axes.Axes) Axes to draw the plot on.
# lw or linewidth: (float) Width of the line (can also be controlled by `size` if set).
# alpha: (float) Transparency level of lines (0 to 1).

# Example usage:
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = sns.load_dataset("fmri")

# Plot a lineplot with semantic groupings
sns.lineplot(
    data=df,
    x="timepoint",                     # x-axis: time
    y="signal",                        # y-axis: signal strength
    hue="event",                       # color by event type
    style="region",                    # line style by brain region
    markers=True,                      # draw markers at data points
    dashes=False,                      # solid lines for all styles
    ci=68,                             # 68% confidence interval band
    estimator="mean",                 # aggregate with mean (default)
    linewidth=2.2,                     # line thickness
    alpha=0.9,                         # slightly transparent
    palette="Set2",                   # color palette for hue
    legend="full"                      # show full legend
)

plt.title("FMRI Signal over Time")
plt.xlabel("Timepoint")
plt.ylabel("Signal Intensity")
plt.grid(True)
plt.show()

# ----------------------------------------------------------------------------------------------------------------------

# sns.histplot(): Plot a histogram for one or two variables with support for semantic grouping and KDE overlays.
# Full Parameter Reference:
#
# data: (DataFrame, Series, array-like) The dataset containing variables for plotting. Required if passing variable names as strings.
# x: (str or array-like) Variable to be plotted along the x-axis. Can be a column name or a direct array.
# y: (str or array-like) Optional. If provided, creates a bivariate histogram.
# hue: (str or array-like) Variable that defines groups by color. Each hue level will be represented separately.
# weights: (str or array-like) Variable providing weights to use for computing histogram bars.
# stat: (str) Defines the type of statistic to plot:
#       - 'count': raw count of observations (default)
#       - 'frequency': fraction of observations divided by total
#       - 'probability': synonym for frequency
#       - 'percent': percentage of total
#       - 'density': probability density normalized such that the area under the histogram = 1
# bins: (int, list, or str) Number of bins (e.g., 20), explicit bin edges list, or method like 'auto', 'sturges', etc.
# binrange: (tuple of 2 values) Lower and upper range of bins to compute. Data outside this range is ignored.
# binwidth: (float or tuple) Width of each bin. Can be specified instead of bins count.
# discrete: (bool) If True, treats input data as discrete values. Plots histogram as a bar plot.
# kde: (bool) Whether to overlay a kernel density estimate (KDE) curve. Useful for smooth distribution shapes.
# cumulative: (bool) If True, plot cumulative counts across the bins.
# common_bins: (bool) If True, all subsets (hue levels) share the same bin edges. If False, each group gets its own binning.
# multiple: (str) Method for plotting multiple histograms:
#       - 'layer': Overlap all plots with transparency
#       - 'stack': Stack histograms on top of each other
#       - 'dodge': Side-by-side bars
#       - 'fill': Stack, but normalize to 100% height
# element: (str) Shape representation of histogram:
#       - 'bars': Default histogram bars
#       - 'step': Outlined, unfilled histogram
#       - 'poly': Connected lines instead of bars
# fill: (bool) Whether to fill under step or poly plots.
# shrink: (float between 0 and 1) Proportion to reduce bar width, useful when `multiple="dodge"`.
# hue_order: (list) Custom order to plot hue levels.
# palette: (str, list, or dict) Color palette for hue levels (e.g., 'deep', 'Set2', ['blue', 'green']).
# linewidth: (float) Width of the edge lines of histogram bars.
# linecolor: (str) Color of bar edges.
# ax: (matplotlib.axes.Axes) Specific axes to draw on.

# Example usage:
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = sns.load_dataset("penguins")

# Plot histogram of flipper lengths for each species with KDE
sns.histplot(
    data=df,
    x="flipper_length_mm",         # x-axis variable
    hue="species",                 # color by species
    bins=20,                       # number of bins
    kde=True,                      # overlay KDE curve
    stat="density",                # normalize so area = 1
    multiple="stack",              # stack hue levels
    element="bars",                # standard filled bars
    fill=True,                     # fill bars (default for bars)
    palette="deep",                # seaborn color palette
    linewidth=0.5,                 # bar edge width
    linecolor="black",             # bar edge color
    shrink=0.9,                    # slightly narrow bars for visual clarity
)

plt.title("Histogram of Flipper Lengths by Penguin Species")
plt.xlabel("Flipper Length (mm)")
plt.ylabel("Density")
plt.grid(True)
plt.show()


# ----------------------------------------------------------------------------------------------------------------------
# sns.boxplot(): Create box plots to display distribution statistics (median, IQR, outliers) for categories.
# Full Parameter Reference:
#
# x: (str or array-like) Name of variable to be used on the x-axis (categorical axis).
# y: (str or array-like) Name of variable to be used on the y-axis (numeric axis).
# data: (DataFrame) The dataset to draw the plot from.
# hue: (str or array-like) Variable that defines nested groupings within each category and is represented by color.
# order: (list of str) Order to display categories in x-axis.
# hue_order: (list of str) Order to display hue variable levels.
# orient: ('v' or 'h') Orientation of the plot — vertical or horizontal.
# color: (str or color) Single color to apply to all boxes (overrides palette).
# palette: (str, list, or dict) Color palette for boxes when `hue` is used (e.g., 'Set2', ['#d62728', '#1f77b4']).
# saturation: (float) Proportion of color intensity; 0 (transparent) to 1 (full color).
# width: (float between 0 and 1) Width of each box.
# fliersize: (float) Size of the outlier markers.
# linewidth: (float) Width of the lines (box edges, whiskers, etc.).
# notch: (bool) Whether to draw a notch to represent the confidence interval around the median.
# showcaps: (bool) Whether to show the caps at min and max values.
# showfliers: (bool) Whether to show outlier points.
# showcmeans: (bool) Whether to show the mean of the distribution.
# meanline: (bool) If True, draw the mean as a line rather than a point (requires `showmeans=True`).
# boxprops: (dict) Customizations for box appearance (e.g., {'facecolor': 'white', 'edgecolor': 'black'}).
# whiskerprops, capprops, flierprops, medianprops, meanprops: (dict) Style dicts for respective components.
# ax: (matplotlib.axes.Axes) Axes to draw the plot on.

# Example usage:
import seaborn as sns
import matplotlib.pyplot as plt

# Load example data
df = sns.load_dataset("tips")

# Create a boxplot comparing total bills across different days, separated by sex
sns.boxplot(
    data=df,
    x="day",                        # x-axis: categorical variable (days)
    y="total_bill",                 # y-axis: numeric variable (total bill)
    hue="sex",                      # color by gender
    order=["Thur", "Fri", "Sat", "Sun"],     # custom order for x categories
    hue_order=["Female", "Male"],            # custom order for hue groups
    palette="pastel",               # use soft pastel colors
    width=0.6,                      # make boxes slightly narrower
    fliersize=5,                    # size of outlier dots
    linewidth=1.2,                  # line thickness for box and whiskers
    notch=False,                    # no notches in boxes
    showmeans=True,                # show the mean as a marker
    meanline=False,                # draw mean as point, not line
    showcaps=True,                 # show min/max caps
    showfliers=True                # display outlier points
)

plt.title("Total Bill Distribution by Day and Sex")
plt.xlabel("Day of the Week")
plt.ylabel("Total Bill ($)")
plt.grid(True)
plt.show()

# ----------------------------------------------------------------------------------------------------------------------
# sns.heatmap(): Plot rectangular 2D data as a color-encoded matrix (heatmap), useful for correlation matrices and confusion matrices.
# Full Parameter Reference:
#
# data: (2D array-like or DataFrame) The matrix-like input data to visualize. If DataFrame, both axes and labels are used.
# vmin: (float) Minimum value to anchor the colormap. All values below this will have same color as vmin.
# vmax: (float) Maximum value to anchor the colormap. All values above this will have same color as vmax.
# cmap: (str or matplotlib colormap) Colormap to use. E.g., 'viridis', 'coolwarm', 'Blues', 'magma'.
# center: (float) Value at which to center the colormap (e.g., 0 for diverging heatmaps).
# robust: (bool) If True, use robust quantiles for vmin and vmax when colormap auto-scaling, ignoring outliers.
# annot: (bool or array-like) If True, write the data values in each cell. Can also pass a matrix of strings or values to annotate.
# fmt: (str) String formatting code for annotations (e.g., ".2f" for float with 2 decimal places).
# annot_kws: (dict) Keyword arguments for formatting annotation text (e.g., {'fontsize': 10, 'color': 'black'}).
# linewidths: (float) Width of the lines that divide each cell.
# linecolor: (str or color) Color of the lines between cells.
# cbar: (bool) Whether to draw a colorbar alongside the heatmap.
# cbar_kws: (dict) Additional keyword arguments for colorbar (e.g., {'orientation': 'horizontal', 'label': 'Intensity'}).
# square: (bool) Force cells to be square (equal height and width).
# mask: (bool array or DataFrame) Matrix of same shape as `data` where True means cell is hidden.
# xticklabels: (bool, list, or int) Controls x-axis tick labels. True=show, False=hide, list=custom labels, int=label frequency.
# yticklabels: (bool, list, or int) Controls y-axis tick labels.
# ax: (matplotlib.axes.Axes) Specific matplotlib Axes to draw the heatmap on.
# norm: (Normalize object) Advanced normalization for color scaling (use from matplotlib.colors).
# rasterized: (bool) If True, rasterize the heatmap (useful for PDF saving and large matrices).
# clip_on: (bool) Whether to clip the elements at the Axes boundary.

# Example usage:
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Create 6x6 random matrix
data = np.random.rand(6, 6)

# Generate a heatmap with annotations, gridlines, and a custom colormap
sns.heatmap(
    data,                            # 2D matrix input
    cmap="viridis",                  # color map
    vmin=0, vmax=1,                  # set fixed scale from 0 to 1
    center=0.5,                      # midpoint for diverging colormaps (optional here)
    annot=True,                      # show values in each cell
    fmt=".2f",                       # format values to 2 decimal places
    annot_kws={"fontsize": 9},       # annotation text style
    linewidths=0.5,                  # thin lines between cells
    linecolor="white",              # line color between cells
    square=True,                     # force square cells
    cbar=True,                       # display colorbar
    cbar_kws={"orientation": "vertical", "label": "Intensity"},  # customize colorbar
    xticklabels=True,               # show x tick labels
    yticklabels=True                # show y tick labels
)

plt.title("Random 6x6 Heatmap")
plt.xlabel("Column Index")
plt.ylabel("Row Index")
plt.show()

# ----------------------------------------------------------------------------------------------------------------------
# sns.pairplot(): Create a grid of scatter plots for pairwise relationships in a dataset, with optional histograms on the diagonal.
# sns.barplot(): Create bar plots to visualize categorical data with optional error bars.
# Full Parameter Reference:
# # data: (DataFrame) The dataset containing variables to plot.
# x: (str) Name of variable for x-axis (categorical).
# y: (str) Name of variable for y-axis (numeric).
# hue: (str) Variable that defines groups by color.
# hue_order: (list) Order to plot levels of the `hue` variable.
# palette: (str, list, or dict) Color palette for hue levels (e.g., 'deep', ['red', 'blue'], {'A': 'red', 'B': 'blue'}).
# order: (list) Order to plot categories on the x-axis.
# estimator: (callable) Function to aggregate multiple y values at each x (e.g., mean, median). Default is mean.
# ci: (int or "sd" or None) Size of confidence interval to show around the estimate. 95 = 95% CI. "sd" = standard deviation.
# n_boot: (int) Number of bootstrap samples used to compute CI.
# capsize: (float) Size of the error bar caps.
# errcolor: (str) Color of the error bars.
# errwidth: (float) Width of the error bars.
# orient: ('v' or 'h') Orientation of the plot (vertical or horizontal).
# saturation: (float) Proportion of color intensity; 0 (transparent) to 1 (full color).
# dodge: (bool) If True, separate bars for each hue level. If False, stack them.
# width: (float between 0 and 1) Width of each bar.
# capprops, errprops: (dict) Customizations for error bar caps and error bars.
# ax: (matplotlib.axes.Axes) Axes to draw the plot on.
# Example usage:
import seaborn as sns
import matplotlib.pyplot as plt
# Load dataset
df = sns.load_dataset("tips")
# Create a bar plot showing average total bill by day, colored


