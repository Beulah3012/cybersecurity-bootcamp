#Create log_analyzer_pandas.py.
#Use logs.csv from walkthrough.
#Group by IP, sum counts.
#Example output: IP 192.168.1.1: 5


import pandas as pd
df = pd.read_csv("logs.csv")
result = df.groupby("ip")["count"].sum()
for ip, count in result.items():
    print(f"IP {ip}: {count}")
