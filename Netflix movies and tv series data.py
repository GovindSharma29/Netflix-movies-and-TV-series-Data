import pandas as pd
df = pd.read_csv("C:/Users/samar/Downloads/netflix_titles.csv")
df.replace(r'^\s*$', pd.NA, regex=True, inplace=True)
df['director'].fillna('Not Available', inplace=True)
df['cast'].fillna('Not Available', inplace=True)
df['country'].fillna('Not Available', inplace=True)
df['date_added'].fillna('Not Available', inplace=True)
df['rating'].fillna('Not Rated', inplace=True)
df['duration'].fillna('Not Specified', inplace=True)
output_path = "C:/Users/samar/Documents/netflix_cleaned file.xlsx"
df.to_excel(output_path, index=False)
print(f"File saved to: {'C:/Users/samar/Documents/netflix_cleaned file.xlsx'}")