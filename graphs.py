import matplotlib.pyplot as plt

import pandas as pd
import sqlite3


conn = sqlite3.connect("shiptivity.db")
df = pd.read_sql_query("SELECT * FROM login_history;", conn)

df['login_timestamp'] = pd.to_datetime(df['login_timestamp'], unit='s')

# Login frequency / Day

before = df[df.login_timestamp < pd.to_datetime(1527897600, unit='s')]
ax = before.groupby(before.login_timestamp.dt.date).size().plot(title='Login frequency / Day')

after = df[df.login_timestamp > pd.to_datetime(1527897600, unit='s')]
after.groupby(after.login_timestamp.dt.date).size().plot(ax=ax, title='Login frequency / Day')

ax.legend(['Login frequency / Day (Before)', 'Login frequency / Day (After)'])

plt.show()


# Unique users / Day

before = df[df.login_timestamp < pd.to_datetime(1527897600, unit='s')].drop_duplicates(['user_id'])
ax = before.groupby(before.login_timestamp.dt.date).size().plot(title='Unique users / Day')

after = df[df.login_timestamp > pd.to_datetime(1527897600, unit='s')].drop_duplicates(['user_id'])
after.groupby(after.login_timestamp.dt.date).size().plot(ax=ax, title='Unique users / Day')

ax.legend(['Unique users / Day (Before)', 'Unique users / Day (After)'])

plt.show()
