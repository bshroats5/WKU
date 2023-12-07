import matplotlib.pyplot as plt

# Example data for teams
teams = ['WKU Trojans', 'Eastern Kentucky Colonels']
fouls = [17, 20]

# Create a bar graph
plt.bar(teams, fouls)

# Define colors for each team
WKU_color = 'Red'
eastern_kentucky_color = 'Maroon'

# Create a bar graph with custom colors
plt.bar(teams, fouls, color=[WKU_color, eastern_kentucky_color])


# Add title and labels
plt.title('Team Fouls')
plt.xlabel('Teams')
plt.ylabel('Fouls')

# Show the plot
plt.show()
