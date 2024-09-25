import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'

def get_big_mac_price_by_year(year,country_code):
    df = pd.read_csv('./big-mac-full-index.csv')

def get_big_mac_price_by_country(country_code):
    df = pd.read_csv('./big-mac-full-index.csv')
    Cou_Code = df.query("iso_a3.str.lower() == @country_code.lower()")
    # den = print(Cou_Code[['iso_a3']])
    den_price = round(Cou_Code['dollar_price'].mean(),2)
    return den_price

    

def get_the_cheapest_big_mac_price_by_year(year):
    df = pd.read_csv('./big-mac-full-index.csv')
    yr_query =
    min =
    result = ('Malaysia(MYS): $%.1f' % (min))

def get_the_most_expensive_big_mac_price_by_year(year):
    df = pd.read_csv('./big-mac-full-index.csv')
    yr_query =
    max =
    result = ('Malaysia(MYS): $%.1f' % (max))
    return result

if __name__ == "__main__":
    mac1 = get_big_mac_price_by_year(2008,'rus')
    print(mac1)
    mac2 = get_big_mac_price_by_country("rus")
    print(mac2)
    mac3 = get_the_cheapest_big_mac_price_by_year()
    print(mac3)
    mac4 = get_the_most_expensive_big_mac_price_by_year()
    print(mac4)