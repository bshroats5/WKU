import matplotlib.pyplot as plt
# Initialize figure and axis
fig, ax = plt.subplots()

# Data for Eastern Kentucky
eastern_kentucky_fg = 26
eastern_kentucky_fga = 62
eastern_kentucky_3pt = 6
eastern_kentucky_3pta = 24

# Data for WKU
WKU_fg = 28
WKU_fga = 69
WKU_3pt = 11
WKU_3pta = 25

# Calculate percentages
eastern_kentucky_fg_percentage = eastern_kentucky_fg / eastern_kentucky_fga * 100
eastern_kentucky_3pt_percentage = eastern_kentucky_3pt / eastern_kentucky_3pta * 100
WKU_fg_percentage = WKU_fg / WKU_fga * 100
WKU_3pt_percentage = WKU_3pt / WKU_3pta * 100

# Set bar width and positions
bar_width = 0.35  # Width of each bar
index = [1, 2, 4, 5]  # X-axis positions for the bars

# Set bar colors
colors = ["#800000", "#000000", "#FF0000", "#FF0000"]  # Maroon, Black, Red, Red

# Create the bars
ax.bar(index[0], eastern_kentucky_fg_percentage, bar_width, label="EKU FG%", color=colors[0])
ax.bar(index[1], eastern_kentucky_3pt_percentage, bar_width, label="EKU 3PT%", color=colors[1])
ax.bar(index[2], WKU_fg_percentage, bar_width, label="WKU FG%", color=colors[2])
ax.bar(index[3], WKU_3pt_percentage, bar_width, label="WKU 3PT%", color=colors[3])

# Set x-axis ticks and labels
ax.set_xticks([index[0] + bar_width / 2, index[1] + bar_width / 2, index[2] + bar_width / 2, index[3] + bar_width / 2])
ax.set_xticklabels(["EKU FG%", "EKU 3PT%", "WKU FG%", "WKU 3PT%"])

# Show the graph
plt.show()
