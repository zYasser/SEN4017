
import pandas as pd
import plotly.express as px

# Read the CSV file
df = pd.read_csv("cap.csv", parse_dates=["Start Date", "End Date"])

# Create Gantt chart
fig = px.timeline(
    df,
    x_start="Start Date",
    x_end="End Date",
    y="Name / Title",
    color="Task Color",
    labels={"Task Color": "Task Color"},
    title="Project Gantt Chart",
    category_orders={"Name / Title": "total ascending"},
)

# Customize the layout
fig.update_layout(xaxis_title="Timeline", yaxis_title="Tasks", showlegend=False)

# Show the Gantt chart
fig.show()
