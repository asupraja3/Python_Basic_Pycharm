# plt.plot(): Plot y versus x as lines and/or markers.
# Commonly used to visualize trends, time series, and continuous relationships.

# Full Parameter Reference:
#
# x: (array-like) Values for the x-axis. Can be omitted, in which case indices are used.
# y: (array-like) Values for the y-axis.
# color / c: (str) Color of the line. Can be a name ('blue'), hex code ('#1f77b4'), or RGB tuple.
# label: (str) Label for the plotted line, used in legends.
# linewidth / lw: (float) Width of the line in points.
# linestyle / ls: (str) Line style, options include:
#     - '-' : solid
#     - '--': dashed
#     - '-.': dash-dot
#     - ':' : dotted
# marker: (str) Marker style to represent data points. Examples: 'o', 's', '^', '*', 'D', 'x'
# markersize / ms: (float) Size of the marker in points.
# markerfacecolor / mfc: (str) Fill color of the marker.
# markeredgecolor / mec: (str) Border color of the marker.
# markeredgewidth / mew: (float) Width of the marker edge.
# alpha: (float between 0 and 1) Transparency level of the plot line and markers.
# zorder: (int) Drawing priority. Higher zorder means on top.
# drawstyle: (str) Connect style: 'default', 'steps', 'steps-pre', 'steps-post', etc.
# solid_capstyle: (str) Style for line endpoints: 'butt', 'round', 'projecting'.
# solid_joinstyle: (str) Style for line joins: 'miter', 'round', 'bevel'.
# dash_capstyle, dash_joinstyle: Similar styles for dashed lines.
# antialiased / aa: (bool) Whether to apply anti-aliasing for smoother rendering.
# data: (dict or DataFrame) An object from which to extract x and y using string keys.

# Example usage:
import matplotlib.pyplot as plt

# Sample data
x = [0, 1, 2, 3, 4, 5]
y = [0, 1, 4, 9, 16, 25]

# Create a detailed line plot
plt.plot(
    x, y,                             # x and y data
    color='darkorange',              # line color
    label='x squared',               # legend label
    linewidth=2.5,                   # thicker line
    linestyle='--',                  # dashed line
    marker='o',                      # circular markers at data points
    markersize=8,                    # marker size
    markerfacecolor='white',         # hollow markers
    markeredgecolor='darkorange',    # border matches line color
    alpha=0.9,                        # slightly transparent
    zorder=3                          # ensure this line appears on top
)

plt.title("Line Plot: y = x²")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.legend()
plt.grid(True)
plt.show()

"-----------------------------------------------------------------------------------------------------------------------"
# plt.scatter(): Create a scatter plot of individual data points.
# Useful for showing correlation, clusters, and distributions in 2D space.

# Full Parameter Reference:
#
# x: (array-like) X-axis coordinates of data points.
# y: (array-like) Y-axis coordinates of data points.
# s: (float or array-like) Marker size in points². Can be a constant or array of size-encoded values.
# c: (str, array-like, or list) Marker color(s). Can be:
#     - a single color (e.g., 'blue', '#FF5733')
#     - an array of numbers (with cmap) to encode color by value
# cmap: (str or Colormap) Colormap name for `c` when numeric. Examples: 'viridis', 'plasma', 'coolwarm'.
# norm: (Normalize object) Normalize scalar values in `c` to the 0–1 range for colormaps.
# vmin, vmax: (float) Bounds for data normalization.
# alpha: (float) Opacity of markers (0.0 to 1.0).
# linewidths: (float or array-like) Width of marker edges.
# edgecolors: (str or list) Color of marker edges. Can be 'face' to match fill color.
# marker: (str) Marker style. Common options: 'o' (circle), '^' (triangle), 's' (square), '*' (star), 'x' (cross).
# label: (str) Label used in the legend.
# data: (DataFrame or dict) Optional data source when passing variable names as strings.
# zorder: (int) Drawing order priority.
# rasterized: (bool) Rasterize markers for efficient vector graphics.

# Example usage:
import matplotlib.pyplot as plt
import numpy as np

# Random dataset
np.random.seed(42)
x = np.random.rand(50)
y = np.random.rand(50)
sizes = np.random.rand(50) * 500     # variable marker sizes
colors = np.random.rand(50)          # color scale values

# Create scatter plot
plt.scatter(
    x, y,                            # coordinates
    s=sizes,                         # size encoding
    c=colors,                        # color encoding
    cmap='viridis',                  # colormap
    alpha=0.7,                       # transparency
    edgecolors='black',              # outline color
    linewidths=0.5,                  # edge width
    marker='o',                      # marker type
    label='Data points'             # legend label
)

plt.colorbar(label='Color scale')    # add colorbar for c values
plt.title("Scatter Plot with Size and Color Encoding")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.legend()
plt.grid(True)
plt.show()

"-----------------------------------------------------------------------------------------------------------------------"
# plt.bar(): Draw vertical bars to represent quantities for categories.
# Typically used for comparisons of discrete categories.

