import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'
# I use ChatGPT trying to get year which i did but ended up messing up my whole code forgeting to use query so my code did't work
def get_big_mac_price_by_year(year,country_code):
    df = pd.read_csv('./big-mac-full-index.csv')
    filtered_data = df[(df['iso_a3'].str.lower() == country_code.lower()) & (df['date'].str.contains(str(year)))]
    if not filtered_data.empty:
        return round(filtered_data['dollar_price'].mean(), 2)
    else:
        return f"No data available for {country_code.upper()} in {year}"

def get_big_mac_price_by_country(country_code):
    df = pd.read_csv('./big-mac-full-index.csv')
    Cou_Code = df.query("iso_a3.str.lower() == @country_code.lower()")
    den = print(Cou_Code[['iso_a3']])
    den_price = round(Cou_Code['dollar_price'].mean(),2)
    return den_price

def get_the_cheapest_big_mac_price_by_year(year):
    df = pd.read_csv('./big-mac-full-index.csv')
    filtere_data = df[df['date'].str.contains(str(year))]
    if not filtere_data.empty:
        max_price_row = filtere_data.loc[filtere_data['dollar_price'].idxmax()]
        result = f"{max_price_row['name']}({max_price_row['iso_a3']}): ${max_price_row['dollar_price']:.1}"
        return result
    else:
        return f"No data available for the year {year}"
    

def get_the_most_expensive_big_mac_price_by_year(year):
    df = pd.read_csv('./big-mac-full-index.csv')
    filtered_data = df[df['date'].str.contains(str(year))]
    if not filtered_data.empty:
        max_price_row = filtered_data.loc[filtered_data['dollar_price'].idxmax()]
        result = f"{max_price_row['name']}({max_price_row['iso_a3']}): ${max_price_row['dollar_price']:.1f}"
        return result
    else:
        return f"No data available for the year {year}"
     

if __name__ == "__main__":
    mac1 = get_big_mac_price_by_year(2008,'rus')
    print(mac1)

    mac2 = get_big_mac_price_by_country("rus")
    print(mac2)

    mac3 = get_the_cheapest_big_mac_price_by_year(2008)
    print(mac3)

    mac4 = get_the_most_expensive_big_mac_price_by_year(2014)
    print(mac4)