import pandas as pd

df = pd.read_excel('database.xlsx')
df['pay_by'] = df['pay_by'].dt.strftime('%B %d, %Y')S