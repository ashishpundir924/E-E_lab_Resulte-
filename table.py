import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta

# Define the tasks and their durations
tasks = [
    ("Prepare Workstation", "Engine Assembly Area", "EA01", timedelta(hours=0.5 + 0.75)),  # 0.5 setup + 0.45 run
    ("Gather Components", "Engine Assembly Area", "EA01", timedelta(hours=0.3 + 0.5)),  # 0.3 setup + 0.3 run
    ("Pre-Assembly Inspection", "Engine Assembly Area", "ES10", timedelta(hours=0.2 + 0.33)),  # 0.2 setup + 0.33 run
    ("Engine Block Assembly", "Engine Stand", "ES10", timedelta(hours=1.5 + 0.75)),  # 1.5 setup + 0.75 run
    ("Cylinder Head Assembly", "Engine Stand", "EA01", timedelta(hours=1 + 0.5)),  # 1 setup + 0.5 run
    ("Sealing and Gasket Application", "Engine Assembly Area", "EA01", timedelta(hours=0.2 + 0.33)),  # 0.2 setup + 0.33 run
    ("Final Assembly", "Engine Assembly Area", "EA01", timedelta(hours=1 + 0.83)),  # 1 setup + 0.83 run
    ("Testing and Inspection", "Testing Area", "TA05", timedelta(hours=0.5 + 2.5)),  # 0.5 setup + 2.5 run
    ("Quality Assurance", "Quality Control Station", "QC15", timedelta(hours=0.3 + 1)),  # 0.3 setup + 1 run
    ("Packaging and Storage", "Packaging Area", "PA03", timedelta(hours=0.4 + 0.5)),  # 0.4 setup + 0.5 run
]

# Calculate the start and end times of each task
start_time = datetime(2024, 4, 26, 8, 0)  # Starting at 8:00 AM on the specified date
task_times = []
for task in tasks:
    task_name, workstation, symbol, duration = task
    end_time = start_time + duration
    task_times.append((task_name, start_time, end_time, workstation, symbol))
    start_time = end_time

# Create the Gantt chart
fig, ax = plt.subplots(figsize=(14, 8))

for task in task_times:
    task_name, start, end, workstation, symbol = task
    ax.barh(task_name, end - start, left=start, align='center', label=workstation, edgecolor='black')

# Format the x-axis to show the time correctly
ax.xaxis.set_major_locator(mdates.HourLocator(interval=1))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))

# Set labels and title
plt.xlabel('Time')
plt.ylabel('Tasks')
plt.title('Gantt Chart for Engine Assembly Process')

# Rotate date labels on x-axis
plt.xticks(rotation=45)

# Display the legend
handles, labels = ax.get_legend_handles_labels()
by_label = dict(zip(labels, handles))
ax.legend(by_label.values(), by_label.keys(), title='Workstation')

plt.tight_layout()
plt.show()
