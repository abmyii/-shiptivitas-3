import matplotlib.pyplot as plt
import pandas as pd
import sqlite3

from matplotlib.ticker import AutoMinorLocator, MultipleLocator


conn = sqlite3.connect("shiptivity.db")

# Status changes / Card (bar plot)

df = pd.read_sql_query("SELECT * FROM card_change_history;", conn)
x = pd.DataFrame(df['cardID'].value_counts().sort_index()).reset_index()

ax = x.plot.scatter(x='index', y='cardID', figsize=(20, 5))
ax.set_axisbelow(True)

ax.set_xlim(0, 201)
ax.set_ylim(0.5, 6.05)

ax.xaxis.set_major_locator(MultipleLocator(5))
ax.yaxis.set_major_locator(MultipleLocator(1))

ax.xaxis.set_minor_locator(AutoMinorLocator(5))

ax.grid(which='major', color='#CCCCCC', linestyle='--')
ax.grid(which='minor', color='#CCCCCC', linestyle=':')

ax.set_xlabel("cardID")
ax.set_ylabel("changes")

ax.get_figure().savefig('StateChangesPerCard.svg', format='svg')
plt.clf()


# Login frequency / Day

df = pd.read_sql_query("SELECT * FROM login_history;", conn)

df['login_timestamp'] = pd.to_datetime(df['login_timestamp'], unit='s')


before = df[df.login_timestamp < pd.to_datetime(1527897600, unit='s')]
ax = before.groupby(before.login_timestamp.dt.date).size().plot(title='Login frequency / Day')

after = df[df.login_timestamp > pd.to_datetime(1527897600, unit='s')]
after.groupby(after.login_timestamp.dt.date).size().plot(ax=ax, title='Login frequency / Day')

ax.legend(['Login frequency / Day (Before)', 'Login frequency / Day (After)'])

ax.get_figure().savefig('DailyLoginFrequency.svg', format='svg')
plt.clf()


# Unique users / Day

before = df[df.login_timestamp < pd.to_datetime(1527897600, unit='s')].drop_duplicates(['user_id'])
ax = before.groupby(before.login_timestamp.dt.date).size().plot(title='Unique users / Day')

after = df[df.login_timestamp > pd.to_datetime(1527897600, unit='s')].drop_duplicates(['user_id'])
after.groupby(after.login_timestamp.dt.date).size().plot(ax=ax, title='Unique users / Day')

ax.legend(['Unique users / Day (Before)', 'Unique users / Day (After)'])

ax.get_figure().savefig('DailyUniqueUsers.svg', format='svg')
plt.clf()
