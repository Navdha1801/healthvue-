import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px

data = pd.read_csv('q4.csv')
df = data.groupby(['Condition', 'Season']).size().reset_index(name='Frequency')
df = df.sort_values(['Season', 'Condition'])

def get_label_rotation(angle, offset):
    rotation = np.rad2deg(angle + offset)
    if angle <= np.pi:
        alignment = "right"
        rotation = rotation + 180
    else: 
        alignment = "left"
    return rotation, alignment

def add_labels(angles, values, labels, offset, ax):
    padding = 4
    for angle, value, label, in zip(angles, values, labels):
        angle = angle
        rotation, alignment = get_label_rotation(angle, offset)
        ax.text(
            x=angle, 
            y=value + padding, 
            s=label, 
            ha=alignment, 
            va="center", 
            rotation=rotation, 
            rotation_mode="anchor"
        ) 

OFFSET = np.pi / 2
VALUES = df["Frequency"].values
LABELS = [f"{condition} - {frequency} Cases" for frequency, condition in zip(df["Frequency"], df["Condition"])]
GROUP = df["Season"].values

PAD = 3
ANGLES_N = len(VALUES) + PAD * len(np.unique(GROUP))
ANGLES = np.linspace(0, 2 * np.pi, num=ANGLES_N, endpoint=False)
WIDTH = (2 * np.pi) / len(ANGLES)

GROUPS_SIZE = [len(i[1]) for i in df.groupby("Season")]

offset = 0
IDXS = []
for size in GROUPS_SIZE:
    IDXS += list(range(offset + PAD, offset + size + PAD))
    offset += size + PAD

fig, ax = plt.subplots(figsize=(20, 10), subplot_kw={"projection": "polar"})
ax.set_theta_offset(OFFSET)
ax.set_ylim(-200, 500)
ax.set_frame_on(False)
ax.xaxis.grid(False)
ax.yaxis.grid(False)
ax.set_xticks([])
ax.set_yticks([])

GROUPS_SIZE = [len(i[1]) for i in df.groupby("Season")]
COLORS = ["#01befe", "#ffdd00", "#ff7d00", "#ff006d", "#adff02", "#8f00ff"]

ax.bar(
    ANGLES[IDXS], VALUES, width=WIDTH, color=COLORS, 
    edgecolor="white", linewidth=2
)

add_labels(ANGLES[IDXS], VALUES, LABELS, OFFSET, ax)


offset = 0 
for group, size in zip(["     Summer", "       Monsoon", "Winter   ", "Fall"], GROUPS_SIZE):
    x1 = np.linspace(ANGLES[offset + PAD], ANGLES[offset + size + PAD - 1], num=50)
    ax.plot(x1, [-10] * 50, color="#333333")
    ax.text(
        np.mean(x1), -50, group, color="#333333", fontsize=10, 
        fontweight="bold", ha="center", va="center"
    )
    x2 = np.linspace(ANGLES[offset], ANGLES[offset + PAD - 1], num=50)
    ax.plot(x2, [100] * 50, color="#bebebe", lw=0.8)
    ax.plot(x2, [200] * 50, color="#bebebe", lw=0.8)
    ax.plot(x2, [300] * 50, color="#bebebe", lw=0.8)
    ax.plot(x2, [400] * 50, color="#bebebe", lw=0.8)
    offset += size + PAD

plt.savefig("q4.svg", format="svg", bbox_inches="tight")