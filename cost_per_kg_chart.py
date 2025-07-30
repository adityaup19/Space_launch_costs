import pandas as pd
import matplotlib.pyplot as plt

# 1) My data
data = [
    {"vehicle": "Long March 11", "year": 2019, "cost_per_kg": 10600, "class": "Small"},
    {"vehicle": "Falcon Heavy",  "year": 2018, "cost_per_kg": 1500,  "class": "Heavy"},
    {"vehicle": "Minotaur IV",   "year": 2017, "cost_per_kg": 30500, "class": "Small"},
    {"vehicle": "Long March 5",  "year": 2016, "cost_per_kg": 7900,  "class": "Heavy"},
    {"vehicle": "Angara",        "year": 2014, "cost_per_kg": 4500,  "class": "Heavy"},
]
df = pd.DataFrame(data)

# 2) Combining vehicle and year into 1 label
df["label"] = df.apply(lambda r: f"{r.vehicle}\n({r.year})", axis=1)

# 3) Professional‐style bar chart
plt.style.use('ggplot')
fig, ax = plt.subplots(figsize=(10, 6), dpi=100)

# sort by cost
df_sorted = df.sort_values('cost_per_kg', ascending=True)
bars = ax.bar(df_sorted['label'], df_sorted['cost_per_kg'], color='#4C72B0')

# gridlines
ax.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)
ax.set_axisbelow(True)

# annotate values
for bar in bars:
    y = bar.get_height()
    ax.annotate(
        f'{int(y):,}',
        xy=(bar.get_x() + bar.get_width() / 2, y),
        xytext=(0, 5),
        textcoords='offset points',
        ha='center',
        va='bottom',
        fontsize=10
    )

# labels, title, footnote
ax.set_ylabel('Cost (US$ per kg)', fontsize=12)
ax.set_title('Launch Cost per kg to LEO', fontsize=14, fontweight='bold')
fig.text(0.99, 0.01, 'Data source: CSIS Aerospace Security Project', ha='right', va='bottom', fontsize=8)

plt.tight_layout()
plt.show()
