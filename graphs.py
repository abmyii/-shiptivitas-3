import matplotlib.pyplot as plt

import pandas as pd
import sqlite3


fig, axes = plt.subplots(nrows=2)

conn = sqlite3.connect("shiptivity.db")
df = pd.read_sql_query("SELECT * FROM login_history;", conn)

df['login_timestamp'] = pd.to_datetime(df['login_timestamp'], unit='s')
df.set_index('login_timestamp', inplace=True)

ax = df[df.index < pd.to_datetime(1527897600, unit='s')]['user_id'].plot(ax=axes[0], title='Login frequency (Before)')
ax2 = df[df.index > pd.to_datetime(1527897600, unit='s')]['user_id'].plot(ax=axes[1], title='Login frequency (After)')

fig.tight_layout()
plt.show()