# Full Parameter Reference:
#
# x: (array-like) Categories or positions of the bars (e.g., names or numerical positions).
# height: (array-like) Heights of the bars corresponding to each x.
# width: (float or array-like) Width of each bar (default: 0.8).
# bottom: (float or array-like) Starting point of each bar on the y-axis.
# align: (str) Alignment of the bars: 'center' (default) or 'edge'.
# color: (str or list) Fill color for the bars. Can be a single color or a list matching `x`.
# edgecolor: (str or list) Color of the bar edges.
# linewidth: (float or array-like) Width of the bar borders.
# tick_label: (str or list) Custom labels to use as x-tick labels.
# alpha: (float) Transparency of the bars.
# label: (str) Label for use in the legend.
# zorder: (int) Drawing priority order on canvas.
# hatch: (str) Pattern on the bars (e.g., '/', '\\', '|', '-', '+').

# Example usage:
import matplotlib.pyplot as plt

# Sample data
categories = ['A', 'B', 'C', 'D']
values = [23, 17, 35, 29]

# Plot vertical bars
plt.bar(
    x=categories,
    height=values,
    width=0.6,
    color='skyblue',
    edgecolor='black',
    linewidth=1.2,
    alpha=0.85,
    label='Sales Volume',
    zorder=3
)

plt.title("Bar Chart Example")
plt.xlabel("Category")
plt.ylabel("Value")
plt.legend()
plt.grid(axis='y', linestyle='--', zorder=0)
plt.show()

"-----------------------------------------------------------------------------------------------------------------------"
# plt.hist(): Plot a histogram to show the distribution of numeric data.
# Groups data into intervals (bins) and plots frequencies.

# Full Parameter Reference:
#
# x: (array-like) Input data to be binned and plotted.
# bins: (int or sequence or str) Number of bins, explicit bin edges, or binning strategy (e.g., 'auto', 'fd', 'sturges').
# range: (tuple) Lower and upper range of bins. Data outside this range is ignored.
# density: (bool) If True, normalize to form a probability density (area = 1).
# cumulative: (bool) Plot cumulative counts.
# color: (str) Fill color of bars.
# edgecolor: (str) Color of bar edges.
# linewidth: (float) Width of bar edge lines.
# histtype: (str) Bar style: 'bar' (default), 'barstacked', 'step', 'stepfilled'.
# align: ('mid', 'left', 'right') Positioning of bars relative to bin edges.
# orientation: ('vertical' or 'horizontal') Direction of the bars.
# alpha: (float) Transparency of bars.
# label: (str) Label for legend.
# stacked: (bool) Stack multiple data series (if passed).

# Example usage:
import numpy as np
import matplotlib.pyplot as plt

# Create random data
data = np.random.normal(loc=0, scale=1, size=1000)

# Plot histogram
plt.hist(
    data,
    bins=30,
    color='steelblue',
    edgecolor='black',
    linewidth=0.5,
    density=True,
    histtype='stepfilled',
    alpha=0.8,
    label='Normal Distribution'
)

plt.title("Histogram of Normally Distributed Data")
plt.xlabel("Value")
plt.ylabel("Density")
plt.legend()
plt.grid(True)
plt.show()

"-----------------------------------------------------------------------------------------------------------------------"
# plt.boxplot(): Create a box-and-whisker plot to show summary statistics (median, quartiles, outliers).
# Useful for detecting skewness and comparing distributions.
#Skewness is a statistical measure that describes the asymmetry of a data distribution around its mean. It tells you
# whether the data leans more to the left or right, or is fairly symmetric.

# Full Parameter Reference:
#
# x: (array-like or sequence of arrays) Data to plot. Each array is a separate box.
# notch: (bool) Whether to draw a notch for the median (shows CI).
# vert: (bool) If True (default), boxplot is vertical.
# patch_artist: (bool) If True, fill the boxes with color.
# widths: (float or sequence) Widths of the boxes.
# meanline: (bool) If True, draw mean as a line (instead of a point).
# showmeans: (bool) Whether to show the mean marker.
# showcaps: (bool) Show the caps on the ends of the whiskers.
# showbox: (bool) Show the box itself.
# showfliers: (bool) Show outlier markers.
# boxprops: (dict) Style dict for the box appearance.
# whiskerprops, capprops, flierprops, medianprops, meanprops: Style dicts for customization.
# labels: (list of str) Custom labels for each box.
# manage_ticks: (bool) Automatically adjust axis ticks.
# autorange: (bool) Automatically set whisker length.
# zorder: (int) Drawing layer priority.

# Example usage:
import matplotlib.pyplot as plt
import numpy as np

# Simulated grouped data
data = [np.random.normal(0, std, 100) for std in range(1, 4)]

# Draw boxplot with customization
plt.boxplot(
    data,
    notch=True,
    patch_artist=True,
    widths=0.5,
    showmeans=True,
    meanline=False,
    showcaps=True,
    showfliers=True,
    labels=['Group A', 'Group B', 'Group C'],
    boxprops=dict(facecolor='lightblue', color='black'),
    medianprops=dict(color='red'),
    meanprops=dict(marker='D', markerfacecolor='white', markeredgecolor='blue'),
    flierprops=dict(marker='o', color='gray', alpha=0.5)
)

plt.title("Box Plot of Three Groups")
plt.ylabel("Value")
plt.grid(True)
plt.show()
